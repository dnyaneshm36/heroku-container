from django.conf.urls import url,include
from . import views
from .views import (
    UsersAPIView,
    whichuserlikespostofiduserAPIView,
    whichuserpostthatiduserlikeAPIView,
)


urlpatterns = [
    url(r'^$',  UsersAPIView.as_view() ),
    url(r'^whichuserlikespostofiduser$',  whichuserlikespostofiduserAPIView.as_view() ),
    url(r'^whichuserpostthatiduserlike$',  whichuserpostthatiduserlikeAPIView.as_view() ),
    url(r'^posts/', include('showuser.posts.urls')),
    url(r'^postslikes/', include('showuser.postlikes.urls')),
]