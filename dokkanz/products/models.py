# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
