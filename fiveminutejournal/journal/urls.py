from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entry/complete/', views.complete, name='complete'),
    url(r'^entry/(?P<journal_name>\w+)/$', views.entry, name='entry'),
    url(r'^archive/(?P<start_date>[\w.@+-]+)/$', views.archive, name='archive'),
    url(r'^goals/', views.goals, name='goals'),
    url(r'^events/', views.events, name='events'),
    url(r'^completed_goals/', views.completed_goals, name='completed_goals'),
]