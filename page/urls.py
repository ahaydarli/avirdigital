from django.urls import path
from . import views

urlpatterns = [
    path('view/<int:id>', views.view, name='page-view')
]