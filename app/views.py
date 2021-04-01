from django.shortcuts import render
from app.models import Website
# Create your views here.
def home_view(request):
    name = "Welcome To"
    obj = Website.objects.get(id=2)

    context = {
        'name' : name,
        'obj': obj
    }

    return render (request, 'home.html', context)
    