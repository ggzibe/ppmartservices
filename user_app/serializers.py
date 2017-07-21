from rest_framework import serializers
from mongoengine.django.auth import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
