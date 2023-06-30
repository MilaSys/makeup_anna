import os
from django.shortcuts import render
from dotenv import load_dotenv
from telegram import Bot

from .forms import FeedbackForm
from .models import Feedback
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

load_dotenv()

NUMBER_OF_ENTRIES = 10
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
bot = Bot(token=TELEGRAM_TOKEN)


def send_message(bot, message):
    """Отправка сообщения в Телеграмм."""
    chat_id = TELEGRAM_CHAT_ID
    bot.send_message(chat_id, message)


def feedback(request):
    """Обратная связь."""
    if request.method == 'POST':
        form_feetdback = FeedbackForm(request.POST)
        if form_feetdback.is_valid():
            name = form_feetdback.cleaned_data['name']
            phone = form_feetdback.cleaned_data['phone']
            m = f'{name}, {phone}'
            send_message(bot, m)
            form_feetdback.save()
            return redirect('index')
        return render(request, 'base.html', {'form_feetdback': form_feetdback})
    form_feetdback = FeedbackForm()
    return render(request, 'base.html', {'form_feetdback': form_feetdback})


@login_required
def customer(request):
    client = Feedback.objects.order_by('-created_at')[:NUMBER_OF_ENTRIES]
    context = {
        'client': client,
    }
    return render(request, 'base.html', context)
