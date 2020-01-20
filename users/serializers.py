from rest_framework import serializers
from . import models

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """User serializer for api
    
    Arguments:
        serializers {Serializer} -- Base serializer
    """

    class Meta:
        model = models.CustomUser
        fields = ('pk', 'email', 'username', 'first_name', 'last_name', )


class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.CustomUser
        fields = ('first_name', 'last_name')