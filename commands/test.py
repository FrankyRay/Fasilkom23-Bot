from linebot.models import TemplateSendMessage, ConfirmTemplate, URIAction

class Test:
    admin = True

    def run(self, *args):
        return [TemplateSendMessage(alt_text="Test Message", template=ConfirmTemplate(text="Are you sure?", actions=[
            URIAction("YES", "https://example.com"),
            URIAction("NO", "https://google.co.id")
        ]))]