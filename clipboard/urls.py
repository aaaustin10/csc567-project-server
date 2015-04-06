from django.conf.urls import url, patterns
from clipboard import views

urlpatterns = patterns('',
    url(r'^clipboard$', views.ClipboardView.as_view(), name='get_clipboard'),
)
