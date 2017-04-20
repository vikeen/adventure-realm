# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Adventure


class Index(generic.ListView):
    model = Adventure
    context_object_name = 'adventure_list'


class Create(generic.CreateView):
    model = Adventure
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)