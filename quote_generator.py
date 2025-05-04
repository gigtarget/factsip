# quote_generator.py

import openai
import os
import json

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_daily_tip():
    prompt = """
Generate a daily health tip in the following JSON format:

{
  "goal": "Goal Name (e.g., Boost Immunity)",
  "points": [
    "🟢 First tip here...",
    "🟢 Second tip...",
    "🟢 Third tip...",
    "🟢 Final actionable tip..."
  ],
  "caption": "Instagram-style caption combining the tips, goal, and a few relevant hashtags."
}

Keep the tone helpful, simple, goal-oriented. Use emojis in tips and 4–6 hashtags in caption.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a nutrition coach who creates bite-sized Instagram health tips."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )

    output = response.choices[0].message.content.strip()

    try:
        return json.loads(output)
    except Exception as e:
        raise ValueError("Failed to parse GPT response:\n" + output)
