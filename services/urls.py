from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='service-index'),
    path('<slug:slug>', views.view, name='service-view')
]