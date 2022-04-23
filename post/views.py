from django.shortcuts import render
from .models import cate_post, post
from django.shortcuts import redirect, render, get_object_or_404


# Create your views here.

def category(request, category_slug):
    category = get_object_or_404(cate_post, cate_post_slug=category_slug)
    posts= post.objects.filter(cate_post_id=category.id)
    return render(request,'product/cate_post.html', {'category': category,'posts':posts})
