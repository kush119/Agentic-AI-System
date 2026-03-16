from fastapi import APIRouter
from ..schema.chat import ChatRequest, ChatResponse
from ..services.agent_services import AgentService

router = APIRouter()
agent_service = AgentService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await agent_service.process_query(request.query)
    return ChatResponse(response=response)