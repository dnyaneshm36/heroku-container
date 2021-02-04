
from rest_framework import serializers
from showuser.models import PostModel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = [
            'id',
            'user_id',
            'content',
            'total_likes',
            'total_comments',
        ]
    