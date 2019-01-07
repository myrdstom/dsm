from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product
from django.urls import reverse
from .serializers import ProductSerializer
from django.conf import settings
import json


class Base(TestCase):
    """This class defines the testsuite for my Product model."""

    def setUp(self):
        self.client = APIClient()
        # serialized = ProductSerializer
        self.productData = {'productName':'vivan','unitPrice':1200000,'quantity':54}
        self.response = self.client.post(
            reverse('create'),
            self.productData,
            format="json"
        )

    """Test create a product."""
    def test_api_can_create_a_product(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        # self.assertIn(self.response.content, self.productData)



    # """Test get a single item."""
    # def test_get_a_product(self):
    #     product = Product.objects.get()
    #     response = self.client.get(
    #         reverse('details',
    #         kwargs={'pk':1}
    #
    #         ), format="json"
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #
    #     self.assertContains(response, product)

    """Test get an item that doesn't exist."""
    def test_get_a_product_that_does_not_exist(self):
        product = Product.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk':300}

            ), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(response.content, b'{"detail":"Not found."}')


    """Edit the products table."""
    def test_update_a_product(self):
        product = Product.objects.get()
        newProduct = {'productName':'lenovo','unitPrice':22000000,'quantity':32}
        response = self.client.put(
            reverse('details',
            kwargs={'pk':product.id}

            ), newProduct, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """Test delete a product."""
    def test_delete_a_product(self):
        product = Product.objects.get()
        res = self.client.delete(
            reverse('details', kwargs={'pk':product.id}),
            format='json',
            follow=True
        )
        self.assertEquals(res.status_code, status.HTTP_204_NO_CONTENT)