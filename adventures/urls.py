from django.conf.urls import url

from . import views

app_name = 'adventures'
urlpatterns = [
    url(r'^$', views.AdventureIndex.as_view(), name='index'),
    url(r'^create$', views.AdventureCreate.as_view(), name='create'),
    url(r'^(?P<adventure_id>[0-9]+)/update$', views.AdventureUpdate.as_view(), name='update'),

    # summary sentence
    url(r'^create$', views.SummarySentenceCreate.as_view(), name='create'),
]
