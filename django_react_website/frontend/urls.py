from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'Frontend'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
]
