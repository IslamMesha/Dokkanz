# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
