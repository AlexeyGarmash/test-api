from rest_framework import generics

from . import models, serializers
# Create your views here.

class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = ProductListView.queryset
    serializer_class = ProductListView.serializer_class

class CommentDeatailView(generics.RetrieveAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer