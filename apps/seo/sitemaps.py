from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.academy.models import Course
from apps.blog.models import Post
from apps.core.models import Page
from apps.products.models import Product


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return ["core:home", "academy:course_list", "products:list", "blog:post_list", "leads:start", "core:customers"]

    def location(self, item):
        return reverse(item)


class CourseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Course.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class PostSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return Post.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


class PageSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.4

    def items(self):
        return Page.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at


SITEMAPS = {"static": StaticSitemap, "courses": CourseSitemap, "products": ProductSitemap,
            "posts": PostSitemap, "pages": PageSitemap}
