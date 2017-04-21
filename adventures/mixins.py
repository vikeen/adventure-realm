import logging

from django.views.generic.base import ContextMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from .models import Adventure


class AdventureMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context['adventure'] = Adventure.objects.get(pk=self.kwargs['adventure_pk'])
        return context


class HasAccessToAdventure(object):
    def get_redirect_url(self):
        return reverse('adventures:index')

    def dispatch(self, *args, **kwargs):
        adventure = Adventure.objects.get(pk=self.kwargs['adventure_pk'])

        if adventure.created_by == self.request.user:
            return super().dispatch(*args, **kwargs)
        else:
            logging.debug(
                'user: [%s] attempted to access restricted adventure, [%s]' % (
                    self.request.user.pk, adventure.pk))
            return redirect(self.get_redirect_url())
