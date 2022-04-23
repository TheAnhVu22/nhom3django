from django.contrib import admin

# Register your models here.

from .models import Category, Product, Brand, rating, comment

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title','slug')
	search_fields = ['title']
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
	list_display = ('title','slug')
	search_fields = ['title']

admin.site.register(Brand,BrandAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ('title','price','quantity','description','image','added_date')
	search_fields = ['title']
	list_filter = ('price','quantity')
admin.site.register(Product,ProductAdmin)


class RatingAdmin(admin.ModelAdmin):
	list_display = ('product_id','rating')
	search_fields = ['product_id']
	list_filter = ('product_id','rating')
admin.site.register(rating,RatingAdmin)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('comment_name','comment_content','product_id','comment_parent_id')
	search_fields = ['comment_name']
	list_filter = ('comment_name','comment_content','product_id')
admin.site.register(comment,CommentAdmin)