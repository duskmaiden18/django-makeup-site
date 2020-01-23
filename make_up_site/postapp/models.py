from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150,unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse('postapp:post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('postapp:post_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('postapp:post_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_pub']

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postapp:tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('postapp:tag_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('postapp:tag_delete', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['title']

class Comment(models.Model):
    text = models.CharField(max_length=200)
    date_pub = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,default=5)

    class Meta:
        ordering = ['-date_pub']



