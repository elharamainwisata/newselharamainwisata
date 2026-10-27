"""Rencana adegan gaya output_final: footage asli kanal Kemenhaj (crop atas, buang subtitle tertanam).
Shot = ("k", kunci_video, detik_mulai, posisi_x 0..1) | ("f", path) """
R = r"D:\newshaji"
KV = {"T": "k_-cTgY3iUXBA", "M": "k_s-3BYDldEro", "Q": "k_qD7qaD0zOnY", "G": "k_GZpfBF3LObw", "P": "k_oPf1NVYP820"}
def k(v, t, x=0.5): return ("k", KV[v], t, x)
def dc(n): return ("f", f"{R}\\footage\\drive_clips\\{n}.mp4")
def ar(n): return ("f", f"{R}\\footage\\haji_drive\\ar_{n}.mov")

L = {  # pustaka adegan
    "makkah": [k("T", 13), k("T", 211)],
    "madinah": [k("Q", 10), k("Q", 55), k("Q", 61)],
    "jemaah_asrama": [k("T", 51.5), k("T", 67), k("T", 79), k("T", 74)],
    "jemaah_wawancara": [k("T", 91), k("T", 97), k("T", 103)],
    "petugas_baris": [k("T", 134.5)],
    "petugas_bantu": [k("T", 151), k("T", 157), k("T", 415), k("T", 463), k("T", 471), k("T", 475), k("Q", 101), k("Q", 116), k("Q", 286)],
    "pesawat": [k("T", 205), k("T", 529)],
    "bus": [k("T", 19), k("T", 235), k("T", 247), k("Q", 176)],
    "katering": [k("T", 253)],
    "hotel": [k("T", 265), k("T", 325), k("T", 331), k("Q", 71), k("Q", 76)],
    "klinik": [k("T", 337), k("T", 343), k("T", 361), k("T", 367), k("Q", 126), k("Q", 131)],
    "ihram": [k("T", 373), k("T", 379), k("T", 385), k("T", 391), k("T", 427)],
    "arafah_mina": [k("T", 397), k("T", 403), k("T", 409), ar("0870"), ar("0858")],
    # adegan wawancara Menteri (T494-507, T525-528) dibuang: ada nama terpotong "...n Yusuf" dan mik berlogo TV.
    # Kategori tetap ada agar giliran klip lain tidak bergeser; isinya gambar suasana tanpa wajah pejabat.
    "menteri_doorstop": [k("Q", 55), k("T", 211.5), k("Q", 58.5)],  # dicek: ~4 detik pertama tanpa wajah
    "rapat_madinah": [k("T", 508), k("T", 511)],
    "menteri_rapat": [k("M", 1), k("M", 15), k("M", 60), k("M", 885), k("M", 1080), k("M", 1125), k("M", 180)],
    "pejabat_jalan": [k("P", 12), k("P", 15)],
    "lansia": [k("G", 1), k("G", 31), k("G", 66), k("G", 168), k("G", 171)],
    "kepulangan": [k("T", 535), k("T", 541), k("T", 553), k("T", 565), k("T", 577), k("G", 150), k("G", 196.5)],
    "jemaah_madinah": [k("Q", 5), k("Q", 20), k("Q", 40)],
    "tutup": [dc("payung1"), dc("menara_haram5")],
}


# Footage Saudi (rekaman rombongan umrah Elharamain, 1080x1920): hanya potongan suasana/lokasi tanpa pose rombongan
# atau spanduk Elharamain. Shot = ("s", path, detik_mulai). Dicek lewat saudi\*.jpg (27 Okt 2026).
SAUDI = R + r"\footage\Video Saudi Elharamainwisata Umroh 1448_"
import json as _json, os as _os
_SEL = _json.load(open(_os.path.join(_os.path.dirname(__file__), "saudi_sel.json"), encoding="utf-8-sig"))
def sv(key, t): return ("s", _SEL[key], t)
def fh(name): return ("f", f"{SAUDI}\\#Footage Haramain\\{name}")
L.update({
    "bandara_jeddah": [sv("bandara_jeddah", 0.2), sv("kepulangan_jed", 0.2), sv("kepulangan_jed", 5.2)],
    "bandara_madinah": [sv("bandara_madinah", 0.2), sv("bandara_madinah", 2.6), sv("bandara_madinah", 30.1)],
    "kereta_cepat": [sv("kereta_cepat", 0.2), sv("kereta_cepat", 12.6), sv("kereta_cepat", 27.6)],
    "miqat_bir_ali": [sv("miqat_bir_ali", 0.2), sv("miqat_bir_ali", 5.1), sv("miqat_bir_ali", 10.1)],
    "raudhah": [sv("raudhah", 0.2), sv("raudhah", 42.6), sv("raudhah", 45.1)],
    # Museum Wahyu: klip yang ada berisi rombongan berpose (footage Elharamain) dan bukan museum lain -> pakai suasana Makkah
    "museum_wahyu": [fh("5. Footage Menara Masjidil Haram.mov"), fh("8. Footage Tangga di Bawah Tower Zam-zam.mov")],
    "uhud": [sv("uhud", 27.6), sv("uhud", 50.1)],
    "thaif": [sv("thaif", 27.6), sv("thaif", 35.1)],
    # hotel_saudi tanpa papan merek hotel (Movenpick dll. bisa disangka hotel yang diberitakan)
    "hotel_saudi": [fh("8. Footage Tangga di Bawah Tower Zam-zam.mov"), fh("6. Footage Pelataran Masjidil Haram.mov")],
    # klip 7 (Musholla Fairmont) tersimpan miring 90 derajat -> tidak dipakai
    "kajian": [fh("9. Footage Menara Masjid Nabawi.mov"), fh("4. Footage Sekitar Masjid Nabawi.mp4")],
    "haramain": [fh("5. Footage Menara Masjidil Haram.mov"), fh("6. Footage Pelataran Masjidil Haram.mov"),
                 fh("8. Footage Tangga di Bawah Tower Zam-zam.mov"), fh("9. Footage Menara Masjid Nabawi.mov"),
                 fh("4. Footage Sekitar Masjid Nabawi.mp4")],
})


