# create_post.py

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os
import datetime

def create_fact_image(tip_data):
    WIDTH, HEIGHT = 1080, 1080
    BG_COLOR = "#fffdf7"
    TITLE_COLOR = "#22543D"
    TEXT_COLOR = "#333333"
    FONT_PATH_BOLD = "templates/OpenSans-Bold.ttf"
    FONT_PATH_REGULAR = "templates/PlayfairDisplay-VariableFont_wght.ttf"

    # Create canvas
    img = Image.new("RGB", (WIDTH, HEIGHT), color=BG_COLOR)
    draw = ImageDraw.Draw(img)

    # Load fonts
    title_font = ImageFont.truetype(FONT_PATH_BOLD, 64)
    point_font = ImageFont.truetype(FONT_PATH_REGULAR, 42)

    # Draw Title
    title = tip_data["goal"]
    draw.text((60, 60), title, font=title_font, fill=TITLE_COLOR)

    # Draw bullet points
    y_offset = 180
    for point in tip_data["points"]:
        wrapped_text = textwrap.wrap(point, width=38)
        for line in wrapped_text:
            draw.text((60, y_offset), line, font=point_font, fill=TEXT_COLOR)
            y_offset += 56
        y_offset += 20

    # Optional branding (bottom right)
    footer = "@factsip"
    footer_font = ImageFont.truetype(FONT_PATH_BOLD, 36)
    draw.text((WIDTH - 220, HEIGHT - 80), footer, font=footer_font, fill="#888")

    # Save image
    filename = f"output/factsip_post_{datetime.datetime.now().strftime('%Y%m%d')}.png"
    os.makedirs("output", exist_ok=True)
    img.save(filename)

    return filename
