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
    url(r'^deleted_goals/', views.deleted_goals, name='deleted_goals'),
    url(r'^edit_entry/(?P<response_id>[0-9]+)/$', views.edit_entry, name='edit_entry'),
    url(r'^settings/', views.journal_settings, name='journal_settings'),
    url(r'^edit_journal/(?P<journal_id>[\w]+)/$', views.edit_journal, name='edit_journal'),
]
