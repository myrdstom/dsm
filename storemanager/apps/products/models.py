from django.db import models

class Product(models.Model):
    productName = models.CharField(max_length=255, blank=False, unique=True)
    unitPrice = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.productName)
