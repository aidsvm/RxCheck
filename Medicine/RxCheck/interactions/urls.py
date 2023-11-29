
from . import views
from django.urls import path, include

urlpatterns = [
    path('search_drug/', views.search_drug, name='search_drug'),
    path('search_results/', views.search_results, name='search_results'),
    path('login/', views.login_page, name='login_page'),
    path('', views.index, name='index'),
]