from django.db import models
from django.utils import timezone

class Producto(models.Model):
	nombreProducto = models.CharField(max_length=60)
	precio = models.FloatField()



	def __str__(self):
		return self.title