from django.conf.urls import url

from . import views

app_name = 'adventures'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^create$', views.Create.as_view(), name='create'),
]
