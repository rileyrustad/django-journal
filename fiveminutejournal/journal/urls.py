from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^morning/', views.morning, name='morning'),
    url(r'^evening/', views.evening, name='evening'),
]