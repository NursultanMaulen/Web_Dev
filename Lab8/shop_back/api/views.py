from django.http import JsonResponse
from django.shortcuts import render
from api.models import Product, Category

def product_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(product.to_json())


def category_list(request):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    return JsonResponse(category.to_json())


def category_item_list(request, category_id):
    ans = []
    try:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        for product in products_json:
            if product['category_id'] == category_id:
                ans.append(product)
    except Category.DoesNotExist as exception:
        return JsonResponse({'message': str(exception)}, status=400)

    return JsonResponse(ans, safe=False)
