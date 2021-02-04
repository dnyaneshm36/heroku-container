from django.shortcuts import render
import json
from django.http import HttpResponse
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from RSA_prime.prime_number import get_reqquired_prime_no

def hello(request):

    bit=request.GET.get('bits',1024)
    bit=int(bit)
    temp = get_reqquired_prime_no(bit)
    data = {
        'bits' : bit,
        'prime_number': temp
    }
    data = json.dumps(data)
    return HttpResponse(data, content_type="application/json")


class PrimeNO(APIView):
   
    def get(self, request, format=None):
        bit=request.GET.get('bits',1024)
        bit=int(bit)
        temp = get_reqquired_prime_no(bit)
        data = {
            'bits' : bit,
            'prime_number': temp
        }
        return Response(data)