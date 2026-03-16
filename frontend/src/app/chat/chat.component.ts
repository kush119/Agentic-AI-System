import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { v4 as uuidv4 } from 'uuid';
import { ChatService } from '../services/chat.service';

interface Message {
  role: 'user' | 'assistant' | 'error';
  content: string;
  time: string;
}

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  sessionId = '';
  input = '';
  sending = false;
  messages: Message[] = [];
  errorText = '';

  constructor(private chat: ChatService) {}

  ngOnInit(): void {
    this.sessionId = localStorage.getItem('chat_session_id') ?? uuidv4();
    localStorage.setItem('chat_session_id', this.sessionId);
  }

  // ✅ CALLED BY (click)="onReset()"
  onReset(): void {
    this.messages = [];
    this.errorText = '';
    this.input = '';
  }

  // ✅ CALLED BY (keydown)="onKeydown($event)"
  onKeydown(event: KeyboardEvent): void {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.onSend();
    }
  }

  // ✅ Send message to backend
  onSend(): void {
    const text = this.input.trim();
    if (!text || this.sending) return;

    this.messages.push({
      role: 'user',
      content: text,
      time: new Date().toISOString()
    });

    this.input = '';
    this.sending = true;

    this.chat.sendMessage({
      session_id: this.sessionId,
      message: text
    }).subscribe({
      next: (res) => {
        this.messages.push({
          role: 'assistant',
          content: res.answer ?? '(no response)',
          time: new Date().toISOString()
        });
        this.sending = false;
      },
      error: (err) => {
        this.errorText = err.message || 'Request failed';
        this.sending = false;
      }
    });
  }
}