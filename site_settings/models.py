from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.contrib.settings.models import BaseGenericSetting
from wagtail.contrib.settings.registry import register_setting


# Create your models here.
@register_setting
class SiteSettings(BaseGenericSetting):
    title = models.CharField(max_length=255)
    header_image = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL)
    panels = [
        FieldPanel('title'),
        FieldPanel('header_image'),
    ]