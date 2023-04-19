import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {VacanciesComponent} from "./vacancies/vacancies.component";
import {AppComponent} from "./app.component";

const routes: Routes = [
  {path: ':id/vacancies', component: VacanciesComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
