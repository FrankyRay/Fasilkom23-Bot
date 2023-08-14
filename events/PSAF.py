from linebot.models import BubbleContainer, BoxComponent, ImageComponent, TextComponent, IconComponent, SpanComponent, CarouselContainer

class PSAF:
    def __init__(self):
        self._pages = CarouselContainer(contents=[
            self._title(),
            self._pakaian_laki(),
            self._pakaian_perempuan(),
            self._tempat_waktu(),
            self._keperluan(),
            self._info_tambahan()
        ])

    def get(self):
        return True, self._pages

    def _title(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(
            text="PSAF FASILKOM 2023",
            weight="bold",
            size="lg",
            align="center"
        )])

        # HERO
        hero = ImageComponent(
            url="https://instagram.fcgk3-2.fna.fbcdn.net/v/t39.30808-6/367011370_18231418849236935_1181392971844523124_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08&_nc_ht=instagram.fcgk3-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=x6tXoTKRt2AAX_Maxvs&edm=AGenrX8AAAAA&ccb=7-5&oh=00_AfCq4UTYyReZd0usCuUxFRBz5MbXpzPzoB3WLaznGXP9JQ&oe=64DF0D34&_nc_sid=ed990e",
            size="full",
            aspect_ratio="442:201"
        )

        # BODY
        body_1 = TextComponent(
            text="APA SAJA PERATURAN-PERATURAN YANG ADA? TEMPAT DAN WAKTU? KETENTUAN DRESS CODE?",
            weight="bold",
            align="center",
            wrap=True
        )

        body_2 = BoxComponent(layout="baseline", margin="md", contents=[
            TextComponent(text="Cek message selanjutnya", align="center"),
            IconComponent(url="https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-arrow-right-c-256.png", offset_top="2px")
        ])

        body_3 = TextComponent(
            text="ATAU BISA CEK DI BOOKLET PERATURAN PSAF",
            weight="bold",
            align="center",
            wrap=True
        )

        body_4 = TextComponent(
            text="https://docs.google.com/document/d/1m9C0klKNq_c8pVthDBd65tTl776P3DJUhVG8oGoH4Ho/edit#heading=h.7k5kkmeaon3c",
            weight="bold",
            align="center",
            wrap=True
        )

        body = BoxComponent(layout="vertical", contents=[body_1, body_2, body_3, body_4])

        # FOOTER
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="PSAF - "),
            SpanComponent(text="1/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[page])

        # MAIN PAGE
        return BubbleContainer(size="giga", header=header, hero=hero, body=body, footer=footer)

    def _pakaian_laki(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(text="PAKAIAN: LAKI-LAKI", weight="bold", size="lg")])

        # BODY
        # Atasan
        text_atasan = TextComponent(text="Atasan", flex=3, wrap=True, contents=[
            SpanComponent(text="Baju kemeja berkerah warna "),
            SpanComponent(text="bebas", color="#FF0000"),
            SpanComponent(text=" atau "),
            SpanComponent(text="putih", color="#0000FF"),
            SpanComponent(text="/"),
            SpanComponent(text="batik (kemeja putih jika tidak ada)", color="#00AA00"),
            SpanComponent(text=" (lengan panjang/pendek)"),
        ])
        atasan = BoxComponent(layout="baseline", contents=[TextComponent(text="Atasan", color="#999999", flex=1), text_atasan])
        # Bawahan
        text_bawahan = TextComponent(text="Celana bahan panjang berwarna hitam dan bukan jeans", flex=3, wrap=True)
        bawahan = BoxComponent(layout="baseline", contents=[TextComponent(text="Bawahan", color="#999999", flex=1), text_bawahan])
        # Alas Kaki
        text_alas_kaki = TextComponent(text="Menggunakan sepatu yang menutupi tumit dan jari kaki", flex=3, wrap=True)
        alas_kaki = BoxComponent(layout="baseline", contents=[TextComponent(text="Alas Kaki", color="#999999", flex=1), text_alas_kaki])
        # MAIN BODY
        body = BoxComponent(layout="vertical", contents=[atasan, bawahan, alas_kaki])

        # FOOTER
        deskripsi = TextComponent(text="Deskripsi", style="italic", wrap=True, contents=[
            SpanComponent(text="Warna pada teks menunjukkan ketentuan pakaian pada tanggal tertentu ("),
            SpanComponent(text="15", color="#FF0000"),
            SpanComponent(text=" / "),
            SpanComponent(text="16", color="#00AA00"),
            SpanComponent(text=" / "),
            SpanComponent(text="18", color="#0000FF"),
            SpanComponent(text=" Agustus 2023)\n"),
            SpanComponent(text="INFO: https://docs.google.com/document/d/1wQRs6a8bUAVsAzoLDZryPyEFuMorR7blEcrNLFv8FbE/edit", weight="bold"),
        ])
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="Pakaian: Laki-Laki - "),
            SpanComponent(text="2/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[deskripsi, page])

        return BubbleContainer(size="giga", header=header, body=body, footer=footer)

    def _pakaian_perempuan(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(text="PAKAIAN: PEREMPUAN", weight="bold", size="lg")])

        # BODY
        # Atasan
        text_atasan = TextComponent(text="Atasan", flex=3, wrap=True, contents=[
            SpanComponent(text="Baju kemeja berkerah warna "),
            SpanComponent(text="bebas", color="#FF0000"),
            SpanComponent(text=" atau "),
            SpanComponent(text="putih", color="#0000FF"),
            SpanComponent(text="/"),
            SpanComponent(text="batik (atau blouse), tidak kaus maupun terbuka (kemeja putih jika tidak ada)", color="#00AA00"),
            SpanComponent(text=" (lengan panjang/pendek)\nMenggunakan kerudung warna "),
            SpanComponent(text="be", color="#FF0000"),
            SpanComponent(text="bas", color="#00AA00"),
            SpanComponent(text="/"),
            SpanComponent(text="putih formal", color="#0000FF"),
            SpanComponent(text="\nDan lain sebagainya...", style="italic"),
        ])
        atasan = BoxComponent(layout="baseline", contents=[TextComponent(text="Atasan", color="#999999", flex=1), text_atasan])
        # Bawahan
        text_bawahan = TextComponent(text="Rok berwarna hitam yang panjangnya minimal dibawah lutut saat duduk", flex=3, wrap=True)
        bawahan = BoxComponent(layout="baseline", contents=[TextComponent(text="Bawahan", color="#999999", flex=1), text_bawahan])
        # Alas Kaki
        text_alas_kaki = TextComponent(text="Alas Kaki", flex=3, wrap=True, content=[
            SpanComponent(text="Menggunakan sepatu yang menutupi tumit dan jari kaki "),
            SpanComponent(text="(bukan high heels)", style="italic"),
        ])
        alas_kaki = BoxComponent(layout="baseline", contents=[TextComponent(text="Alas Kaki", color="#999999", flex=1), text_alas_kaki])
        # MAIN BODY
        body = BoxComponent(layout="vertical", contents=[atasan, bawahan, alas_kaki])

        # FOOTER
        deskripsi = TextComponent(text="Deskripsi", style="italic", wrap=True, contents=[
            SpanComponent(text="Warna pada teks menunjukkan ketentuan pakaian pada tanggal tertentu ("),
            SpanComponent(text="15", color="#FF0000"),
            SpanComponent(text=" / "),
            SpanComponent(text="16", color="#00AA00"),
            SpanComponent(text=" / "),
            SpanComponent(text="18", color="#0000FF"),
            SpanComponent(text=" Agustus 2023)\n"),
            SpanComponent(text="INFO: https://docs.google.com/document/d/1wQRs6a8bUAVsAzoLDZryPyEFuMorR7blEcrNLFv8FbE/edit", weight="bold"),
        ])
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="Pakaian: Perempuan - "),
            SpanComponent(text="3/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[deskripsi, page])

        return BubbleContainer(size="giga", header=header, body=body, footer=footer)

    def _tempat_waktu(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(text="TEMPAT & WAKTU", weight="bold", size="lg")])

        # BODY
        intro = TextComponent(text="Semua Maba Fasilkom UI harus sudah datang pada pukul 06.30 WIB (Jumat: 07.00 WIB)", wrap=True)
        # 15 Agustus
        agustus_15 = BoxComponent(layout="vertical", margin="sm", contents=[
            TextComponent(text="15", size="lg", weight="bold", contents=[
                SpanComponent(text="15 Agustus 2023 "),
                SpanComponent(text="*", color="#FF2222"),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Gedung Baru", color="#999999", wrap=True, flex=1),
                TextComponent(text="Sistem Informasi\nIlmu Komputer KKI", wrap=True, flex=2),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Gedung Lama", color="#999999", wrap=True, flex=1),
                TextComponent(text="Ilmu Komputer [Reg & Non]", wrap=True, flex=2),
            ]),
        ])
        # 16 Agustus
        agustus_16 = BoxComponent(layout="vertical", margin="sm", contents=[
            TextComponent(text="16", size="lg", weight="bold", contents=[
                SpanComponent(text="16 Agustus 2023 "),
                SpanComponent(text="*", color="#FF2222"),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Gedung Baru", color="#999999", wrap=True, flex=1),
                TextComponent(text="Ilmu Komputer [Reg & Non]", wrap=True, flex=2),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Gedung Lama", color="#999999", wrap=True, flex=1),
                TextComponent(text="Sistem Informasi\nIlmu Komputer KKI", wrap=True, flex=2),
            ]),
        ])
        # 18 Agustus
        agustus_18 = BoxComponent(layout="vertical", margin="sm", contents=[
            TextComponent(text="18", size="lg", weight="bold", contents=[
                SpanComponent(text="18 Agustus 2023 "),
                SpanComponent(text="**", color="#FF2222"),
            ]),
            TextComponent(text="Semua mahasiswa berada di Gedung Baru"),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Auditorium", color="#999999", wrap=True, flex=1),
                TextComponent(text="Ilmu Komputer [Reg & Non]", wrap=True, flex=2),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="Plaza Lantai Dasar", color="#999999", wrap=True, flex=1),
                TextComponent(text="Sistem Informasi\nIlmu Komputer KKI", wrap=True, flex=2),
            ]),
        ])
        # MAIN BODY
        body = BoxComponent(layout="vertical", contents=[intro, agustus_15, agustus_16, agustus_18])

        # FOOTER
        bintang_1 = BoxComponent(layout="baseline", contents=[
            TextComponent(text="*", color="#FF2222", flex=1),
            TextComponent(text="Gedung Baru mendapat snack + makan siang, sedangkan Gedung Lama hanya snack saja", wrap=True, flex=12),
        ])
        bintang_2 = BoxComponent(layout="baseline", contents=[
            TextComponent(text="**", color="#FF2222", flex=1),
            TextComponent(text="Disarankan membawa bekal masing-masing dan tidak telat", wrap=True, flex=12),
        ])
        bintang = BoxComponent(layout="vertical", margin="sm", contents=[bintang_1, bintang_2])
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="Tempat & Waktu - "),
            SpanComponent(text="4/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[bintang, page])

        return BubbleContainer(size="giga", header=header, body=body, footer=footer)

    def _keperluan(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(text="BARANG KEPERLUAN", weight="bold", size="lg")])

        # BODY
        name_tag = BoxComponent(layout="vertical", margin="xs", contents=[
            TextComponent(text="Name Tag", size="lg", weight="bold"),
            TextComponent(text="Isi", wrap=True, contents=[
                SpanComponent(text="Name tag harus di print dengan ukuran "),
                SpanComponent(text="9 x 6 cm, dilaminating, dan dipeniti", weight="bold"),
                SpanComponent(text=". Link Name Tag bisa di-unduh di https://ristek.link/NameTagMaba23"),
            ])
        ])
        lainnya = BoxComponent(layout="vertical", margin="xs", contents=[
            TextComponent(text="Lain-Lain", size="lg", weight="bold"),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="1.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Bagi mahasiswa baru yang beragama Islam membawa perlengkapan sholat.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="2.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Disarankan membawa botol minum (sama airnya ya...), bekal, dan obat-obatan pribadi.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="3.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Tidak diperkenankan membawa barang-barang seperti perangkat elektronik (kecuali HP), perhiasan, mainan, rokok, dsb.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="4.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Alat tulis untuk mencatat materi (opsional wkwk)", wrap=True, flex=12),
            ]),
        ])
        # MAIN BODY
        body = BoxComponent(layout="vertical", contents=[name_tag, lainnya])

        # FOOTER
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="Barang Keperluan - "),
            SpanComponent(text="5/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[page])

        return BubbleContainer(size="giga", header=header, body=body, footer=footer)

    def _info_tambahan(self):
        # HEADER
        header = BoxComponent(layout="vertical", contents=[TextComponent(text="INFORMASI TAMBAHAN", weight="bold", size="lg")])

        # BODY
        psaf = BoxComponent(layout="vertical", margin="xs", contents=[
            TextComponent(text="Selama PSAF", size="lg", weight="bold"),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="1.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Menggunakan name tag PMB.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="2.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Mematikan nada dering komunikasi.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="3.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Tidak menggunakan telepon genggam kecuali dengan urusan mendadak atau saat istirahat.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="4.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Memperhatikan setiap materi yang diberikan selama kegiatan  dan membawa alat tulis.", wrap=True, flex=12),
            ]),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="5.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Mengikuti acara hingga akhir.", wrap=True, flex=12),
            ]),
        ])
        tambahan = BoxComponent(layout="vertical", margin="xs", contents=[
            TextComponent(text="Info Tambahan", size="lg", weight="bold"),
            BoxComponent(layout="baseline", contents=[
                TextComponent(text="1.", color="#999999", wrap=True, flex=1),
                TextComponent(text="Acara di Gedung Lama sampai Zuhur, sementara Gedung Baru hingga sore", wrap=True, flex=12),
            ])
        ])
        # MAIN BODY
        body = BoxComponent(layout="vertical", contents=[psaf, tambahan])

        # FOOTER
        page = TextComponent(text="page", align="end", size="sm", contents=[
            SpanComponent(text="Info Tambahan - "),
            SpanComponent(text="6/6", color="#999999")
        ])

        footer = BoxComponent(layout="vertical", contents=[page])

        return BubbleContainer(size="giga", header=header, body=body, footer=footer)