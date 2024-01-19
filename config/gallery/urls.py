from django.urls import path
from .views import add_gallery_item

app_name = 'gallery'

urlpatterns = [
    path('add/', add_gallery_item, name='image_gallery'),
]
