from django.urls import path

from . import views

app_name = 'postapp'
urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('tags', views.tags_list, name='tags_list'),
    path('tag/create', views.TagCreate.as_view(),name='tag_create'),
    path('post/create', views.PostCreate.as_view(),name='post_create'),
    path('post/<str:slug>',views.PostDetail.as_view(),name='post_detail'),
    path('tag/<str:slug>', views.TagDetail.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update', views.TagUpdate.as_view(), name='tag_update'),
    path('post/<str:slug>/update',views.PostUpdate.as_view(),name='post_update'),
    path('tag/<str:slug>/delete', views.TagDelete.as_view(), name='tag_delete'),
    path('post/<str:slug>/delete', views.PostDelete.as_view(), name='post_delete'),

]