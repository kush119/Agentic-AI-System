import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ChatService {
  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  sendMessage(payload: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/chat`, payload);
  }
}