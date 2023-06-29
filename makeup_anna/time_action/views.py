from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ActionForm


@login_required
def action(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'base.html', {'form': form})
    form = ActionForm()
    return render(request, 'base.html', {'form': form})