# Footage pejabat (footage\pejabat\katalog.py): kategori "pj_<slug>" berisi adegan pejabat itu sendiri.
# Aturan: kalimat yang menyebut nama pejabat memakai kategori pejabatnya.
_PJ_DIR = R + r"\footage\pejabat"
_sys_pj = __import__("sys"); _sys_pj.path.insert(0, _PJ_DIR)
import katalog as _kat
for _slug, _p in _kat.PEJABAT.items():
    L["pj_" + _slug] = [("j", _os.path.join(_PJ_DIR, a["file"]), a["t"], a["x"], int(a["crop"][3:]))
                        for a in _p["adegan"] if a.get("pakai", True)]


def pick(*names):
    """ambil satu shot dari tiap kategori, bergilir supaya tidak berulang"""
    out = []
    for n in names:
        c = _cnt.get(n, 0); _cnt[n] = c + 1
        out.append(L[n][c % len(L[n])])
    return out
_cnt = {}

# Gaya bercerita: baris 1 = kalimat pembuka (jemaah/suasana). Kalimat yang menyebut nama pejabat selain Menhaj
# Irfan Yusuf memakai footage tanpa wajah pejabat, supaya penonton tidak salah mengira orangnya.
PLAN3 = {
    1: [pick("jemaah_asrama", "jemaah_wawancara"), pick("menteri_doorstop", "menteri_rapat"), pick("petugas_bantu", "jemaah_asrama"),
        pick("jemaah_wawancara", "lansia"), pick("jemaah_asrama", "menteri_rapat"), pick("rapat_madinah", "petugas_bantu"),
        pick("jemaah_wawancara", "jemaah_asrama"), pick("tutup")],
    2: [pick("makkah", "jemaah_madinah"), pick("pesawat", "kepulangan"), pick("madinah", "hotel"), pick("jemaah_madinah", "bus"),
        pick("ihram", "arafah_mina"), pick("jemaah_asrama", "kepulangan"), pick("petugas_bantu", "jemaah_madinah"), pick("tutup")],
    3: [pick("jemaah_wawancara", "lansia"), pick("jemaah_asrama", "jemaah_wawancara"), pick("menteri_rapat", "rapat_madinah"),
        pick("hotel", "jemaah_madinah"), pick("menteri_rapat", "pejabat_jalan"), pick("rapat_madinah", "menteri_rapat"),
        pick("jemaah_asrama", "petugas_bantu"), pick("tutup")],
    4: [pick("jemaah_asrama", "lansia"), pick("menteri_rapat", "makkah"), pick("madinah", "jemaah_madinah"),
        pick("menteri_doorstop", "menteri_doorstop"), pick("menteri_doorstop", "rapat_madinah"), pick("menteri_rapat", "jemaah_madinah"),
        pick("hotel", "katering"), pick("tutup")],
    5: [pick("makkah", "madinah"), pick("makkah", "madinah"), pick("bus", "hotel"), pick("jemaah_asrama", "arafah_mina"),
        pick("makkah", "jemaah_madinah"), pick("hotel", "bus"), pick("jemaah_madinah", "kepulangan"), pick("tutup")],
    6: [pick("jemaah_wawancara", "hotel"), pick("petugas_baris", "rapat_madinah"), pick("hotel", "petugas_bantu"), pick("katering", "bus"),
        pick("madinah", "hotel"), pick("menteri_rapat", "arafah_mina"), pick("lansia", "petugas_bantu"), pick("tutup")],
    7: [pick("jemaah_madinah", "pesawat"), pick("makkah", "jemaah_madinah"), pick("madinah", "jemaah_madinah"),
        pick("pesawat", "kepulangan"), pick("pesawat", "bus"), pick("kepulangan", "pesawat"),
        pick("jemaah_asrama", "petugas_bantu"), pick("tutup")],
    8: [pick("kepulangan", "jemaah_asrama"), pick("pesawat", "kepulangan"), pick("jemaah_asrama", "katering"),
        pick("rapat_madinah", "menteri_rapat"), pick("petugas_bantu", "jemaah_asrama"), pick("menteri_rapat", "pesawat"),
        pick("jemaah_wawancara", "kepulangan"), pick("tutup")],
    9: [pick("petugas_bantu", "madinah"), pick("petugas_baris", "jemaah_madinah"), pick("petugas_bantu", "makkah"),
        pick("rapat_madinah", "petugas_bantu"), pick("madinah", "jemaah_madinah"), pick("petugas_bantu", "lansia"),
        pick("petugas_bantu", "jemaah_madinah"), pick("tutup")],
    10: [pick("jemaah_asrama", "ihram"), pick("menteri_rapat", "petugas_baris"), pick("menteri_rapat", "jemaah_asrama"),
         pick("ihram", "jemaah_wawancara"), pick("hotel", "pesawat"), pick("menteri_doorstop", "arafah_mina"),
         pick("jemaah_asrama", "lansia"), pick("tutup")],
    11: [pick("lansia", "jemaah_madinah"), pick("menteri_doorstop", "jemaah_asrama"), pick("jemaah_madinah", "lansia"),
         pick("jemaah_asrama", "kepulangan"), pick("menteri_doorstop", "lansia"), pick("jemaah_asrama", "pesawat"),
         pick("klinik", "lansia"), pick("tutup")],
    12: [pick("jemaah_asrama", "ihram"), pick("menteri_doorstop", "katering"), pick("menteri_doorstop", "jemaah_asrama"),
         pick("ihram", "hotel"), pick("bus", "menteri_rapat"), pick("rapat_madinah", "menteri_rapat"),
         pick("jemaah_madinah", "ihram"), pick("tutup")],
    13: [pick("makkah", "jemaah_asrama"), pick("menteri_rapat", "rapat_madinah"), pick("makkah", "madinah"),
         pick("jemaah_wawancara", "lansia"), pick("ihram", "kepulangan"), pick("pesawat", "madinah"),
         pick("lansia", "jemaah_asrama"), pick("tutup")],
    14: [pick("makkah", "jemaah_madinah"), pick("kepulangan", "menteri_rapat"), pick("rapat_madinah", "menteri_rapat"),
         pick("jemaah_madinah", "pesawat"), pick("klinik", "lansia"), pick("menteri_rapat", "hotel"),
         pick("klinik", "jemaah_asrama"), pick("tutup")],
    15: [pick("petugas_bantu", "petugas_baris"), pick("rapat_madinah", "menteri_rapat"), pick("petugas_bantu", "lansia"),
         pick("makkah", "madinah"), pick("petugas_bantu", "menteri_rapat"), pick("rapat_madinah", "petugas_bantu"),
         pick("jemaah_wawancara", "petugas_bantu"), pick("tutup")],
}
# koreksi setelah cek: nama pejabat jangan jatuh di wajah orang lain (ditimpa setelah pick agar giliran klip lain tetap)
PLAN3[4][5] = [L["menteri_doorstop"][1], L["jemaah_madinah"][2]]   # "Menurutnya" = Menhaj
PLAN3[13][2] = [L["madinah"][0], L["madinah"][2]]                  # Dahnil & Fadli Zon disebut
PLAN3[15][3] = [L["madinah"][1], L["hotel"][3]]                    # Harun Al Rasyid disebut
PLAN3[1][1] = [L["menteri_doorstop"][0], L["menteri_doorstop"][2]]  # "Tiga menteri..." jangan tampilkan pejabat tak dikenal

