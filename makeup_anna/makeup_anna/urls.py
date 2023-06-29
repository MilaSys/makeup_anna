from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('action/', include('time_action.urls', namespace='action')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    # path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
