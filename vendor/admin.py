from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
	list_display = ('name','email')
	search_fields = ['name']
	list_filter = ('name','email')
admin.site.register(Vendor,VendorAdmin)
