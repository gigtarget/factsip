# post_to_instagram.py

from instagrapi import Client
import os

def post_to_instagram(image_path, caption):
    cl = Client()

    # Login with session or credentials
    cl.load_settings("session.json")
    try:
        cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))
        cl.dump_settings("session.json")
    except Exception as e:
        raise Exception("Instagram login failed: " + str(e))

    try:
        cl.photo_upload(
            path=image_path,
            caption=caption
        )
    except Exception as e:
        raise Exception("Failed to post image: " + str(e))
