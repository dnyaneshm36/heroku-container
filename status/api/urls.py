from django.conf.urls import url


from .views import (
    StatusAPIView,
    StatusAPIDetailView,
    #StatusCreateAPIView,
    #StatusDetailAPIView,
    #StatusUpdateAPIView,
    #StatusDeleteAPIView,
    #StatusListSearchAPIView,
)


urlpatterns =[
    url(r'^$',  StatusAPIView.as_view() ),
    url(r'^(?P<id>\d+)/$',  StatusAPIDetailView.as_view() ),
    #url(r'^create/$', StatusCreateAPIView.as_view() ),
    #url(r'^(?P<pk>\d+)/$',StatusDetailAPIView.as_view() ),
    #url(r'^(?P<pk>\d+)/update$',StatusUpdateAPIView.as_view() ),
    #url(r'^(?P<pk>\d+)/delete$',StatusDeleteAPIView.as_view() ), 
]


'''
/api/status/   ->List
/api/status/create ->Create
/api/status/12/ ->detail
/api/status/12/update -> Update
/api/status/12/delete ->    Delete


'''


'''
leter 
/api/status/ ->List -crud
/api/status/1/    -> Detail ->crud

'''

"""
/api.status ->crud & ls
"""