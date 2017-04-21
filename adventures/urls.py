from django.conf.urls import url

from . import views

app_name = 'adventures'
urlpatterns = [
    url(r'^$', views.AdventureIndex.as_view(), name='index'),
    url(r'^create$', views.AdventureCreate.as_view(), name='create'),
    url(r'^(?P<adventure_pk>[0-9]+)/update$', views.AdventureUpdate.as_view(), name='update'),

    # summary sentence
    url(r'^(?P<adventure_pk>[0-9]+)/summary-sentence/create', views.SummarySentenceCreate.as_view(),
        name='summary_sentence_create'),
    url(r'^(?P<adventure_pk>[0-9]+)/summary-sentence/(?P<summary_sentence_pk>[0-9]+)/update',
        views.SummarySentenceUpdate.as_view(),
        name='summary_sentence_update'),

    # summary paragraph
    url(r'^(?P<adventure_pk>[0-9]+)/summary-paragraph/create', views.SummaryParagraphCreate.as_view(),
        name='summary_paragraph_create'),
    url(r'^(?P<adventure_pk>[0-9]+)/summary-paragraph/(?P<summary_paragraph_pk>[0-9]+)/update',
        views.SummaryParagraphUpdate.as_view(),
        name='summary_paragraph_update'),

    # summary paragraph
    url(r'^(?P<adventure_pk>[0-9]+)/character-outline/create', views.CharacterOutlineCreate.as_view(),
        name='character_outline_create'),
    url(r'^(?P<adventure_pk>[0-9]+)/character-outline/(?P<character_outline_pk>[0-9]+)/update',
        views.CharacterOutlineUpdate.as_view(),
        name='character_outline_update'),
]
