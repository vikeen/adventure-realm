from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^(?P<username>[\w]+)/$', views.Detail.as_view(), name='detail')
]
