import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import { Vacancy } from "../models";

@Injectable({
  providedIn: 'root'
})

export class VacancyService {
  BASE_URL = 'http://localhost:8000'

  constructor(private client: HttpClient) { }

  getVacancies(company_id: number): Observable<Vacancy[]>{
    console.log('asdasd');
    return this.client.get<Vacancy[]>(
      `${this.BASE_URL}/api/companies/${company_id}/vacancies/`
    )
  }

  addVacancy(vacancy_name:string, vacancy_description:string, vacancy_salary:number, vacancy_company:number){
    return this.client.post<Vacancy>(`${this.BASE_URL}/api/vacancies/`,
      {name:vacancy_name, description:vacancy_description, salary:vacancy_salary, company_id:vacancy_company})
  }

  deleteVacancy(id:number){
    return this.client.delete<any>(`${this.BASE_URL}/api/vacancies/${id}/`)
  }

  updateVacancy(id: number, name: string, salary: number, description: string, company: number): Observable<Vacancy> {
    return this.client.put<Vacancy>(`${this.BASE_URL}/api/vacancies/${id}/`, {
      name: name,
      company_id: company,
      description: description,
      salary: salary
    })
  }

}
