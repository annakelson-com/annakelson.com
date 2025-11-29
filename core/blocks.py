from wagtail.blocks import StructBlock, StreamBlock, RichTextBlock, CharBlock


class SidebarContentBlock(StructBlock):
    title = CharBlock()
    content = StreamBlock([
        ('rich_text', RichTextBlock()),
    ])

    class Meta:
        template = 'core/blocks/sidebar_content.html'
