from django.contrib import admin
from gallery.models import Gallery, Tag


@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
    list_display = ('image', 'pub_date', )
    list_filter = ('tags',)
