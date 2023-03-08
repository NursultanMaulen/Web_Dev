import { Component } from '@angular/core';
import { albums } from "../albums";
import {album_ids} from "../album-ids";

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent {
  album_ids = album_ids;
  // albums = albums;
}
