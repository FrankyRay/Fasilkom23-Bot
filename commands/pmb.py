from linebot.models import TextSendMessage

class PMB:
    admin = True

    def run(self, bot, event, *args):
        return [TextSendMessage(text="Pong")]
    
    def mentoring(self, npm):
        pass