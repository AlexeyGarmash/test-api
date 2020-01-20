from rest_framework import serializers
from . import models

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )

    class Meta:
        model = models.Product
        fields = ['pk', 'name', 'price', 'photo', 'comments']

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    author = serializers.HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='user-detail'
    )

    class Meta:
        model = models.Comment
        fields = ['pk', 'author', 'text', 'created_at']