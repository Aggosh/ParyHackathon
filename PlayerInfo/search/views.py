from django.views.generic import ListView
from django.db.models import Q

import sys

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
            | Q(twitter_url__icontains=query)
            | Q(telegram_url__icontains=query)
        )
        return object_list
