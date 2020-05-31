from rest_framework import serializers
from .models import MyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
