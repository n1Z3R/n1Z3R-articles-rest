from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from articlesapp.models import *


class ArticlesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = ArticlesModel
        fields = "__all__"

    def get_likes(self, instance):
        '''This func gets names of users who liked current article'''
        return [i.user.username for i in ArticlesLikesModel.objects.filter(article=instance)]

    def get_comments(self, instance):
        '''This func gets names of users who comment current article and content of comment'''
        return [{"username": i.user.username, "content": i.content, "time_create": i.time_create} for i in
                ArticlesCommentsModel.objects.filter(article=instance)]


class ArticlesCommentsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ArticlesCommentsModel
        fields = "__all__"


class ArticlesLikesSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ArticlesLikesModel
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
