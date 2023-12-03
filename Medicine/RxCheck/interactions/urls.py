
from . import views
from django.urls import path

urlpatterns = [
    path('search_drug/', views.search_drug, name='search_drug'),
    path('compare_drugs/', views.compare_drugs, name='compare_drugs'),
    path('search_results/', views.search_results, name='search_results'),
    path('', views.index, name='index'),
]