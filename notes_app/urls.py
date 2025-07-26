
from . import views
from django.urls import re_path as url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'note_app'
urlpatterns = [
    url(r'^$', views.all_notes, name='all_notes'),
    url(r'^(?P<slug>[-\w]+)$', views.detail_note, name='detail_notes'),
    url(r'^note/add$', views.add_note, name='add_note'),
    url(r'^(?P<slug>[-\w]+)/edit$', views.edit, name='note_edit'),
    url(r'^ckeditor$', include('ckeditor_uploader.urls')),
    url(r'^logout/$', views.logout_view, name='logout'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)