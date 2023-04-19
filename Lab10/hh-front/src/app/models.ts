export interface Company {
  id: number;
  name: string;
}
export interface Vacancy {
  id: number;
  company_id: number;
  salary: number;
  description: string;
  name: string;
}
