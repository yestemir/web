import {Component, OnInit} from '@angular/core';
import {Company} from '../models';
import {CompanyService} from '../services/company.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  companies: Company[];

  constructor(private companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompaniesList();
  }

  getCompaniesList() {
    this.companyService.getCompanyList()
      .subscribe(companies => {
        this.companies = companies;
      });
  }

}
