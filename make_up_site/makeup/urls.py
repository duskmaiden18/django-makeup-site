from django.urls import path

from . import views

app_name = 'makeup'
urlpatterns = [
    path('', views.index, name='index'),
    path('types/', views.types, name='types'),
    path('types/decor', views.DecorView.as_view(), name='decor'),
    path('types/care', views.CareView.as_view(), name='care'),
    path('polls', views.polls, name='polls'),
    path('decorpolls',views.DecorPollsView.as_view(), name='decor_polls'),
    path('db_change',views.dbchange,name='dbchange'),
    path('carepolls',views.CarePollsView.as_view(), name='care_polls')
]