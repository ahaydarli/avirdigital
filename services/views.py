from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service
# Create your views here.

def index(request):
    services = Service.objects.all().order_by('position')
    return render(request, 'services/index.html', {'services': services})

def view(request, slug):
    service = Service.objects.get(slug=slug)
    return render(request, 'services/view.html', {'service': service})

