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
        companies_json = [p.to_json() for p in companies]
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
        # desc = data.get('desc', company.desc)
        company.name = new_company_name
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})

def vacancy_list(request):
    # select * from auth_product;
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(vacancy.to_json())

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
