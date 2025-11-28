from django.db import models
from wagtail.models import Page


# Create your models here.


class GalleryPage(Page):
    parent_page_types = ['home.HomePage']
    subpage_types = ['gallery.ArtPage']


class ArtPage(Page):
    parent_page_types = ['gallery.GalleryPage']
