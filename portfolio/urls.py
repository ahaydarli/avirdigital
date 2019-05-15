from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name='portfolio-index'),
    path('view/<int:id>/', views.view, name='portfolio-view')
]