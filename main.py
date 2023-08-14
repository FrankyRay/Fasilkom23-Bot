import os
from flask import Flask, request, abort
# LINE BOT
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, BubbleContainer, FlexSendMessage, CarouselContainer
# EXTENSION
from command import Command

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')


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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    if not event.message.text.startswith("/"):
        return
    
    profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id) \
        if event.source.group_id \
        else line_bot_api.get_profile(event.source.user_id)
    
    cmd, *args = event.message.text.split(" ")
    command = getattr(Command, cmd[1::])
    if not callable(command):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f"Command '{cmd[1::]}' tidak bisa dipanggil atau tidak punya akses"))
        return
    
    public, message = command(args)
    if not public and profile.display_name != "FrankyRayMS":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f"Command '{cmd[1::]}' tidak bisa dipanggil atau tidak punya akses"))
    elif type(message) is BubbleContainer or type(message) is CarouselContainer:
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="OKK UI 2023", contents=message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)