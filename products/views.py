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

class CommentsProductListView(generics.ListAPIView):

    serializer_class = serializers.CommentSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        pk = self.kwargs['pk']
        return models.Comment.objects.filter(product__pk=pk)