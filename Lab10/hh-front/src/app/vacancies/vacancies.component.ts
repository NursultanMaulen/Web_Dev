import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {VacancyService} from "./vacancy.service";
import {Vacancy} from "../models";

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit{
  constructor(private vacancyService: VacancyService, private route: ActivatedRoute) {
    this.vacancies = [];
  }

  vacancies: Vacancy[];

  ngOnInit(): void{
    this.getCompanyId();
  }
  getCompanyId(){
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.vacancyService.getVacancies(id).subscribe((vacancies) => {
        this.vacancies = vacancies;
      })
    })
  }
  deleteVacancy(id: number){
    this.vacancyService.deleteVacancy(id).subscribe((data)=>
    this.vacancies = this.vacancies.filter((vacancy)=>vacancy.id != id))
  }

}
