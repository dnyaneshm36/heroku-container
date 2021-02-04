
from django.conf.urls import url,include
from django.contrib import admin

from .view import UserDetailAPIView
urlpatterns = [
    url(r'^(?P<username>\w+)/$',UserDetailAPIView.as_view(),name = "detail"),

   
] 