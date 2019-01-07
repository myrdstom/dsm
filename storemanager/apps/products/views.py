from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
# Create your views here.

class CreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """Saving the post data to the products table."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
