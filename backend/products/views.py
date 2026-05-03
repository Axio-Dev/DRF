from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreatAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

# class ProductListAPIView(generics.ListAPIView):
#     """
#     Not gonna use this method
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            # detail view
            qs = Product.objects.filter(pk=pk)
            obj = get_object_or_404(Product, pk=pk) # This func will raise a 404 if the obj does not exists
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        qs = Product.objects.all() # we can use 'queryset' as variable or just 'qs'
        data = ProductSerializer(qs, many=True).data
        return Response(data)

    if method == "POST":
        # Create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
