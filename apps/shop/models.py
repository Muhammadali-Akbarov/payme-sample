from django.db import models


class CustomOrderModel(models.Model):
    amount = models.IntegerField(default=0)
