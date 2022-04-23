from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'vendor/become_vendor.html', {'form': form})