import {Component, OnInit} from '@angular/core';
import {Vacancy} from '../models';
import {CompanyService} from '../services/company.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[];

  constructor(private companyService: CompanyService,
              public route: ActivatedRoute) {
  }

  ngOnInit(): void {
    this.getVacanciesList();
  }

  getVacanciesList() {
    let id = this.route.snapshot.paramMap.get('id');
    this.companyService.getVacancyList(id)
      .subscribe(vacancies => {
        this.vacancies = vacancies;
      });
  }

}
