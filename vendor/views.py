from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm  

from .models import Vendor
from product.models import Product
from .forms import ProductForm

# Converting Title into Slug
from django.utils.text import slugify

# Create your views here.


def vendors(request):
    return render(request, 'vendor/vendors.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            vendor = Vendor.objects.create(name=user.username,email = user.email, password=user.password)

            return redirect('core:home')
    else:
        form = CustomUserCreationForm()   

    return render(request, 'vendor/become_vendor.html', {'form': form})


@login_required
def vendor_admin(request):
    name = request.user
    idx = name.id
    user = Vendor.objects.get(id=idx);
    return render(request, 'vendor/vendor_admin.html', {'user': user, 'idx':idx, 'name':name})


def vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    return render(request, 'vendor/vendor.html', {'vendor': vendor})


