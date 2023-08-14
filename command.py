import json
from linebot.models import TextMessage, FlexContainer, BubbleContainer, BoxComponent, ImageComponent, TextComponent, ButtonComponent, URIAction
from events.PSAF import PSAF

class Command:
    @staticmethod
    def event(*args):
        return True, "Untuk sementara ini, kalian bisa liat di docs.google.com/document/d/1aOgFa9rmb10GEpOpmjUVeTXoYX51tx91r8Pcj5-pGxY/edit?usp=sharing"

    @staticmethod
    def link(*args):
        with open("./data/link.json", "r") as f:
            data = json.load(f)
            print(data)

        link_join = lambda x: "\n".join(x)

        message = "[LINK INSTAGRAM PENTING]\n\n"
        message += "\n".join([
            f"{i + 1}. {l['nama']}: \n{l['link'] if type(l['link']) is str else link_join(l['link'])}"
            for i, l in enumerate(data)])

        return True, message

    @staticmethod
    def akun(*args):
        with open("./data/akun.json", "r") as f:
            data = json.load(f)
            print(data)

        link_join = lambda x: "\n".join(x)

        message = "[LINK INSTAGRAM PENTING]\n\n"
        message += "\n".join([
            f"{i + 1}. {l['nama']}: \n{l['link']}"
            for i, l in enumerate(data)])

        return True, message

    @staticmethod
    def update(*args):
        with open("./update/recent.txt", "r") as f:
            data = f.read()

        return True, data

    @staticmethod
    def help(*args):
        with open("./help.txt", "r") as f:
            data = f.read()

        return True, data
    
    @staticmethod
    def okk(*args):
        # HERO
        hero = ImageComponent(
            url="https://scontent.cdninstagram.com/v/t51.2885-19/342501269_623735279189278_1091141984677910224_n.jpg?stp=dst-jpg_s240x240&_nc_cat=110&ccb=1-7&_nc_sid=c4dd86&_nc_ohc=AGXXjIRoJeYAX_i8mre&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.cdninstagram.com&oh=00_AfBH4VZXp0tDfyau4X4dRkbSsd_U_SDnxiF0b21CSICAVQ&oe=65004F41",
            size="full",
            aspect_ratio="20:13",
            aspect_mode="cover"
        )

        # BODY
        title = TextComponent(text="OKK UI 2023", weight="bold", size="xl")
        desc = TextComponent(text="Puncak OKK UI yang akan dilaksanakan 14 Agustus dengan bintang tamu yang menarik", size="sm", wrap=True)
        # INFO
        # Tanggal
        tanggal = BoxComponent(layout="baseline", spacing="sm", contents=[
            TextComponent(text="Tanggal", color="#aaaaaa", size="sm", flex=1),
            TextComponent(text="14 Agustus 2023", wrap=True, color="#666666", size="sm", flex=4)
        ])
        # Waktu
        waktu = BoxComponent(layout="baseline", spacing="sm", contents=[
            TextComponent(text="Waktu", color="#aaaaaa", size="sm", flex=1),
            TextComponent(text="[Sesi 1] 07.00 - 11.00\n[Sesi 2] 13.00 - 17.00", wrap=True, color="#666666", size="sm", flex=4)
        ])
        # Tempat
        tempat = BoxComponent(layout="baseline", spacing="sm", contents=[
            TextComponent(text="Tempat", color="#aaaaaa", size="sm", flex=1),
            TextComponent(text="Balairung Universitas Indonesia", wrap=True, color="#666666", size="sm", flex=4)
        ])
        # [BOX::INFO]
        info = BoxComponent(layout="vertical", margin="lg", spacing="sm", contents=[tanggal, waktu, tempat])
        body = BoxComponent(layout="vertical", contents=[title, desc, info])

        # FOOTER
        # Website
        web = ButtonComponent(style="primary", height="sm", action=[URIAction(label="WEBSITE OKK", uri="https://okk.ui.ac.id/")])
        book = ButtonComponent(style="secondary", height="sm", action=[URIAction(label="BOOKLET OKK", uri="https://drive.google.com/file/d/1hPsz5_hlXMeF8G5Kf8ImRC0UmbJewgi-/view")])
        footer = BoxComponent(layout="vertical", spacing="sm", flex=0, contents=[web, book])

        return True, BubbleContainer(size="mega", hero=hero, body=body, footer=footer)

    @staticmethod
    def psaf(*args):
        return PSAF().get()