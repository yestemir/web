import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProductListComponent } from './product-list/product-list.component';
import {CategoryComponent} from './category/category.component';
import {ProductDetailComponent} from './product-detail/product-detail.component';

const routes: Routes = [
  { path: 'category', component: CategoryComponent },
  { path: 'category/:id/:products', component: ProductListComponent },
  { path: '', redirectTo: '/category', pathMatch: 'full' },
  { path: 'detail/:id', component: ProductDetailComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
