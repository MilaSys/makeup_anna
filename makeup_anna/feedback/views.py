from django.shortcuts import render
import os
from dotenv import load_dotenv
from telegram import Bot

from .forms import FeedbackForm
from .models import Feedback
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse

load_dotenv()

NUMBER_OF_ENTRIES = 10
# TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
# bot = Bot(token=TELEGRAM_TOKEN)


# def send_message(bot, message):
#     """Отправка сообщения в Телеграмм."""
#     chat_id = TELEGRAM_CHAT_ID
#     bot.send_message(chat_id, message)


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            # m = f'{name}, {phone}, {message}'
            # send_message(bot, m)
            form.save()
            return redirect('/thank-you/')
        return render(request, 'contact.html', {'form': form})
    form = FeedbackForm()
    return render(request, 'contact.html', {'form': form})


# @login_required
# def customer(request):
#     client = Feedback.objects.order_by('-created_at')[:NUMBER_OF_ENTRIES]
#     context = {
#         'client': client,
#     }
#     return render(request, 'posts/index.html', context)