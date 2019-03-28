from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^create$', views.create),
    url(r'^newjobs$', views.newjobs),
    url(r'^view/(?P<num>\d+)$', views.view_job),
    url(r'delete/(?P<num>\d+)$', views.delete_job),
    url(r'^edit/(?P<num>\d+)$', views.edit_job),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'assign/(?P<num>\d+)$', views.assign_job),
]