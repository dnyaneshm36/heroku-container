
from rest_framework import serializers
from friend.models import Myfrienddetail

class MyfrienddetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myfrienddetail
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'phone_number',
            'nick_name',
            'date_of_birth',
            'email'
            ]
