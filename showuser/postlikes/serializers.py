
from rest_framework import serializers
from showuser.models import PostlikesModel

class PostlikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostlikesModel
        fields = [
            'id',
            'user_id',
            'post_id',
            'updated_at',
            'created_at',
        ]
    