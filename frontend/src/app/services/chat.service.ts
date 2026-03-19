import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {

  private apiUrl = 'http://localhost:8000/chat';

  constructor(private http: HttpClient) {}

  sendQuery(query: string): Observable<any> {
    const body = { query: query };
    return this.http.post<any>(this.apiUrl, body);
  }
}
