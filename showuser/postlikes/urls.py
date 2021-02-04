from django.conf.urls import url,include
from . import views
from .views import (
    PostlikesAPIView,
)


urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^$',  PostlikesAPIView.as_view() ),
]