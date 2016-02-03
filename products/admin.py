from django.contrib import admin
from .models import Product
from .models import Favourite
#admin.site.register(Product)
#./manage.py createsuperuser
#admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ("name", "category", "description", "price", "id")
    list_filter = ('category',)
@admin.register(Favourite)
class AdminProduct(admin.ModelAdmin):
    list_display = ("user", "product")
