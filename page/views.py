from django.shortcuts import render
from .models import Page
# Create your views here.

def view(request, id):
    page = Page.objects.get(id=id)
    return render(request, 'page/view.html', {
        'page': page,
    })
