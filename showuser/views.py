import json
from rest_framework import generics,mixins
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from django.shortcuts import get_object_or_404 
from rest_framework.generics import ListAPIView
#local file
from showuser.models import PostModel

from showuser.models import PostlikesModel

from .serializers import UserSerializer

from django.contrib.auth.models import User

from django.shortcuts import render

# Create your views here.








def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


class UsersAPIView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.ListAPIView): 

    serializer_class = UserSerializer
    permission_classes        =[]
    authentication_classes    =[]
    passed_id                 =None
    def get_queryset(self):
        request = self.request
        qs = User.objects.all()
        query = self.request.GET.get('ur',None) 
        # print(query,'-----query--')
        # print(self.passed_id,"inget")
        if query == 'whichuserslikepost':

            postids = PostModel.objects.filter(user_id__exact=self.passed_id).values_list('id', flat=True)
            

            users_ids = PostlikesModel.objects.filter(post_id__in=list(postids)).values_list('user_id', flat=True)

            # print(postids,"p___ost")
            # print(users_ids,"use___rs")
                
            qs = qs.filter(id__in=list(users_ids))
            
            self.passed_id = None
            print(self.passed_id,"the ")
        elif query is not None:
            qs = qs.filter(id__exact = query)
        print(qs,"qeers__ses")
        return qs

    def get_object(self):
        request         =self.request
        passed_id       =request.GET.get('id',None) or self.passed_id

        #print(request.body)
        print(passed_id,"uameing")
        # print(request.data)     
        queryset        =self.get_queryset()
        obj = None
        print(passed_id,"afteruerwurt")
        if passed_id is not None:
            obj = get_object_or_404(queryset, id = passed_id)
            self.check_object_permissions(request,obj)
        print(obj)
        return obj  

    def get(self,request,*args,**kwargs):
        print("----assdf------")
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            #print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        if passed_id is not None:
            return self.retrieve(request, *args,**kwargs)
        return super(UsersAPIView,self).get(request,*args,**kwargs)





    def put(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            #print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return self.update(request,*args,**kwargs)


    def patch(self,request,*args,**kwargs):
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id        
        return self.partial_update(request,*args,**kwargs)








class whichuserlikespostofiduserAPIView(
    generics.ListAPIView): 

    serializer_class = UserSerializer
    permission_classes        =[]
    authentication_classes    =[]
    passed_id                 =None
    def get_queryset(self):
        request = self.request
        qs = User.objects.all()
        #query = self.request.GET.get('ur',None) 
        # print(query,'-----query--')
        # print(self.passed_id,"inget")    
        postids = PostModel.objects.filter(user_id__exact=self.passed_id).values_list('id', flat=True)
            

        users_ids = PostlikesModel.objects.filter(post_id__in=list(postids)).values_list('user_id', flat=True)

            # print(postids,"p___ost")
            # print(users_ids,"use___rs")
    
        qs = qs.filter(id__in=list(users_ids))
            
        # self.passed_id = None
        # print(self.passed_id,"the ")

        # if query is not None:
        #     qs = qs.filter(id__exact = query)
        # print(qs,"qeers__ses")
        return qs


    def get(self,request,*args,**kwargs):
        #print("----assdf------")
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            #print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        # if passed_id is not None:
        #     return self.retrieve(request, *args,**kwargs)
        return super().get(request,*args,**kwargs)








class whichuserpostthatiduserlikeAPIView(
    generics.ListAPIView): 

    serializer_class = UserSerializer
    permission_classes        =[]
    authentication_classes    =[]
    passed_id                 =None
    def get_queryset(self):
        request = self.request
        qs = User.objects.all()
        #query = self.request.GET.get('ur',None) 
        # print(query,'-----query--')
        # print(self.passed_id,"inget")    
        postids = PostlikesModel.objects.filter(user_id__exact=self.passed_id).values_list('post_id', flat=True)
        print(postids,"p___ost")    

        users_ids = PostModel.objects.filter(id__in=list(postids)).values_list('user_id', flat=True)

        
        print(users_ids,"use___rs")
    
        qs = qs.filter(id__in=list(users_ids))
            
        # self.passed_id = None
        # print(self.passed_id,"the ")

        # if query is not None:
        #     qs = qs.filter(id__exact = query)
        # print(qs,"qeers__ses")
        return qs


    def get(self,request,*args,**kwargs):
        #print("----assdf------")
        url_passed_id           = request.GET.get('id',None)
        json_data               ={}
        body_                   =request.body
        if is_json(body_):
            json_data               =json.loads(request.body)
            #print(json_data,"jata")
        new_passed_id           =json_data.get('id',None)
        passed_id     = url_passed_id or new_passed_id or None
        self.passed_id = passed_id
        # if passed_id is not None:
        #     return self.retrieve(request, *args,**kwargs)
        return super().get(request,*args,**kwargs)
