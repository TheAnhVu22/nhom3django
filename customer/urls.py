from . import views
from django.urls import path


app_name = 'customer'


urlpatterns = [
     path('register/', views.register, name="register"),
]
