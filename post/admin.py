from django.contrib import admin
from .models import cate_post, post
# Register your models here.
class CatePostAdmin(admin.ModelAdmin):
	list_display = ('cate_post_name','cate_post_slug')
	search_fields = ['cate_post_name']
admin.site.register(cate_post,CatePostAdmin)

class PostAdmin(admin.ModelAdmin):
	list_display = ('post_name','post_slug','post_content','post_image','post_author','cate_post_id')
	search_fields = ['post_name','post_author']
	list_filter = ('post_name','post_author')
admin.site.register(post,PostAdmin)