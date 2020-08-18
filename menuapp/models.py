from django.db import models


class VegIndian(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    def __str__(self):
        return self.name
class NonvegIndian(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    def __str__(self):
        return self.name

class VegChinese(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    def __str__(self):
        return self.name

class NonvegChinese(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    def __str__(self):
        return self.name


# Create your models here.
