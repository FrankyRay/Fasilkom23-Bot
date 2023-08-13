import os
from flask import Flask, request, abort
# LINE BOT
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, BubbleContainer, FlexSendMessage
# EXTENSION
from command import Command

app = Flask(__name__)

line_bot_api = LineBotApi('cql3/UoZ9n8yFrMxt81Pw4+mPxZuumYpD0Kgy+LA+9ILg+r9y3HqwsXkdxEumMshKqTUdNL+lWVwESAUyKwfNu7UXKSByl9fhQWHX6OmLB67XsMhbndwsYeluuiRxYeMOO0P6/7b8Iomi0BAR/pU0AdB04t89/1O/w1cDnyilFU=') # YOUR_CHANNEL_ACCESS_TOKEN
handler = WebhookHandler('1a7ed8ecdb583c177abbcb3ad26903b8') # YOUR_CHANNEL_SECRET


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
    
    cmd, *args = event.message.text.split(" ")
    command = getattr(Command, cmd[1::])
    if not callable(command):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f"Command '{cmd[1::]}' tidak bisa dipanggil atau tidak punya akses"))
        return
    
    message = command(args)
    if type(message) is BubbleContainer:
        line_bot_api.reply_message(event.reply_token, FlexSendMessage(alt_text="OKK UI 2023", contents=message))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)