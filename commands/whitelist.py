import json
from pathlib import Path
from linebot.models import TextSendMessage

class Whitelist:
    admin = True

    def __init__(self):
        with open(Path.cwd() / "data" / "userlist.json") as f:
            self.ids = json.load(f)

    def run(self, bot, event, *args):
        if args[1] == "add":
            message = self.__add_whitelist(event.message.mention.mentionees)
        elif args[1] == "remove":
            message = self.__remove_whitelist(event.message.mention.mentionees)

        return [TextSendMessage(text=message)]
    
    def __add_whitelist(self, users):
        message = "User(s) berhasil ditambahkan ke daftar whitelist"
        for user in users:
            if user.user_id in self.ids['whitelist']:
                message += "\n(Beberapa user sudah ada dalam daftar whitelist)"
            else:
                self.ids['whitelist'].append(user.user_id)

        with open(Path.cwd() / "data" / "userlist.json") as f:
            json.dump(self.ids, f, indent=4)
            return message
    
    def __remove_whitelist(self, users):
        message = "User(s) berhasil dihapus dari daftar whitelist"
        for user in users:
            if user.user_id not in self.ids['whitelist']:
                message += "\n(Beberapa user tidak ada dalam daftar whitelist)"
            elif user.user_id == "U7b2348d438909133abdc503bf47c0e32":
                message += "\n(User 'FrankyRayMS' tidak bisa dihapus. Enak aja mau di hapus :P)"
            else:
                self.ids['whitelist'].remove(user.user_id)

        with open(Path.cwd() / "data" / "userlist.json") as f:
            json.dump(self.ids, f, indent=4)
            return message