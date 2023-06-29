from django.shortcuts import render
from django.utils import timezone

from feedback.forms import FeedbackForm
from gallery.forms import GalleryForm
from gallery.models import Gallery
from time_action.forms import ActionForm
from time_action.models import Action


def asdf():
    time = Action.objects.latest('date')

    if time and time.date > timezone.now():
        action_js = str(time.date.strftime('%Y-%m-%dT%H:%M:%S'))

        return action_js


def index(reqest):
    """Главная страница."""

    template = 'base.html'
    form_feetdback = FeedbackForm()
    form_gallery = GalleryForm()
    form_action = ActionForm()
    action = Action.objects.last()
    gallery = Gallery.objects.all()
    context = {
        'form_feetdback': form_feetdback,
        'form_gallery': form_gallery,
        'form_action': form_action,
        'gallery': gallery,
        'action': action,
        'action_js': asdf(),
    }

    return render(reqest, template, context)
