from wagtail.blocks import StructBlock, PageChooserBlock, BooleanBlock, IntegerBlock, CharBlock


class GalleryBlock(StructBlock):
    page = PageChooserBlock(
        help_text="Choose a page whose children should be displayed in this gallery"
    )
    # smaller_thumbnails = BooleanBlock(
    #     help_text="Use smaller thumbnails",
    #     default="False",
    # )

    class Meta:
        template = 'gallery/gallery_block.html'