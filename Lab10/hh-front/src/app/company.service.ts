import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import {Company} from "./models";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class CompanyService {

  BASE_URL = 'http://localhost:8000'

  constructor(private client: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.client.get<Company[]>(
      `${this.BASE_URL}/api/companies/`
    )
  }

  createCompany(companyName: string): Observable<Company> {
    return this.client.post<Company>(
      `${this.BASE_URL}/api/companies/`,
      {name: companyName}
    )
  }

  updateCompany(company_id: number, company_name: string): Observable<Company> {
    return this.client.put<Company>(
      `${this.BASE_URL}/api/companies/${company_id}/`,
      {
        name: company_name
      }
    )
  }

  deleteCompany(company_id: number): Observable<any> {
    return this.client.delete(
      `${this.BASE_URL}/api/companies/${company_id}/`
    )
  }
}
