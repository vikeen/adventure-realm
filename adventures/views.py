# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic

from .models import Adventure, SummaryParagraph, SummarySentence, CharacterOutline
from .mixins import AdventureMixin, HasAccessToAdventure


class AdventureIndex(generic.ListView):
    model = Adventure
    context_object_name = 'adventure_list'


class AdventureCreate(generic.CreateView):
    model = Adventure
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Adventure created')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.object.pk
        })


class AdventureUpdate(HasAccessToAdventure,
                      generic.UpdateView):
    model = Adventure
    fields = ['name']

    def get_object(self, queryset=None):
        return Adventure.objects.get(pk=self.kwargs['adventure_pk'])

    def get_success_url(self):
        messages.success(self.request, 'Adventure updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class SummarySentenceCreate(HasAccessToAdventure,
                            AdventureMixin,
                            generic.CreateView):
    model = SummarySentence
    fields = ['text']

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'One Sentence Summary updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class SummarySentenceUpdate(HasAccessToAdventure,
                            AdventureMixin,
                            generic.UpdateView):
    model = SummarySentence
    fields = ['text']

    def get_object(self, queryset=None):
        return SummarySentence.objects.get(pk=self.kwargs['summary_sentence_pk'])

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'One Sentence Summary updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class SummaryParagraphCreate(HasAccessToAdventure,
                             AdventureMixin,
                             generic.CreateView):
    model = SummaryParagraph
    fields = ['text']

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'One Paragraph Summary updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class SummaryParagraphUpdate(HasAccessToAdventure,
                             AdventureMixin,
                             generic.UpdateView):
    model = SummaryParagraph
    fields = ['text']

    def get_object(self, queryset=None):
        return SummaryParagraph.objects.get(pk=self.kwargs['summary_paragraph_pk'])

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'One Paragraph Summary updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class CharacterOutlineCreate(HasAccessToAdventure,
                             AdventureMixin,
                             generic.CreateView):
    model = CharacterOutline
    fields = ['name', 'image_url', 'description', 'background', 'personality', 'motive', 'conflict']

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Character Outline created')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })


class CharacterOutlineUpdate(HasAccessToAdventure,
                             AdventureMixin,
                             generic.UpdateView):
    model = CharacterOutline
    fields = ['name', 'image_url', 'description', 'background', 'personality', 'motive', 'conflict']

    def get_object(self, queryset=None):
        return CharacterOutline.objects.get(pk=self.kwargs['character_outline_pk'])

    def form_valid(self, form):
        form.instance.adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Character Outline updated')
        return reverse('adventures:update', kwargs={
            'adventure_pk': self.kwargs['adventure_pk']
        })
