from linebot.models import TextSendMessage

class Ping:
    admin = False

    def run(self, *args):
        return [TextSendMessage(text="Pong")]