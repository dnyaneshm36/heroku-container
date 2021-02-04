
from rest_framework import serializers
from status.models import Status
from accounts.api.serializers import  UserPublicSerializer




class StatusInlineSerializer(serializers.ModelSerializer):
    uri             =serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    def get_uri(self,obj):
        return "/status/{id}/".format(id=obj.id)








class StatusSerializer(serializers.ModelSerializer):
    uri             =serializers.SerializerMethodField(read_only=True)
    user            =UserPublicSerializer(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    def get_uri(self,obj):
        return "/status/{id}/".format(id=obj.id)
    def validate_content(self,value):
        if len(value) > 1000:
          raise serializers.ValidationError("This is  wayy too long.")  
        return value

    def validate(self,data):
        content = data.get("content",None)
        if content == "":
            content = None
            raise serializers.ValidationError("Content or image is require.")
        image = data.get("image", None)

        if content is None and image is None:
            raise serializers.ValidationError("Content or image is require.")
        return data