import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { ChatComponent } from './chat/chat.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, ChatComponent],
  template: `<app-chat></app-chat>`
})
export class AppComponent {}