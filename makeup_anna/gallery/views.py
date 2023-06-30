from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import GalleryForm

User = get_user_model()


@login_required
def gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'base.html', {'form': form})
    form = GalleryForm()
    return render(request, 'base.html', {'form': form})
