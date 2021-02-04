from rest_framework import permissions,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework_jwt.settings import api_settings

from .utils import jwt_response_payload_handler
from .permissions import AnonPermissionOnly
from .serializers import UserRegisterSerilalizer
from .user.serializer import UserDetailSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


User = get_user_model()





class AuthAPIView(APIView):

    permission_classes          =[permissions.AllowAny]
    def post(self, request, *args, ** kwargs):


        if request.user.is_authenticated:  
            return Response({'detail': 'you are already authenticated'},status=400)
        data = request.data 
        username = data.get('username')
        password = data.get('password')
        # if email is send thought the username field
        # user = authenticate(username=username,password=password)
        qs = User.objects.filter(
            Q(username__iexact = username)|
            Q(email__iexact= username)
        ).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                user = user_obj
                payload = jwt_payload_handler(user) 
                token = jwt_encode_handler(payload)
                response = jwt_response_payload_handler(token,user,request=request)
                return Response(response)
        return Response( {'detail' : 'Invalid cratedtiotal' },status=401)


class RestigerAPIView(generics.CreateAPIView):
    queryset                   =User.objects.all()
    serializer_class           =UserRegisterSerilalizer
    permission_classes         =[AnonPermissionOnly]

    def get_serializer_context(self, *args,**kwargs):
        return {'request' : self.request}


# class RestigerAPIView(APIView):

#     permission_classes          =[permissions.AllowAny]
#     def post(self, request, *args, ** kwargs):


#         if request.user.is_authenticated:  
#             return Response({'detail': 'you are already authenticated'},status=400)
#         data = request.data 
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#         # if email is send thought the username field
#         # user = authenticate(username=username,password=password)
#         qs = User.objects.filter(
#             Q(username__iexact = username)|
#             Q(email__iexact= username)
#         ).distinct()

#         if password != password2:
#             return Response( {'detail' : 'passward should match' },status=401)

#         if qs.exists():
#             return Response( {'detail' : 'this user aleardy exists' },status=401)
#         else: 
#             user = User.objects.create(username= username ,email =email)
#             user.set_password(password)
#             user.save()
#             payload = jwt_payload_handler(user) 
#             token = jwt_encode_handler(payload)
#             response = jwt_response_payload_handler(token,user,request=request)
#             return Response(response)         
#         return Response( {'detail' : 'Invalid requests' },status=401)