import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product, products } from '../products';
import {CartService} from "../cart.service";
// import {Category, categories} from "../categories";

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css'],
})


export class ProductListComponent implements OnInit{
  products = products;
  // category: Category | undefined;

  curId = 0;

  constructor(
      private route: ActivatedRoute,
  ) {}

  ngOnInit(): void{
    const routeParams = this.route.snapshot.paramMap;
    const productIdFromRoute = Number(routeParams.get('categoryId'));
    this.curId = productIdFromRoute;
  }



  share(lin: string) {
    window.open('https://t.me/share/url?url=' + lin);
    // window.alert('The product has been shared!');
  }

  del(prod: Product) {
    prod.isActive = false;
  }

  like(prod: Product) {
    prod.likes++;
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
