import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Post} from "./models";
import {Photo} from "./photo-models";

@Injectable({
  providedIn: 'root'
})
export class PostService {

  BASE_URL: string = 'https://jsonplaceholder.typicode.com'

  constructor(private client: HttpClient) { }

  getPosts(): Observable<Post[]>{
    return this.client.get<Post[]>(`${this.BASE_URL}/posts`);
  }

  getPost(id: number): Observable<Post> {
    return this.client.get<Post>(`${this.BASE_URL}/posts/${id}`);
  }

  addPost(post: Post): Observable<Post> {
    return this.client.post<Post>(`${this.BASE_URL}/posts`, post);
  }
  updatePost(id: number, newTitle: string): Observable<Post> {
    return this.client.put<Post>(`${this.BASE_URL}/posts/${id}`, { title: newTitle });
  }

  deletePost(id: number): Observable<Post>{
    return this.client.delete<Post>(`${this.BASE_URL}/posts/${id}`);
  }

  getPhotos(id: number): Observable<Photo[]>{
    return this.client.get<Photo[]>(`${this.BASE_URL}/albums/${id}/photos`);
  }

}
