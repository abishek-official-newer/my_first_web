from flask import Blueprint, request, render_template
import requests
import os

home_bp = Blueprint("home", __name__)


API_KEY = os.getenv("API_KEY")


def ask_ai(message):

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",

        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },

        json={
            "model": "deepseek/deepseek-chat",

            "messages": [
                {
                    "role": "system",
                    "content": """
Reply in plain text only.

Do not use markdown.

Do not use ** symbols.

Do not use ### headings.

Do not use code blocks.

Keep answers clean and readable.
"""
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        }
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    data = response.json()

    return data["choices"][0]["message"]["content"]


@home_bp.route("/")
def home():
    return render_template("home.html")


@home_bp.route("/ai_bot", methods=["GET", "POST"])
def ai_bot():

    ai_response = ""
    user_message = ""

    if request.method == "POST":

        user_message = request.form.get("message")

        try:
            ai_response = ask_ai(user_message)

        except Exception as e:
            ai_response = f"Error: {e}"

    return render_template(
        "ai_bot.html",
        answer=ai_response,
        question=user_message
    )
