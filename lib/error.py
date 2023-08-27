import json
from pathlib import Path
from linebot.models import FlexSendMessage, BubbleContainer

def call_error(pesan: str, command: str = None):
    with open(Path.cwd() / "templates" / "error.json") as f:
        template = json.load(f)

    template['body']['contents'][0]['text'] = pesan
    if command:
        template['footer']['contents'][0]['text'] += "/" + command

    flex = BubbleContainer.new_from_json_dict(data=template)
    return [FlexSendMessage("Error", contents=flex)]