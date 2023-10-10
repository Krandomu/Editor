from django.urls import path, re_path
from . import views, upload_views

urlpatterns = [
    path('add/', views.ContentHTMLAdd.as_view(), name='add'),
    re_path(r'^retrieve/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', views.ContentHTMLRetrieve.as_view(), name="retrieve"),
    re_path(r'^update/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', views.ContentHTMLUpdate.as_view(), name='update'),
    path('list/', views.ContentHTMLList.as_view(), name="list"),
    re_path(r'^delete/(?P<uuid>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})', views.ContentHTMLDelete.as_view(), name="delete"),
    path('images/add/', upload_views.ImagesAdd.as_view(), name='images_add'),
    re_path(r'^images/update/(?P<id>[-\d]+)/', upload_views.ImagesUpdate.as_view(), name='images_update'),
    path('images/list/', upload_views.ImagesList.as_view(), name='images_list'),
]