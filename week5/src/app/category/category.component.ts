import { Component, OnInit } from '@angular/core';
import {Product} from '../product';
import {ProductSerService} from '../product-ser.service';
import {Category} from '../category';
import {CategoryService} from '../category.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {

  category: Category[] = [];

  constructor(private categoryService: CategoryService) { }

  ngOnInit() {
    this.getCategories();
  }

  getCategories(): void {
    this.categoryService.getCategories()
      .subscribe(category => this.category = category);
  }

}
