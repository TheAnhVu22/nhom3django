from product.models import Category, Brand
from post.models import cate_post


def menu_categories(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    cate_posts = cate_post.objects.all()
    return {'categories': categories, 'brands':brands,'cate_posts': cate_posts}