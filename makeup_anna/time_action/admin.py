from django.contrib import admin

from time_action.models import Action
from django.contrib import admin


@admin.register(Action)
class Action(admin.ModelAdmin):

    # @admin.display(description='date')
    # def admin_date(self, obj):
    #     return obj.date.strftime("%B %d, %Y")
    list_display = ('discount', 'date')
    search_fields = ('discount',)
    list_filter = ('discount',)
