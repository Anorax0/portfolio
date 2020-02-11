from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('projects', views.projects, name='projects'),
    path('projects/<project>', views.projects, name='projects')
]
