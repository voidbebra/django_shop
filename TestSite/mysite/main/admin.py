from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Prod

@admin.register(Prod)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_sale', 'sale_price', 'image_show']
    list_filter = ['is_sale']

    def image_show(self, obj):
        if obj.img:
            return mark_safe("<img src='{}' width='70' />".format(obj.img.url))
        return "None"