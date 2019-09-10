from django.urls import path
from . import views
from .views import ListImages

urlpatterns = [
    path('', ListImages.as_view(), name='gallery'),
    path('add', views.add, name='add'),
]