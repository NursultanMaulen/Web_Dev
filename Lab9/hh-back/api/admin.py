from django.contrib import admin
from api.models import Company, Vacancy


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'address')


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'price', 'category')

@admin.register(Vacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'company')
