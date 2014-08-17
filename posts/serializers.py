from rest_framework import serializers
from models import Post, TestModel
from django.contrib.auth.models import User
from django.utils import timezone

class PostSerializer(serializers.ModelSerializer):
	owner = serializers.Field(source='owner.username')
	publish_date = serializers.DateTimeField(default=timezone.now())
	class Meta:
		model = Post
        fields = ('id', 'title', 'message', 'publish_date', 'owner')

class UserSerializer(serializers.ModelSerializer):
	posts = serializers.PrimaryKeyRelatedField(many=True)
	profile = serializers.PrimaryKeyRelatedField()

	class Meta:
		model = User
        fields = ('id', 'post_set', 'username', 'profile', 'first_name', 'last_name')

class TestModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = TestModel
        fields = ('msg',)
        