# video 16-30: rencana dari kolom vis di work7\narasi_16_30.py
import sys as _sys
_sys.path.insert(0, r"D:\newshaji\work7")
import narasi_16_30 as _n16
for _n, _v in sorted(_n16.V.items()):
    PLAN3[_n] = [pick(*row) for row in _v["vis"]]
PLAN3[7][2] = [L["menteri_doorstop"][0], L["menteri_doorstop"][1]]  # Wamenhaj Dahnil disebut: jangan wajah petugas

# 27 Okt: kalimat yang menyebut nama pejabat memakai footage pejabat itu sendiri (footage\pejabat)
_I, _D, _H = L["pj_irfan_yusuf"], L["pj_dahnil_anzar"], L["pj_harun_alrasyid"]
PLAN3[4][3] = [_I[0], _I[1]]; PLAN3[4][4] = [_I[3], _I[2]]; PLAN3[4][5] = [_I[4], _I[0]]
PLAN3[7][2] = [_D[0], _D[1]]
PLAN3[10][5] = [_I[1], _I[3]]
PLAN3[11][1] = [_I[0], _I[2]]; PLAN3[11][4] = [_I[1], _I[3]]
PLAN3[12][1] = [_I[4], _I[0]]; PLAN3[12][2] = [_I[3], _I[1]]
PLAN3[13][2] = [_D[3], _D[4]]
PLAN3[15][3] = [_H[0], _H[1]]
