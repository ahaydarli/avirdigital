from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.translation import gettext as _
from django.utils import translation
from django.http import HttpResponseRedirect
from portfolio.models import Portfolio, PortfolioCategory
from .forms import ContactForm
from django.core.mail import BadHeaderError, EmailMessage
from services.models import Service
from blog.models import Blog
from partners.models import Partner
from django.conf import settings
from about.models import About


# Create your views here.

def index(request):
    services = Service.objects.all().filter(home=True).order_by('position')[:5]
    portfolios = Portfolio.objects.all().filter(home=True).order_by('position')
    portfolio_categories = PortfolioCategory.objects.all()
    blogs = Blog.objects.all()[:3]
    partners = Partner.objects.all()
    return render(request, 'index.html', {
        'services': services,
        'portfolios': portfolios,
        'portfolio_categories': portfolio_categories,
        'blogs': blogs,
        'partners': partners
    })


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            try:
                send_email = EmailMessage(full_name,
                                          message,
                                          email,
                                          ['contact@avirdigital.az'],
                                          reply_to=['contact@avirdigital.az']
                                          )
                send_email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})


def about(request):
    about_items = About.objects.all()
    partners = Partner.objects.all()
    return render(request, 'about.html', {
        'about_items': about_items,
        'partners': partners
    })


