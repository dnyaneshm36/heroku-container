from django.conf.urls import url,include
from . import views
from .views import (
    FriendAPIView,
)


urlpatterns = [
    url(r'^RSA_prime_no_1024bits', views.hello, name='hello'),
    url(r'^$',  FriendAPIView.as_view() ),
]