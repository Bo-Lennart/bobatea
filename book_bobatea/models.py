from django.db import models

# Create your models here.


class TeaMenu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.IntegerField()


    def __str__(self):
        return self.name