# main.py

import schedule
import time
from quote_generator import get_daily_tip
from create_post import create_fact_image
from post_to_instagram import post_to_instagram
from telegram_alert import send_telegram_alert
from dotenv import load_dotenv

load_dotenv()

def run_bot():
    try:
        tip_data = get_daily_tip()
        image_path = create_fact_image(tip_data)
        post_to_instagram(image_path, tip_data['caption'])
        send_telegram_alert(f"✅ Posted: {tip_data['goal']}")
        print("✅ Post successful:", tip_data["goal"])
    except Exception as e:
        error_msg = f"❌ Bot failed: {str(e)}"
        print(error_msg)
        send_telegram_alert(error_msg)

# Schedule posts 3 times a day (UTC)
schedule.every().day.at("19:21").do(run_bot)
schedule.every().day.at("13:00").do(run_bot)
schedule.every().day.at("18:00").do(run_bot)

print("🔄 FactSip bot running. Waiting for scheduled times...")

if __name__ == "__main__":
    run_bot()  # Run immediately once
    while True:
        schedule.run_pending()
        time.sleep(30)
