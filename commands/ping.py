from linebot.models import TextSendMessage

class Ping:
    admin = False

    def run(self, bot, event, *args):
        return [TextSendMessage(text="Pong")]