import csv
import json
from pathlib import Path
from linebot.models import TextSendMessage, FlexSendMessage, BubbleContainer, CarouselContainer
from lib.error import call_error

class Kelas:
    admin = False

    def __init__(self) -> None:
        with open(Path.cwd() / "data" / "kelas.json") as f:
            self.KELAS = json.load(f)

        with open(Path.cwd() / "data" / "mahasiswa.json") as f:
            self.MAHASISWA = json.load(f)

    def run(self, bot, event, *args):
        if len(args) == 1:
            return call_error("Please input the NPM")
        elif len(args) == 2:
            return self.__get_profile(args[1])
        elif len(args) == 3:
            return self.__get_matches(args[1], args[2])

    def __get_template(self):
        with open(Path.cwd() / "templates" / "kelas_v2.json") as f:
            return json.load(f)

    def __get_profile(self, npm):
        bubbles = []

        mahasiswa = next(iter([ms for ms in self.MAHASISWA if ms['NPM'] == int(npm)]), None)
        if not mahasiswa:
            return call_error(f"Cannot found any student with NPM '{npm}'!", "kelas")

        if "Kelas" not in mahasiswa and mahasiswa['Jurusan'] != "KKI":
            return call_error("Data class not found!", "kelas")

        index = 0
        if mahasiswa['Jurusan'] == "KKI":
            with open(Path.cwd() / "data" / "kki_class.json") as f:
                data = json.load(f)

            for subject in data:
                index += 1
                template = self.__get_template()

                # Ganti judul menjadi nama mahasiswa
                template['header']['contents'][0]['text'] = mahasiswa['Nama']

                # Ganti nama kelas
                template['body']['contents'][0]['contents'][0]['contents'][0]['text'] = subject['Nama']
                template['body']['contents'][0]['contents'][1]['text'] = "-"

                # Kueri jadwal kelas
                for jdw in subject['Jadwal']:
                    template['body']['contents'][0]['contents'][0]['contents'][1]['contents'].append({
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "-",
                                    "size": "sm",
                                    "color": "#BBBBBB",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": f"{jdw['Periode']}\n{jdw['Waktu']}\n{jdw['Ruang']}",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "flex": 12,
                                    "wrap": True,
                                    "contents": []
                                }
                            ]
                        })

                # Kueri pengajar
                for pj in subject["Pengajar"]:
                    template['body']['contents'][0]['contents'][0]['contents'][2]['contents'].append({
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "-",
                                    "size": "sm",
                                    "color": "#BBBBBB",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": pj,
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "flex": 12,
                                    "wrap": True,
                                    "contents": []
                                }
                            ]
                        })

                template['styles']['body']['backgroundColor'] = "#A01218" if index % 2 == 1 else "#1D1F5E"
                bubbles.append(BubbleContainer.new_from_json_dict(data=template))
        else:
            for key, val in mahasiswa['Kelas'].items():
                index += 1
                template = self.__get_template()
                data_kelas = self.KELAS[key][val]

                # Ganti judul menjadi nama mahasiswa
                template['header']['contents'][0]['text'] = mahasiswa['Nama']

                # Ganti nama kelas
                template['body']['contents'][0]['contents'][0]['contents'][0]['text'] = key
                template['body']['contents'][0]['contents'][1]['text'] = val

                # Kueri jadwal kelas
                for jdw in data_kelas['Jadwal']:
                    template['body']['contents'][0]['contents'][0]['contents'][1]['contents'].append({
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "-",
                                    "size": "sm",
                                    "color": "#BBBBBB",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": f"{jdw['Periode']}\n{jdw['Waktu']}\n{jdw['Ruang']}",
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "flex": 12,
                                    "wrap": True,
                                    "contents": []
                                }
                            ]
                        })

                # Kueri pengajar
                for pj in data_kelas["Pengajar"]:
                    template['body']['contents'][0]['contents'][0]['contents'][2]['contents'].append({
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "-",
                                    "size": "sm",
                                    "color": "#BBBBBB",
                                    "contents": []
                                },
                                {
                                    "type": "text",
                                    "text": pj,
                                    "size": "sm",
                                    "color": "#FFFFFF",
                                    "flex": 12,
                                    "wrap": True,
                                    "contents": []
                                }
                            ]
                        })

                template['styles']['body']['backgroundColor'] = "#A01218" if index % 2 == 1 else "#1D1F5E"
                bubbles.append(BubbleContainer.new_from_json_dict(data=template))

        flex = CarouselContainer(contents=bubbles)
        return [FlexSendMessage(alt_text="Info Kelas", contents=flex)]

    def __get_matches(self, npm, kelas):
        mahasiswa = next(iter([ms for ms in self.MAHASISWA if ms['NPM'] == int(npm)]), None)
        if not mahasiswa:
            return [TextSendMessage(text=f"Cannot found any student with NPM '{npm}'!")]

        if mahasiswa['Jurusan'] == "KKI":
            with open(Path.cwd() / "templates" / "cari_teman.json") as f:
                template = json.load(f)
            template['body']['contents'][0]['text'] = "Anak KKI selalu sekelas bareng anak KKI juga. What'd you expect bro?"

            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Cari Teman @Kelas", contents=flex)]
        elif kelas.lower() == "all":
            with open(Path.cwd() / "templates" / "cari_teman.json") as f:
                template = json.load(f)
            template['body']['contents'][0]['text'] = "Teman sekelas dalam SEMUA KELAS:"
            for ms in self.MAHASISWA:
                if mahasiswa['Jurusan'] != ms['Jurusan'] or mahasiswa['Kelas'] != ms['Kelas'] or mahasiswa['NPM'] == ms['NPM']:
                    continue
                template['body']['contents'][0]['text'] += f"\n- {ms['Nama']}"
                
            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Cari Teman @Kelas", contents=flex)]
        elif kelas.lower() == "any":
            bubbles = []
            for kel, kode in mahasiswa['Kelas'].items():
                with open(Path.cwd() / "templates" / "cari_teman.json") as f:
                    template = json.load(f)
                template['body']['contents'][0]['text'] = f"Teman sekelas dalam '{kel} ~ {kode}':"
                for ms in self.MAHASISWA:
                    if mahasiswa['Jurusan'] != ms['Jurusan'] or mahasiswa['Kelas'][kel] != ms['Kelas'][kel] or mahasiswa['NPM'] == ms['NPM']:
                        continue
                    template['body']['contents'][0]['text'] += f"\n- {ms['Nama']}"

                bubbles.append(BubbleContainer.new_from_json_dict(data=template))

            flex = CarouselContainer(contents=bubbles)
            return [FlexSendMessage(alt_text="Cari Teman @Kelas", contents=flex)]
            
        elif kelas.lower() not in [kls.lower() for kls in mahasiswa['Kelas'].keys()]:
            return call_error(f"Kelas '{kelas}' tidak ditemukan. Pilihan yang ada:\n{' | '.join([kls for kls in mahasiswa['Kelas'].keys()])}")
        else:
            with open(Path.cwd() / "templates" / "cari_teman.json") as f:
                template = json.load(f)
            template['body']['contents'][0]['text'] = "Teman sekelas dalam SEMUA KELAS:"
            for ms in self.MAHASISWA:
                if mahasiswa['Jurusan'] != ms['Jurusan'] or mahasiswa['Kelas'][kelas] != ms['Kelas'][kelas] or mahasiswa['NPM'] == ms['NPM']:
                    continue
                template['body']['contents'][0]['text'] += f"\n- {ms['Nama']}"

            flex = BubbleContainer.new_from_json_dict(data=template)
            return [FlexSendMessage(alt_text="Cari Teman @Kelas", contents=flex)]
