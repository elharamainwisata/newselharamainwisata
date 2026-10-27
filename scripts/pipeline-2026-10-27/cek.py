"""Lembar cek setelah render: tiap klip diambil frame awal/tengah/akhir dari video jadi.
Kalimat yang menyebut pejabat diberi bingkai merah -> wajib dipastikan tidak ada wajah orang lain,
teks nama tertanam, atau mik berlogo TV.  Pakai: python cek.py N  -> cek\\vN.jpg"""
import json, os, subprocess, sys, glob
from PIL import Image, ImageDraw, ImageFont
from narasi import V
sys.path.insert(0, r"D:\newshaji\work7")
import narasi_baru; V.update(narasi_baru.V)
import narasi_cerita; narasi_cerita.terapkan(V)

import re
_PJ = re.compile(r"\b(menteri|menhaj|wamenhaj|dirjen|direktur|kepala|irfan|dahnil|harun|rudy|fadli|al-rabiah|rabiah)\b", re.I)
def cocok(teks): return bool(_PJ.search(teks))
n = int(sys.argv[1])
video = glob.glob(rf"D:\newshaji\video_harian\*\Video_{n}_*.mp4")
video = max(video, key=os.path.getmtime)
shots = json.load(open(f"b{n}/shots.json"))
S = V[n]["s"]
os.makedirs("cek", exist_ok=True)
f = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 15)
W, H = 120, 213
rows = []
for j, s in enumerate(shots):
    fr = []
    for p in (0.15, 0.5, 0.9):
        t = s["mulai"] + s["durasi"] * p
        out = f"cek/_f.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", video, "-frames:v", "1", "-vf", f"scale={W}:{H}", out], check=True)
        fr.append(Image.open(out).copy())
    rows.append((s, fr))
os.remove("cek/_f.png")
per = 4  # klip per baris
img = Image.new("RGB", (per * (3 * W + 12), ((len(rows) + per - 1) // per) * (H + 40)), "white")
d = ImageDraw.Draw(img)
for j, (s, fr) in enumerate(rows):
    x0 = (j % per) * (3 * W + 12); y0 = (j // per) * (H + 40)
    teks = S[s["kal"]][0]
    nama = cocok(teks)
    if nama:
        d.rectangle((x0, y0, x0 + 3 * W + 8, y0 + H + 38), fill=(220, 30, 30))
    for m, im in enumerate(fr):
        img.paste(im, (x0 + 4 + m * W, y0 + 4))
    d.text((x0 + 4, y0 + H + 6), f"K{s['kal'] + 1} {teks[:46]}", font=f, fill="white" if nama else "black")
img.save(f"cek/v{n}.jpg", quality=88)
print("cek", f"cek/v{n}.jpg", "klip", len(rows), "kalimat-nama", sum(cocok(S[s['kal']][0]) for s, _ in rows))
