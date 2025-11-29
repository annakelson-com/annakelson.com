from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import StreamField
from wagtail.models import Page


# Create your models here.


class StandardPage(Page):
    body = StreamField(
        [
            ('rich_text', RichTextBlock()),
            ('embed', EmbedBlock()),
        ],
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

