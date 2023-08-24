from linebot.models import TextSendMessage
from commands.test import Test
from commands.link import Link
from commands.ping import Ping
from commands.whitelist import Whitelist
from lib.whitelist import get_whitelist
from lib.profile import get_profile

class Command:
    commands = {
        "/link": Link(),
        "/ping": Ping(),
        "/test": Test(),
        "/whitelist": Whitelist(),
    }

    @classmethod
    def parse(cls, bot, event, command: str):
        profile = get_profile(bot, event)
        input_value = ""
        command_args = []
        quotation_str: bool = False
        escaped_char = False

        for char in command + " ":
            if escaped_char:
                if char == "n": input_value += "\n"
                else: input_value += char
                escaped_char = False
            elif char == "\\":
                escaped_char = True
            elif quotation_str and char == '"':
                quotation_str = False
            elif char == '"':
                quotation_str = True
            elif char == " " and not quotation_str:
                command_args += [input_value]
                input_value = ""
            else:
                input_value += char

        if (command_args[0] not in cls.commands) \
            or (cls.commands[command_args[0]].admin and profile.user_id not in get_whitelist()):
            return [TextSendMessage(text=f"Command '{command_args[0]}' tidak ditemukan atau Anda tidak memiliki akses (tidak di-whitelist)")]
        
        return cls.commands[command_args[0]].run(bot, event, *command_args)