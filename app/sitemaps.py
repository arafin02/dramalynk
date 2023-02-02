from django.contrib.sitemaps import Sitemap

from .models import *


class DramaSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
    protocol = "https"

    def items(self):
        return Drama.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
