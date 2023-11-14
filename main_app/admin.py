from django.contrib import admin
from main_app.models import Product


# admin.site.register(Product)

@admin.register(Product)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'descriptions', )
