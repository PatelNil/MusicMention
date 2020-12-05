from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    url(r'^$',views.index.as_view(),name='index'),
]

urlpatterns = format_suffix_patterns(urlpatterns)