from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, PortfolioCategory, PortfolioImages
# Create your views here.
def index(request):
    portfolios = Portfolio.objects.all().order_by('position')
    portfolio_categories = PortfolioCategory.objects.all()
    return render(request, 'portfolio/index.html', {
        'portfolios': portfolios,
        'portfolio_categories': portfolio_categories
    })

def view(request, id):
    portfolio = Portfolio.objects.get(id=id)
    images = PortfolioImages.objects.all().filter(portfolio_id=portfolio.id)
    return render(request, 'portfolio/view.html', {
        'portfolio': portfolio,
        'images': images
    })
