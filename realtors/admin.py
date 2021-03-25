from django.contrib import admin
# Register your models here
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date')
    list_display_links = ('id', 'name', 'phone',)
    search_fields = ('name', 'id', 'phone', 'email', 'hire_date',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
