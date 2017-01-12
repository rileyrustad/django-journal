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
    url(r'^edit_journal_name/(?P<journal_id>[\w]+)/$', views.edit_journal_name, name='edit_journal_name'),
    url(r'^edit_goal_cat/(?P<goal_cat_id>[\w]+)/$', views.edit_goal_category, name='edit_goal_cat'),
    url(r'^goal_categories/$', views.goal_categories, name='goal_categories'),
    url(r'^delete_journal/(?P<journal_id>[0-9]+)/$', views.delete_journal, name='delete_journal'),
    url(r'^delete_response/(?P<response_id>[0-9]+)/$', views.delete_response, name='delete_response'),
    url(r'^delete_goal/(?P<goal_id>[0-9]+)/$', views.delete_goal, name='delete_goal'),
    url(r'^delete_event/(?P<event_id>[0-9]+)/$', views.delete_event, name='delete_event'),
    url(r'^delete_goal_cat/(?P<goal_cat_id>[0-9]+)/$', views.delete_goal_category, name='delete_goal_category'),
    url(r'^journal_defaults/', views.journal_defaults, name='journal_defaults'),
    url(r'^goal_defaults/', views.goal_defaults, name='goal_defaults'),
    url(r'^event_defaults/', views.event_defaults, name='event_defaults'),

]
