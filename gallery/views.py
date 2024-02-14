from django.shortcuts import render, redirect
from .models import Image
from .forms import GalleryItemForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from extension.utils import persian_number_converter
from jdatetime import datetime
# Create your views here.

def add_gallery_item(request):
    if request.method == 'POST':
        form = GalleryItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "عکس شما با موفقیت آپلود شد.", 'success')
            return redirect('gallery:image_gallery')
        else:
            messages.error(request, "متاسفانه وعکس شما با موفقیت آپلود نشد.لطفا مجددا تلاش کنید.", 'error')


    else:
        form = GalleryItemForm()


    return render(request, 'gallery/add_img.html', {'form': form})

def galleries(request):
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    gallery_list = Image.objects.all()
    context = {
        'gallery_list': gallery_list,
        'current_date': current_date
    }
    return render(request, 'gallery/detail-imgs.html', context)




def slide_detail(request, id):
    current_date = persian_number_converter(str(datetime.now().strftime("%Y/%m/%d")))
    image = get_object_or_404(Image, pk=id)
    context={
        'current_date': current_date,
        'image': image
    }

    return render(request, 'gallery/slide_detail.html', context)