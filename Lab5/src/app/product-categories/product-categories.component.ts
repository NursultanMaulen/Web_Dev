import { Component } from '@angular/core';
import {RouterModule} from "@angular/router";

import {categories, Category} from "./categories";
import { products } from "./products";

@Component({
  selector: 'app-product-categories',
  templateUrl: './product-categories.component.html',
  styleUrls: ['./product-categories.component.css']
})

export class ProductCategoriesComponent {

    categories = categories;
    products = products;

    static current_id: number;

    constructor() {
    }


    visit(id: number){
        ProductCategoriesComponent.current_id = id;
    }

}
