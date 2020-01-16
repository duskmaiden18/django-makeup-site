from django.urls import path

from . import views

app_name = 'postapp'
urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('tags', views.tags_list, name='tags_list'),
    path('<str:slug>',views.post_detail,name='post_detail'),
]