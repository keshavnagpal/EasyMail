from django.conf.urls import patterns,url
from msg import views

urlpatterns = [
  url('',url(r'^$',views.index,name="index"))
  ]
                       
