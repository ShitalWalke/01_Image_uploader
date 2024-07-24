from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image


def upload_image(request):
    if request.method == 'POST':
        if 'upload' in request.POST:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('upload_image')
        elif 'delete' in request.POST:
            image_id = request.POST.get('delete')
            image = get_object_or_404(Image, id=image_id)
            image.delete()
            return redirect('upload_image')
    else:
        form = ImageForm()

    images = Image.objects.all()
    return render(request, 'uploader/upload_image.html', {'form': form, 'img': images})
