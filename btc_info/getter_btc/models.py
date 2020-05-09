from django.db import models


class Btc(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['-id']
