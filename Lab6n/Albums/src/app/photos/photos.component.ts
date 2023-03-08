import {Component, OnInit} from '@angular/core';
import {Post} from "../models";
import {PostService} from "../post.service";
import {Photo} from "../photo-models";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-photos',
  templateUrl: './photos.component.html',
  styleUrls: ['./photos.component.css']
})
export class PhotosComponent implements OnInit{
  photos: Photo[];
  loaded: boolean;
  post_id: number;

  constructor(private postService: PostService, private route: ActivatedRoute) {
    this.photos = [];
    this.loaded = true;
    this.post_id = 0;
  }

  ngOnInit(): void {
    this.getPhotoss();
  }

  getPhotoss(){
    this.loaded = false;
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.post_id = id;
    })
    this.postService.getPhotos(this.post_id).subscribe((photos) =>{
      console.log(this.post_id);
      this.photos = photos;
      this.loaded = true;
    })
  }

}
