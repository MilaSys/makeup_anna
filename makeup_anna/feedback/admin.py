from django.contrib import admin
from feedback.models import Feedback


@admin.register(Feedback)
class Feedback(admin.ModelAdmin):
    list_display = ('name', 'phone', 'created_at',)
    search_fields = ('name',)
    list_filter = ('created_at', )
