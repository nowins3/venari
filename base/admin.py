from django.contrib import admin
from .models import Product, Supplier, Brand, Rating, User, Type, Niche, Employees, Specification, Category
# Register your models here.

admin.site.register(Employees)
admin.site.register(Niche)
admin.site.register(Type)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Brand)
admin.site.register(Rating)
admin.site.register(Specification)
admin.site.register(Category)

