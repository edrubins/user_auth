from django.conf.urls import url
from user_app import views

app_name ='user_app'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register/$', views.register , name='register'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]