from . import views
from django.urls import path


app_name = 'post'


urlpatterns = [
     path('<slug:category_slug>/', views.category, name="category"),
]
