import {Component, OnInit} from '@angular/core';
import {Company} from './models'
import {CompanyService} from "./company.service";

import { Router } from '@angular/router';
import { VacanciesComponent } from './vacancies/vacancies.component'
import {VacancyService} from "./vacancies/vacancy.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'hh-front';

  companies: Company[] = [];
  newCompany: string = '';

  companyId: number = NaN;

  companyName: string = '';

  vacancyId: number = 1;
  vacancyName: string = '';
  vacancySalary: number = 1000;
  vacancyDescription: string = '';
  vacancyCompany: number = 2;

  constructor(private companyService: CompanyService,
              private vacancyService: VacancyService) {
  }

  ngOnInit() {
    this.companyService.getCompanies().subscribe((companies) => {
      this.companies = companies;
    });
  }


  addCompany() {
    this.companyService.createCompany(this.newCompany).subscribe((company) => {
      this.companies.push(company);
      this.newCompany = '';
    });
  }

  addVacancy(){
    this.vacancyService.addVacancy(this.vacancyName, this.vacancyDescription, this.vacancySalary,
      this.vacancyCompany).subscribe((vacancy)=>{
        this.vacancyName="";
        this.vacancyDescription="";
        this.vacancySalary=1000;
        this.vacancyCompany=NaN;
      })
  }

  deleteCompany(company_id: number) {
    this.companyService.deleteCompany(company_id).subscribe((data) => {
      this.companies = this.companies.filter((company) => company.id !== company_id);
    });
  }

  updateCompany(company_id: number, company_name: string){
    this.companyService.updateCompany(company_id, company_name).subscribe((company) => {
      console.log("Updated: true");
    })
  }

  updateVacancy(vacancy_id: number, vacancy_name: string, vacancy_salary: number,
                vacancy_description: string, vacancy_company: number){
    this.vacancyService.updateVacancy(vacancy_id, vacancy_name, vacancy_salary, vacancy_description, vacancy_company).subscribe((vacancy) => {
      console.log("Updated: true");
    })
  }

}
