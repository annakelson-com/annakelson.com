from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from core.blocks import SidebarContentBlock


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
