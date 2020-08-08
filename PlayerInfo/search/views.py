from django.views.generic import ListView
from django.db.models import Q

import sys

from .mainparser import create_new_profile

sys.path.append("..")  # Adds higher directory to python modules path.
from Profile.models import Profile


class SearchResultsView(ListView):
    model = Profile
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Profile.objects.filter(
            Q(nickname__icontains=query)
            | Q(steam_url__icontains=query)
            | Q(wow_url__icontains=query)
            | Q(twitter__icontains=query)
            | Q(telegram_url__icontains=query)
        )
        if len(object_list) == 0:
            create_new_profile(query)
            return self.get_queryset()

        return object_list
