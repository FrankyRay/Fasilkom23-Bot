from pathlib import Path
import json

def get_whitelist():
    with open(Path.cwd() / "data" / "userlist.json") as w:
        return json.load(w)['whitelist']