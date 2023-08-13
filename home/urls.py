from django.urls import path
from . import views


urlpatterns =[
    path('', views.HomeView.as_view(), name='home.base'),
    path('about', views.AboutView.as_view(), name='about.base'),
    path('administration', views.AdministrationView.as_view(), name='administration.base'),
]