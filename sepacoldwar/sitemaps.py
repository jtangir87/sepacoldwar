from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from pages.models import Event


class StaticViewSitemap(Sitemap):
    def items(self):
        return [
            "home",
            "about_us",
            "contact_us",
            "volunteer",
            "merchandise",
            "links",
            "donate",
            "hiob_events",
            "movie_events",
            "avt_events",
            "other_events",
            "oral_histories",
            "dfs",
            "nadc",
            "nadc_15th_reunion",
            "nadc_20th_reunion",
        ]

    def location(self, item):
        return reverse(item)


class EventSitemap(Sitemap):
    def items(self):
        return Event.objects.all()