from django.db import models

# Create your models here.

class Decorative(models.Model):
    product_type= models.CharField(max_length=200)
    product_info = models.CharField(max_length=2000)
    budget=models.IntegerField()
    lux=models.IntegerField()
    pic=models.ImageField(default='')

    def __str__(self):
        return self.product_type


class Care(models.Model):
    product_type= models.CharField(max_length=200)
    product_info = models.CharField(max_length=2000)
    pic = models.ImageField(default='')
    companies=models.ManyToManyField('FavCare',blank=True,related_name="+")

    def __str__(self):
        return self.product_type

class Fav(models.Model):
    decorative = models.ForeignKey(Decorative, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class FavCare(models.Model):
    name=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)






