from django.apps import AppConfig


class SeoConfig(AppConfig):
    name = "apps.seo"
    verbose_name = "سئو"

    def ready(self):
        from django.db.models.signals import post_save
        from .indexnow import ping

        def on_save(sender, instance, created=False, **kw):
            visible = getattr(instance, "is_published", getattr(instance, "is_active", True))
            if visible and not getattr(instance, "noindex", False) and hasattr(instance, "get_absolute_url"):
                try:
                    ping([instance.get_absolute_url()])
                except Exception:
                    pass

        for label in ("blog.Post", "products.Product", "academy.Course", "team.TeamMember", "core.Page"):
            try:
                post_save.connect(on_save, sender=label, dispatch_uid=f"indexnow-{label}", weak=False)
            except Exception:
                pass
