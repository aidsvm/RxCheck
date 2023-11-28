
from . import views
from django.urls import path, include

urlpatterns = [
    path('search_drug/', views.search_drug, name='search_drug'),
]