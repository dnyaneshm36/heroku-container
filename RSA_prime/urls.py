from django.conf.urls import url
from django.conf.urls import url
from .views import (
    hello,
    PrimeNO
)

urlpatterns = [
    url(r'^prime/$', PrimeNO.as_view() ),
]   