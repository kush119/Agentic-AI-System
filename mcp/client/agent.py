import json
import re
from llm.config import get_llm_client, AZURE_OPENAI_MODEL
from llm.prompts import SYSTEM_PROMPT, USER_WRAPPER
from client import MCPClient


class Agent:
    def __init__(self):
        self.mcp = MCPClient()
        self.llm = get_llm_client()

    async def handle_query(self, user_query: str):
        # 1. Build LLM messages
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_WRAPPER.format(user_query=user_query)}
        ]

        # 2. Call Azure OpenAI (NO temperature for GPT‑5 / preview models)
        response = self.llm.chat.completions.create(
            model=AZURE_OPENAI_MODEL,
            messages=messages
        )

        # ✅ FIX 1: message is an object, not a dict
        content = response.choices[0].message.content.strip()

        # 3. Try to parse JSON decision (tool mode)
        decision = self._safe_json_parse(content)

        # ✅ If JSON parsing fails → LLM‑only response (NO 500)
        if decision is None:
            return {
                "type": "llm_only",
                "message": content
            }

        tool = decision.get("tool")
        args = decision.get("arguments", {})
        final_answer = decision.get("final_answer", "")

        # 4. No tool required → return final answer
        if not tool:
            return {
                "type": "llm_only",
                "message": final_answer
            }

        # 5. Call MCP tool safely
        try:
            tool_result = await self.mcp.call_tool(tool, args)
        except Exception as e:
            return {
                "type": "tool_error",
                "tool": tool,
                "error": str(e)
            }

        # 6. Return combined result
        return {
            "type": "tool_response",
            "message": final_answer,
            "tool_used": tool,
            "tool_arguments": args,
            "tool_result": (
                tool_result.data if hasattr(tool_result, "data") else tool_result
            )
        }

    # ─────────────────────────────────────────────
    # Helpers
    # ─────────────────────────────────────────────
    def _safe_json_parse(self, text: str):
        """
        Attempts to extract and parse JSON from LLM output.
        Returns None if parsing fails.
        """
        try:
            # Remove ```json ``` wrappers if present
            cleaned = re.sub(r"```json|```", "", text).strip()
            return json.loads(cleaned)
        except Exception:
            return None