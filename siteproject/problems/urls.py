from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('add/', addpage, name='add_page'),
    path('projects/<int:pr_id>', projectpage, name = 'project_page')
]