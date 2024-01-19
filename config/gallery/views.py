from django.shortcuts import render, redirect
from .models import Image
from .forms import GalleryItemForm
from django.contrib import messages

# Create your views here.

def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('gallery:image_gallery')
    else:
        messages.success(request, "note save")
        form = GalleryItemForm()

    messages.success(request, "save")
    return render(request, 'gallery/add_img.html', {'form': form})
