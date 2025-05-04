# main.py

import schedule
import time
from post_to_instagram import post_to_instagram
from create_post import create_fact_image
from quote_generator import get_daily_tip
from telegram_alert import send_telegram_alert

def run_bot():
    try:
        tip_data = get_daily_tip()
        image_path = create_fact_image(tip_data)
        post_to_instagram(image_path, tip_data['caption'])
        send_telegram_alert(f"✅ Posted: {tip_data['goal']}")
    except Exception as e:
        send_telegram_alert(f"❌ Failed to post: {str(e)}")

# Run every day at 8:00 AM UTC (adjust as needed)
schedule.every().day.at("19:00\5").do(run_bot)

if __name__ == "__main__":
    print("🚀 FactSip bot started...")
    run_bot()
    while True:
        schedule.run_pending()
        time.sleep(60)
