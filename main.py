import os
import requests
from decouple import config
from flask import Flask, request, abort
from commands.main import Command
from lib.profile import get_profile
from lib.whitelist import get_whitelist
# Line-Bot-SDK
from linebot import (
    LineBotApi,
    WebhookHandler,
)
from linebot.exceptions import (
    InvalidSignatureError,
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    LocationMessage,
    TextSendMessage,
    SourceGroup,
)


# Get access token
CHANNEL_ACCESS = config("CHANNEL_ACCESS")
CHANNEL_SECRET = config("CHANNEL_SECRET")
DISCORD_WEBHOOK = config("DISCORD_WEBHOOK")
# Apps
app = Flask(__name__)
bot = LineBotApi(CHANNEL_ACCESS)
handler = WebhookHandler(CHANNEL_SECRET)


# Webhook
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# Event handler
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    title = event.message.text.split("\n")[0]

    if event.message.text.startswith("/"):
        profile = get_profile(bot, event)

        # if profile.user_id not in get_whitelist():
        #     return bot.reply_message(event.reply_token, [
        #         TextSendMessage(text="Bot dalam maintenance! Mohon bersabar")
        #     ])

        message = Command.parse(bot, event, event.message.text)

        bot.reply_message(event.reply_token, message)
    elif title.startswith("[") and title.endswith("]"):
        profile = get_profile(bot, event)
        embed = {
            "embeds": [{
                "author": {
                    "name": profile.display_name,
                    "icon_url": profile.picture_url,
                },
                "title": title,
                "description": event.message.text.replace(title, '').strip(),
                "color": 0xfddc01,
            }]
        }
        webhook = requests.post(DISCORD_WEBHOOK, json=embed)

        try:
            webhook.raise_for_status()
        except requests.exceptions.HTTPError as err:
            bot.reply_message(event.reply_token, [
                TextSendMessage(text=f"Info gagal dikirimkan, status kode: {webhook.status_code}, alasan: {err}")
            ])
        else:
            bot.reply_message(event.reply_token, [
                TextSendMessage(text=f"Info berhasil dikirimkan ke discord, status kode: {webhook.status_code}")
            ])


@handler.add(MessageEvent, message=LocationMessage)
def location_message(event):
    profile = get_profile(bot, event)

    if profile.user_id not in get_whitelist():
        return

    message = "[CONVERTER] ~ Location Link on Google Maps\n\n"
    if event.message.title:
        message += "\n".join([
            f"< {event.message.title} >",
            event.message.address,
            f"https://www.google.com/maps/search/?api=1&query={event.message.title.lower().replace(' ', '+')}"
        ])
    else:
        message += "\n".join([
            event.message.address,
            f"https://www.google.com/maps/search/?api=1&query={event.message.latitude}%2C{event.message.longitude}"
        ])

    bot.reply_message(event.reply_token, [
        TextSendMessage(text=message)
    ])


# App run
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)