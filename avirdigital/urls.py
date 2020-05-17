"""avirdigital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from avirdigital import views
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


admin.site.site_header = "Avirdigital Admin"
admin.site.site_title = "Avirdigital Admin Portal"
admin.site.index_title = "Welcome to Avirdigital Admin"

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('portfolio/', include('portfolio.urls'), ),
    path('service/', include('services.urls')),
    path('blog/', include('blog.urls')),
    path('page/', include('page.urls')),
    path('filer/', include('filer.urls')),
    path('', views.index, name='home-index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),

)
urlpatterns += (
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('mailru-domaindImcPxrKGJBOVG1T.html', TemplateView.as_view(template_name="mailru-domaindImcPxrKGJBOVG1T.html")),
    # path('mailru-domaindImcPxrKGJBOVG1T.html', lambda r: HttpResponse("mailru-domain: dImcPxrKGJBOVG1T")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

