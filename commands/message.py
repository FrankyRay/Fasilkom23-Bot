from linebot.models import TextSendMessage

class Message:
    admin = True

    def run(self, bot, event, id, message, *args):
        bot.push_message(id, [TextSendMessage(text=message)])
        return [TextSendMessage(text="Pesan berhasil dikirimkan ke grup")]