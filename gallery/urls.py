from django.urls import path
from .views import add_gallery_item, slide_detail

app_name = 'gallery'

urlpatterns = [
    path('add/', add_gallery_item, name='image_gallery'),
    path('slide/<int:id>/', slide_detail, name='slide_detail'),
]
