from django.db.models import ForeignKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from core.blocks import SidebarContentBlock

from gallery.models import ArtPage

from django.db import models

class HomePage(Page):
    sidebar = StreamField(
        [
            ("sidebar_content", SidebarContentBlock())
        ],
        null=True,
        blank=True,
    )
    featured_gallery = ForeignKey(
        'core.StandardPage',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )

    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('sidebar'),
        FieldPanel('featured_gallery'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        if self.featured_gallery:
            context['art_pages'] = [page for page in self.featured_gallery.get_children().all() if page.specific.is_art_page][:6]
                                       #ArtPage.objects.live().order_by('-first_published_at'))[:6]
        return context
