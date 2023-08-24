import json
from pathlib import Path
from linebot.models import TextSendMessage, FlexSendMessage, BubbleContainer
from lib.whitelist import get_whitelist
from lib.profile import get_profile

class Link:
    admin = True

    def __init__(self):
        with open(Path.cwd() / "data" / "links.json") as f:
            self.links: dict = json.load(f)

    def run(self, bot, event, *args):
        profile = get_profile(bot, event)

        if len(args) == 1:
            return self.take_link(None)
        elif args[1] in ["add", "remove"] and profile.user_id not in get_whitelist():
            return [TextSendMessage(text="Kamu tidak bisa menambahkan atau menghapus link (hanya admin atau orang yang di-whitelist)")]

        if args[1] == "add":
            return [TextSendMessage(text=self.add_link(*args[2::]))]
        elif args[1] == "list":
            return [TextSendMessage(text=self.list_link(args[2] if len(args) > 2 else None))]
        elif args[1] == "help":
            return [TextSendMessage(text=self.help_link(profile.user_id in get_whitelist()))]
        else:
            return self.take_link(args[1])
        
    def __get_template(self) -> dict:
        with open(Path.cwd() / "templates" / "link.json") as f:
            return json.load(f)

    def __get_link(self, namespace: str, value: str):
        """Get single link with `namespace:value`"""
        template = self.__get_template()
        if namespace not in list(self.links.keys()):
            template['body']['contents'] += [{
                "type": "text",
                "text": f"Tidak bisa menemukan grup '{namespace}'",
                "color": "#C30000FF",
                "wrap": True,
                "contents": []
            }]
            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Link Website Penting", contents=flex)]

        data = next(filter(lambda link: link['id'] == value, self.links[namespace]['list']), None)
        if not data:
            template['body']['contents'] += [{
                "type": "text",
                "text": f"Tidak bisa menemukan id '{value}' dalam grup '{namespace}'",
                "color": "#C30000FF",
                "wrap": True,
                "contents": []
            }]
            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Link Website Penting", contents=flex)]

        template['header']['contents'][0]['text'] += f"({namespace.upper()})"
        template['body']['contents'] += [{
            "type": "button",
            "action": {
                "type": "uri",
                "label": data['nama'],
                "uri": data['link']
            },
            "height": "sm",
            "style": "primary"
        }]
        flex = BubbleContainer.new_from_json_dict(data=template)
        return [FlexSendMessage(alt_text="Link Website Penting", contents=flex)]

    def __query_links(self, namespace: str):
        """Get all of the link from `namespace`"""
        template = self.__get_template()
        if namespace not in list(self.links.keys()):
            template['body']['contents'] += [{
                "type": "text",
                "text": f"Tidak bisa menemukan grup '{namespace}'",
                "color": "#C30000FF",
                "wrap": True,
                "contents": []
            }]
            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Link Website Penting", contents=flex)]

        template['header']['contents'][0]['text'] += f"({namespace.upper()})"
        links = self.links[namespace]['list']

        for data in links:
            template['body']['contents'] += [{
                "type": "button",
                "action": {
                    "type": "uri",
                    "label": data['nama'],
                    "uri": data['link']
                },
                "height": "sm",
                "style": "primary"
            }]

        flex = BubbleContainer.new_from_json_dict(data=template)
        return [FlexSendMessage(alt_text="Link Website Penting", contents=flex)]

    def take_link(self, id: str):
        """Take single or multiple link and convert into message"""
        if not id:
            return self.__query_links("cs23")

        val = id.strip().split(":")

        if len(val) == 1:
            return self.__query_links(id)
        return self.__get_link(val[0], val[1])

    def add_link(self, id: str, name: str, links: str | list[str]):
        """Add link into database"""
        val = id.strip().split(":")

        if val[0] not in self.links:
            self.links[val[0]] = {
                "whitelist": False,
                "list": []
            }

        self.links[val[0]]['list'].append({
            "id": val[1],
            "nama": name,
            "link": links,
        })

        with open(Path.cwd() / "data" / "links.json", "w") as f:
            json.dump(self.links, f, indent=4)

        return f"Link '{id}' berhasil ditambahkan"

    def list_link(self, group: str):
        header = "[LINK] ~ Link grup\n" \
            if not group \
            else f"[LINK] ~ Link {group.upper()}\n"

        return header + (" | ".join(list(self.links.keys())) \
            if not group \
            else " | ".join(map(lambda x: x['id'], self.links[group]['list'])))

    def help_link(self, admin: bool):
        message = """Command '/link'

/link [group]:[id]
~ group (opsional): Identitas grup dari beberapa link. '/link list' untuk melihat daftar grup yang tersedia.
~ id (opsional): Identitas dari link tersebut. '/link list [group]' untuk melihat daftar link dari grup tersebut.
---
/link list
> Melihat daftar grup/link dalam grup

Contoh:
/link cs23
/link events:okk"""

        if admin:
            message += "\n" + """(Khusus Admin dan orang yang di-whitelist)
Kalian bisa menambahkan link terbaru dan menghapus link yang tidak digunakan lagi (outdated)
/link add|remove [id] ..."""

        return message


if __name__ == "__main__":
    Link().add_link("test:test", "Test Events", "https://example.com")