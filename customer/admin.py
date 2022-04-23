from django.contrib import admin
from .models import  customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
	list_display = ('name','email')
	search_fields = ['name']
	list_filter = ('name','email')
admin.site.register(customer,CustomerAdmin)