from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('view/<int:id>', views.view, name='blog-view'),
    path('category/<int:category_id>', views.category, name='blog-category')
]