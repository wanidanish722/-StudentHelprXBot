import requests
import time

TOKEN = "8848419731:AAGGGOM3HBtqzJvQF5kkNPGwHD1z1rm_GmU"

url = f"https://api.telegram.org/bot{TOKEN}"

last_update_id = 0

print("Bot is running...")

while True:
    try:
        updates = requests.get(
            f"{url}/getUpdates?offset={last_update_id + 1}"
        ).json()

        if updates["ok"]:
            for result in updates["result"]:
                last_update_id = result["update_id"]

                if "message" in result:
                    chat_id = result["message"]["chat"]["id"]
                    text = result["message"].get("text", "")

                    # Start command
                    if text == "/start":
                        message = """
👋 Welcome to Student AI Bot!

📚 Available Notes:
1. Math
2. Science
3. English

Send class + subject
Example:
10th math
"""

                    # Notes system
                    elif "math" in text.lower():
                        message = "📘 Math notes coming soon!"

                    elif "science" in text.lower():
                        message = "🧪 Science notes coming soon!"

                    elif "english" in text.lower():
                        message = "📖 English notes coming soon!"

                    else:
                        message = f"✏️ You said: {text}"

                    requests.get(
                        f"{url}/sendMessage",
                        params={
                            "chat_id": chat_id,
                            "text": message
                        }
                    )

        time.sleep(2)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
