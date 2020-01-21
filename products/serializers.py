from rest_framework import serializers
from . import models

from users.serializers import UserSerializer


class ProductSerializer(serializers.ModelSerializer):

    #comments = CommentSerializer(
    #    many=True,
    #    read_only=True,
    #    #view_name='comment-detail'
    #)

    class Meta:
        model = models.Product
        fields = ['pk', 'name', 'price', 'photo']

class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(
        many=False,
        read_only=True,
        #view_name='user-detail'
    )

    product = ProductSerializer(
        many=False,
        read_only=True,
        #view_name='user-detail'
    )

    class Meta:
        model = models.Comment
        fields = ['pk', 'product', 'author', 'text', 'created_at']




