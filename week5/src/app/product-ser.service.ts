import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import {PRODUCTS} from './products';
import {Product} from './product';

@Injectable({
  providedIn: 'root'
})
export class ProductSerService {
  constructor() { }

  getProducts(): Observable<Product[]> {
    return of(PRODUCTS);
  }

  getProduct(id: number): Observable<Product> {
    // TODO: send the message _after_ fetching the hero
    return of(PRODUCTS.find(product => product.id === id));
  }

  getProductsById(id: number): Observable<any> {
    return of(PRODUCTS.filter(product => product.category_id === id));
  }
}
