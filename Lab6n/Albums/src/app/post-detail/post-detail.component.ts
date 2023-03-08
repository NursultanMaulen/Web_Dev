import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {POSTS} from "../fake-db";
import {Post} from "../models";
import {PostService} from "../post.service";

@Component({
  selector: 'app-post-detail',
  templateUrl: './post-detail.component.html',
  styleUrls: ['./post-detail.component.css']
})
export class PostDetailComponent implements OnInit{
  post: Post;
  loaded: boolean;

  newTitle: string;

  constructor(private route: ActivatedRoute,
              private postService: PostService) {
    this.post = {} as Post;
    this.loaded = true;
    this.newTitle = '';
  }

  ngOnInit(): void {
    // const id = Number(this.route.snapshot.paramMap.get('id'));
    // if(id){
    //   let num_id = +id;
    // }
    this.getPost();

  }

  getPost(){
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      // this.post = POSTS.find((post) => post.id === id) as Post;
      this.loaded = false;
      this.postService.getPost(id).subscribe((post) => {
        this.post = post;
        this.loaded = true;
      });
    })
  }

  updatePost(){
    this.loaded = false;
    const post_body = this.post.body;
    this.postService.updatePost(this.post.id, this.newTitle).subscribe((post) => {
      this.loaded = true;
      this.post = post;
      this.post.body = post_body;
      this.newTitle = '';
    });
  }

}
