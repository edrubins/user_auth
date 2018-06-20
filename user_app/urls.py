from django.conf import settings
from django.conf.urls import url
from django.conf.urls import static
from user_app import views

app_name ='user_app'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'register/', views.register , name='register'),
    url(r'user_list/', views.user_list, name='user_list'),
]