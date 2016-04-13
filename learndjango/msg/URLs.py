from django.conf.urls import patterns,url
from msg import views

<<<<<<< HEAD
urlpatterns = patterns('',url(r'^$',views.index,name="index"))
=======
urlpatterns = [
  url('',url(r'^$',views.index,name="index"))
  ]
>>>>>>> origin/master
                       
