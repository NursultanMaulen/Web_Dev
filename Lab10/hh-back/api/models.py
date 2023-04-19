from django.db import models

'''
Model/Table relations

1) OneToOne - each "User" can have only one "Profile"
2) OneToMany - each "Category" can have many "Products"
3) ManyToMany - each "Post" can have many "Tags", in the same time, one "Tag" can in in multiple "Posts"
'''


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return f'{self.id}: {self.name}'
#
#     def to_json(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.FloatField(default=1000)
#     category = models.ForeignKey(Category,
#                                  on_delete=models.CASCADE,
#                                  related_name='products')
#
#     class Meta:
#         verbose_name = 'Product'
#         verbose_name_plural = 'Products'
#
#     def __str__(self):
#         return f'{self.id}: {self.name}'
#
#     def to_json(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'price': self.price
#         }


class Company(models.Model):
    name = models.CharField(max_length=255, default='Lolek')
    description = models.TextField(max_length=255, default='Lolek description')
    city = models.CharField(max_length=255, default='Lolek city')
    address = models.TextField(max_length=255, default='Lolek address')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

class Vacancy(models.Model):
    name = models.CharField(max_length=255, default='Lolek name')
    description = models.TextField(max_length=255, default='Lolek description')
    salary = models.FloatField(default=1000)
    company = models.ForeignKey(Company,
                                 on_delete=models.CASCADE,
                                 related_name='vacancies')

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }
