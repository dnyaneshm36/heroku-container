
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime

from status.api.serializers import StatusInlineSerializer

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    uri                  =serializers.SerializerMethodField(read_only=True)
    status_list          =serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'uri',
            'status_list',
        ]
    def get_uri(self,obj):
        return "/api/user/{id}/".format(id=obj.id)

    def get_status_list(self,obj):
        qs= obj.status_set.all().order_by("-timestamp")[:10]          #Status.objects.filter(user= obj)
        return StatusInlineSerializer(qs, many= True).data