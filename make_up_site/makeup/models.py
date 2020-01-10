from django.db import models

# Create your models here.

class Decorative(models.Model):
    product_type= models.CharField(max_length=200)
    product_info = models.CharField(max_length=2000)
    budget=models.IntegerField()
    lux=models.IntegerField()
    pic=models.ImageField(default='')

class Care(models.Model):
    product_type= models.CharField(max_length=200)
    product_info = models.CharField(max_length=2000)
    pic = models.ImageField(default='')

class Fav(models.Model):
    decorative = models.ForeignKey(Decorative, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




