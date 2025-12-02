from willow.registry import registry
from willow.plugins.pillow import PillowImage
from PIL import ImageDraw, ImageFont

from wagtail.images.image_operations import FilterOperation
from wagtail import hooks

from site_settings.models import SiteSettings


WATERMARK_TEXT = 'Anna Kelson\nFine Art'
MARGIN = 10


def pillow_watermark(image):
    watermark_text = SiteSettings.load().watermark_text.replace('\r', '')
    pil_image = image.image
    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.load_default(size=40)  # .truetype(settings.STATIC_ROOT + "fontsarial.ttf", 16)
    text_color = (255, 255, 255)
    # text_width, text_height = (200, 100) # draw.text(WATERMARK_TEXT, font)
    # image_width, image_height = pil_image.size
    position = (50, 40)
    draw.text(position, watermark_text, font=font, fill=text_color, opacity=0.5)
    return PillowImage(pil_image)


class WatermarkOperation(FilterOperation):
    def construct(self, *args):
        pass

    def run(self, willow, image, env):
        return willow.watermark()


@hooks.register('register_image_operations')
def register_watermark():
    return [
        ('watermark', WatermarkOperation),
    ]


registry.register_operation(PillowImage, 'watermark', pillow_watermark)
