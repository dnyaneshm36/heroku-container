
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token 
from rest_framework_jwt.views import refresh_jwt_token
from .view import AuthAPIView,RestigerAPIView
urlpatterns = [
    url(r'^$',AuthAPIView.as_view()),
    url(r'^register/$',RestigerAPIView.as_view()),
     url(r'^jwt/refresh/$',refresh_jwt_token),

    url(r'^jwt/$', obtain_jwt_token),
   
] 