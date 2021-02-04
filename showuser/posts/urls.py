from django.conf.urls import url,include
from . import views
from .views import (
    PostAPIView,
)


urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^$',  PostAPIView.as_view() ),
]