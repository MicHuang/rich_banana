from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['phone', 'first_name', 'last_name', 'date_of_birth', 'email', 'address', 'points', 'date_joined']
