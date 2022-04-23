from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'vendor'


urlpatterns = [
    path('', views.vendors, name="vendors"),
    path('register/', views.register, name="register"),
    path('vendor-admin/', views.vendor_admin, name="vendor-admin"),
    


    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/',auth_views.LoginView.as_view(template_name="vendor/login.html"), name="login"),

    path('<int:vendor_id>/', views.vendor, name="vendor"),
]
