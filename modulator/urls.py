from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

print(settings.STATIC_ROOT)
urlpatterns = [
    path('', views.home_view, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 