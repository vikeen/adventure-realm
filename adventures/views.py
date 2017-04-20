# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import generic

from .models import Adventure, SummaryParagraph, SummarySentence


class AdventureIndex(generic.ListView):
    model = Adventure
    context_object_name = 'adventure_list'


class AdventureCreate(generic.CreateView):
    model = Adventure
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AdventureUpdate(generic.UpdateView):
    model = Adventure
    fields = ['name']

    def get_object(self, queryset=None):
        return Adventure.objects.get(pk=self.kwargs['adventure_id'])

    def get_success_url(self):
        messages.success(self.request, 'Adventure updated')
        return reverse('adventures:update', kwargs={
            'adventure_id': self.kwargs['adventure_id']
        })


class SummarySentenceCreate(generic.CreateView):
    model = SummarySentence
    fields = ['description']

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super().form_valid(form)
