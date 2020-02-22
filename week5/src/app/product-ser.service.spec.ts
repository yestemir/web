import { TestBed } from '@angular/core/testing';

import { ProductSerService } from './product-ser.service';

describe('ProductServService', () => {
  let service: ProductSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProductSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
