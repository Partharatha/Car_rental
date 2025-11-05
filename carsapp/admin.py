from django.contrib import admin
from.models import Company,Products,ProductInteriorImgs,ProductExteriorImgs

# Register your models here.

admin.site.register(Company)
admin.site.register(Products)
admin.site.register(ProductInteriorImgs)
admin.site.register(ProductExteriorImgs)
