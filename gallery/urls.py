from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gallery'),
    path('<int:image_id>', views.image, name='image')
]
