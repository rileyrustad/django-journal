from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^entry/(?P<entry_type>\w+)/$', views.entry, name='entry'),
    url(r'^goals/', views.goals, name='goals'),
    url(r'^events/', views.events, name='events'),
]