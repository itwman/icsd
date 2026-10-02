from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from apps.core.models import SiteSettings
from .models import Post


class LatestPostsFeed(Feed):
    feed_type = Rss201rev2Feed

    def title(self):
        return f"مقالات {SiteSettings.load().site_name}"

    def link(self):
        return "/blog/"

    def description(self):
        return SiteSettings.load().default_meta_description or "آخرین مقالات"

    def items(self):
        return Post.objects.filter(is_published=True, noindex=False).select_related("category")[:30]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.meta_description or item.excerpt

    def item_pubdate(self, item):
        return item.published_at

    def item_updateddate(self, item):
        return item.updated_at

    def item_categories(self, item):
        return [item.category.title] + [t.name for t in item.tags.all()]
