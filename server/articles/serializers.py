from rest_framework import serializer
from django.conf import settings
from .models import Article

class ArticleListSerializer(serializer.ModelSerializer):
    like_user = serializers.PrimaryKeyRelatedField(queryset=settings.AUTH_USER_MODEL, many=True,read_only=True)
    like_user_count = serializers.IntegerField(source="like_user.count",read_only=True)
    class Meta:
        model = Article
        fields = ('id','title','like_user','color1','color2','color3','color4','color5','created_at','like_user_count')


class ArticleSerializer(serializer.ModelSerializer):
    like_user = serializers.PrimaryKeyRelatedField(queryset=settings.AUTH_USER_MODEL, many=True,read_only=True)
    class Meta:
        model = Article
        fields = ('id','title','like_user','color1','color2','color3','color4','color5','created_at')

