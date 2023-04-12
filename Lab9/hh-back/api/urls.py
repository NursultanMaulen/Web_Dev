from django.urls import path, re_path
from api import views

urlpatterns = [
    # path('categories/', views.category_list),
    # path('categories/<int:category_id>/', views.category_detail),

    path('companies/', views.company_list),
    path('companies/<int:company_id>/', views.company_detail),
    path('companies/<int:company_id>/vacancies/', views.company_vacancies),


    # path('products/', views.product_list),
    # path('products/<int:product_id>/', views.product_detail),

    path('vacancies/', views.vacancy_list),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail),
    path('vacancies/top_ten', views.top_ten_vacancies)
]
