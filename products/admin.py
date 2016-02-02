from django.contrib import admin
from .models import Product
#admin.site.register(Product)
#./manage.py createsuperuser
#admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("name", "category", "description", "price", "id")
    list_filter = ('category',)
