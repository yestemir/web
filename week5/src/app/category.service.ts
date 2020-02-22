import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {Product} from './product';
import {PRODUCTS} from './products';
import {Category} from './category';
import {CATEGORIES} from './categories';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  constructor() { }


  getCategories(): Observable<Category[]> {
    return of(CATEGORIES);
  }

  getCategory(id: number): Observable<Category> {
    return of(CATEGORIES.find(product => product.id === id));
  }
}
