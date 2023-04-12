import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Company, Vacancy


# CRUD - CRATE, READ, UPDATE, DELETE

# @csrf_exempt
# def category_list(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         categories_json = [p.to_json() for p in categories]
#         return JsonResponse(categories_json, safe=False)
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         category_name = data.get('name', '')
#         category = Category.objects.create(name=category_name)
#         return JsonResponse(category.to_json())
#
#
# @csrf_exempt
# def category_detail(request, category_id):
#     try:
#         category = Category.objects.get(id=category_id)
#     except Category.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)
#
#     if request.method == 'GET':
#         return JsonResponse(category.to_json())
#     elif request.method == 'PUT':
#         data = json.loads(request.body)
#         new_category_name = data.get('name', category.name)
#         # desc = data.get('desc', category.desc)
#         category.name = new_category_name
#         category.save()
#         return JsonResponse(category.to_json())
#     elif request.method == 'DELETE':
#         category.delete()
#         return JsonResponse({'deleted': True})
#
#
# def product_list(request):
#     # select * from auth_product;
#     products = Product.objects.all()
#     products_json = [p.to_json() for p in products]
#     return JsonResponse(products_json, safe=False)
#
#
# def product_detail(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)
#
#     return JsonResponse(product.to_json())

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [c.to_json() for c in companies]
        return JsonResponse(companies_json, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        company_name = data.get('name', '')
        company = Company.objects.create(name=company_name)
        return JsonResponse(company.to_json())


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
        vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(vacancies_json, safe=False)
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
