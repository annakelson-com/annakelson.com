from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock, StructBlock, CharBlock, FloatBlock
from wagtail.fields import StreamField
from wagtail.models import Page


# Create your models here.


class ArtPage(Page):
    description = StreamField(
        [
            ('rich_text', RichTextBlock()),
        ],
        null=True,
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    medium = models.CharField(max_length=120, null=True)
    dimensions = models.CharField(max_length=120, null=True)
    prints_available = models.BooleanField(default=False)
    print_prices = StreamField(
        [
            (
                'price_tier', StructBlock([
                ('dimensions', CharBlock()),
                ('prices', FloatBlock()),
            ])
            )
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('description'),
        FieldPanel('medium'),
        FieldPanel('dimensions'),
        FieldPanel('prints_available'),
        FieldPanel('print_prices'),
    ]