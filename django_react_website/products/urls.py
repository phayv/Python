from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'Products'

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name="index"),
    re_path(r'^(?P<pk>\d+)/$', views.ProductDetailView.as_view(), name='product-detail'),
    re_path(r'^api/(?P<pk>[0-9]+)/$', views.ProductAPIDetailView.as_view(), name='product-api-detail'),
    re_path(r'^api/products/$', views.ProductListView.as_view(), name='product-api-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
