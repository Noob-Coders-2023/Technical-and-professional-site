from django.shortcuts import render, redirect
from .models import Image
from .forms import GalleryItemForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404

# Create your views here.

def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "عکس شما با موفقیت آپلود شد.", 'success')
            return redirect('gallery:image_gallery')
    else:
        # messages.error(request, "متاسفانه وعکس شما با موفقیت آپلود نشد.لطفا مجددا تلاش کنید.",extra_tags='error')
        form = GalleryItemForm()

    # messages.success(request, "عکس شما با موفقیت آپلود شد.",'success')
    return render(request, 'gallery/add_img.html', {'form': form})
def slide_detail(request, id):
    image = get_object_or_404(Image, pk=id)
    return render(request, 'gallery/slide_detail.html', {'image': image})