import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views.generic import ListView
from api.models import Company, Vacancy

from api.serializers import CompanySerializer1, CompanySerializer2, VacancySerializer

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer1(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company = Company.objects.create(name=company_name)
        return JsonResponse(company.to_json())

class CompanyListView(ListView):
    def get(self, request):
        if request.method == 'GET':
            companies = Company.objects.all()
            serializer = CompanySerializer1(companies, many=True)
            return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_company_name = data.get('name', company.name)
        new_company_description = data.get('description', company.description)
        new_company_city = data.get('city', company.city)
        new_company_address = data.get('address', company.address)

        # desc = data.get('desc', company.desc)

        company.name = new_company_name
        company.description = new_company_description
        company.city = new_company_city
        company.address = new_company_address
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})

@csrf_exempt
def vacancy_list(request):
    # select * from auth_product;
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancy_name = data.get('name', '')
        vacancy_company_id = data.get('company_id', '1')
        vacancy = Vacancy.objects.create(name=vacancy_name, company_id = vacancy_company_id)
        return JsonResponse(vacancy.to_json())

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        new_vacancy_name = data.get('name', vacancy.name)
        new_vacancy_company_id = data.get('company_id', vacancy.company_id)
        new_vacancy_description = data.get('description', vacancy.description)
        new_vacancy_salary = data.get('salary', vacancy.salary)

        # desc = data.get('desc', vacancy.desc)

        vacancy.name = new_vacancy_name
        vacancy.salary = new_vacancy_salary
        vacancy.description = new_vacancy_description
        vacancy.company_id = new_vacancy_company_id
        vacancy.save()

        return JsonResponse(vacancy.to_json())

    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    vacancies = Vacancy.objects.filter(company_id = company_id)
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe= False)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe= False)