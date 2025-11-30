from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from core.blocks import SidebarContentBlock

from gallery.models import ArtPage


class HomePage(Page):
    sidebar = StreamField(
        [
            ("sidebar_content", SidebarContentBlock())
        ],
        null=True,
        blank=True,
    )
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('sidebar'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['art_pages'] = ArtPage.objects.live().order_by('-first_published_at')[:6]
        return context
