from django.contrib.auth.models import User
from django.views import generic

from .mixins import ProfileMixin, HasAccessToRestrictedUserProfile


class Detail(ProfileMixin, generic.DetailView):
    model = User
    template_name = 'users/user_detail_overview.html'
    context_object_name = 'view_user'

    def get_object(self, queryset=None):
        return User.objects.get(username=self.kwargs['username'])