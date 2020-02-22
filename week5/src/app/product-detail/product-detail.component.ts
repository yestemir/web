import { Component, OnInit, Input } from '@angular/core';
import {Product} from '../product';
import {ActivatedRoute} from '@angular/router';
import { Location } from '@angular/common';
import {ProductSerService} from '../product-ser.service';
import {PRODUCTS} from '../products';
import {PRODUCTS1} from '../products1';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {

  @Input() product: Product;
  products: Product[];

  constructor(
    private route: ActivatedRoute,
    private productService: ProductSerService,
    private location: Location
  ) {}

  ngOnInit(): void {
    this.getProduct();
  }

  getProduct() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id).subscribe(product => this.product = product);
  }

  goBack(): void {
    this.location.back();
  }
}
