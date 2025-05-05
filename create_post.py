# create_post.py

from PIL import Image, ImageDraw, ImageFont
import os
import datetime
import textwrap

def create_fact_image(tip_data):
    WIDTH, HEIGHT = 1080, 1350
    BG_COLOR = "#fef9f4"
    BOX_COLOR = "#ffffff"
    TITLE_COLOR = "#2b9348"
    POINT_COLOR = "#333333"
    FOOTER_COLOR = "#888888"

    FONT_PATH_BOLD = "templates/OpenSans-Bold.ttf"
    FONT_PATH_REGULAR = "templates/PlayfairDisplay-VariableFont_wght.ttf"

    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts with fallback
    def safe_font(path, size):
        try:
            return ImageFont.truetype(path, size)
        except:
            return ImageFont.load_default()

    title_font = safe_font(FONT_PATH_BOLD, 64)
    point_font = safe_font(FONT_PATH_REGULAR, 44)
    footer_font = safe_font(FONT_PATH_BOLD, 36)

    # Draw bold goal title
    title_text = f"🌿 {tip_data['goal']}"
    draw.text((60, 60), title_text, font=title_font, fill=TITLE_COLOR)

    # Draw box area behind tips
    box_top = 160
    box_left = 50
    box_right = WIDTH - 50
    box_bottom = 860
    draw.rounded_rectangle([box_left, box_top, box_right, box_bottom], radius=40, fill=BOX_COLOR)

    # Draw each bullet point with wrapping
    y = 200
    for point in tip_data["points"]:
        wrapped = textwrap.wrap(point, width=40)
        for line in wrapped:
            draw.text((80, y), line, font=point_font, fill=POINT_COLOR)
            y += 54
        y += 24

    # Draw @factsip footer
    draw.text((WIDTH - 240, HEIGHT - 60), "@factsip", font=footer_font, fill=FOOTER_COLOR)

    # Save image
    os.makedirs("output", exist_ok=True)
    filename = f"output/factsip_post_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(filename)

    print("✅ Image created at:", filename)
    return filename
