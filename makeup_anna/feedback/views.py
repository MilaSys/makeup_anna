from django.shortcuts import render
from .forms import FeedbackForm
from .models import Feedback
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

NUMBER_OF_ENTRIES: int = 10

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            form.save()
            return redirect('/thank-you/')
        return render(request, 'contact.html', {'form': form})
    form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})


@login_required
def customer(request):
    client = Feedback.objects.order_by('-created_at')[:NUMBER_OF_ENTRIES]
    context = {
        'client': client,
    }
    return render(request, 'posts/index.html', context)