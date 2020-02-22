import { Component, OnInit } from '@angular/core';
import {Product} from '../product';
import { ProductSerService } from '../product-ser.service';
import {Category} from '../category';
import {ActivatedRoute} from '@angular/router';
import {CategoryService} from '../category.service';
import {PRODUCTS} from '../products';
import {PRODUCTS1} from '../products1';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {

  constructor(private productService: ProductSerService, private route: ActivatedRoute, private categoryService: CategoryService) {}

  products: Product[];
  categories: Category;

  /*getProducts(): void {
    this.productService.getProducts()
      .subscribe(products => this.products = products);
  }*/

  getCategory() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getCategory(id)
      .subscribe(categories => this.categories = categories);
  }

  getProducts() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProductsById(id).subscribe(products => this.products = products);
  }

  ngOnInit() {
    this.getCategory();
    this.getProducts();
  }
}
