import subprocess, os, sys, json
from PIL import Image, ImageDraw, ImageFont
from narasi import V
from plan3 import PLAN3 as PLAN2
import gaya
sys.path.insert(0, r"D:\newshaji\work7")
try:
    import narasi_baru; V.update(narasi_baru.V)
    import narasi_cerita; narasi_cerita.terapkan(V)
except ImportError:
    pass

R = r"D:\newshaji"
H = R + r"\footage\haji_drive"; U = R + r"\umrah"; D = R + r"\footage\drive_clips"
import datetime
OUT = os.path.join(R, "video_harian", datetime.date.today().isoformat())
os.makedirs(OUT, exist_ok=True)
n = int(sys.argv[1])
info = V[n]
S = info["s"]
GAP = 0.3
OFF = 0.07  # frame thumbnail di awal


def dur(f):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                                capture_output=True, text=True).stdout)


def ar(k): return f"{H}\\ar_{k}.mov"
def u(k): return f"{U}\\{k}.mp4"
def dc(k): return f"{D}\\{k}.mp4"


# daftar klip bersih (tanpa orang/logo/grup Elharamain): (file, mulai)
PLAN = {
    1: [(ar("0827"), 0), (ar("0837"), 0), (dc("payung1"), 6), (ar("0846"), 0), (dc("menara_haram5"), 5), (ar("0849"), 0),
        (dc("payung2"), 5), (ar("0864"), 0), (dc("nabawi"), 8), (ar("0867"), 0), (dc("payung3"), 3), (ar("0858"), 0),
        (dc("zamzam"), 6), (ar("0840"), 0), (dc("pelataran"), 5)],
    2: [(u("u15"), 24), (u("u13"), 41), (dc("menara_haram5"), 12), (u("u02"), 0), (dc("payung1"), 18), (u("u09"), 6),
        (dc("nabawi"), 20), (u("u11"), 30), (dc("pelataran"), 3), (u("u08"), 12), (dc("payung2"), 2), (dc("zamzam"), 4),
        (u("u13"), 8), (u("u15"), 5)],
    3: [(u("u09"), 30), (dc("pelataran"), 8), (u("u11"), 6), (dc("payung3"), 1), (u("u02"), 15), (dc("nabawi"), 5),
        (u("u13"), 20), (dc("menara_haram5"), 18), (u("u15"), 40), (dc("zamzam"), 10), (u("u08"), 30), (dc("payung1"), 25),
        (u("u09"), 44)],
    4: [(ar("0846"), 0), (dc("menara_haram5"), 2), (ar("0864"), 0), (dc("payung2"), 8), (ar("0849"), 0), (dc("zamzam"), 12),
        (ar("0867"), 0), (dc("nabawi"), 15), (ar("0837"), 0), (dc("pelataran"), 11), (ar("0858"), 0), (dc("payung1"), 2),
        (ar("0870"), 0), (dc("menara_haram5"), 20)],
    5: [(dc("menara_haram5"), 8), (dc("payung1"), 10), (dc("nabawi"), 2), (ar("0840"), 0), (dc("payung3"), 6),
        (dc("pelataran"), 2), (ar("0827"), 0), (dc("payung2"), 0), (dc("zamzam"), 0), (ar("0852"), 0), (dc("nabawi"), 28),
        (u("u08"), 12), (dc("menara_haram5"), 22), (u("u13"), 8)],
    6: [(ar("0827"), 0), (ar("0852"), 0), (ar("0837"), 0), (ar("0855"), 0), (ar("0870"), 0), (ar("0846"), 0),
        (dc("payung1"), 14), (ar("0849"), 0), (ar("0858"), 0), (ar("0864"), 0), (ar("0867"), 0), (ar("0840"), 0),
        (dc("payung2"), 10), (ar("0829"), 0)],
}

PLAN = {k: [p for p in v if not p[0].endswith(("ar_0827.mov", "ar_0837.mov")) and not p[0].startswith(U)] for k, v in PLAN.items()}
work = f"b{n}"; os.makedirs(work + "/cuts", exist_ok=True)
wavs = [f"seg/v{n}_{i}.wav" for i in range(len(S))]
durs = [dur(w) for w in wavs]
total = sum(durs) + GAP * len(S)
print("durasi narasi", round(total, 1))
assert total + OFF <= 60, "lebih dari 60 detik"

# audio
cmd = ["ffmpeg", "-v", "error", "-y"] + sum([["-i", w] for w in wavs], []) + ["-filter_complex",
    "".join(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono,apad=pad_dur={GAP}[p{k}];" for k in range(len(S))) +
    "".join(f"[p{k}]" for k in range(len(S))) + f"concat=n={len(S)}:v=0:a=1[a]", "-map", "[a]", f"{work}/narr.wav"]
subprocess.run(cmd, check=True)

# visual: tiap kalimat memakai klip yang sesuai isinya (plan2.py)
FC = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,format=yuv420p,setsar=1"
ENC = ["-an", "-c:v", "libx264", "-crf", "17", "-preset", "fast", "-r", "30"]
assert len(PLAN2[n]) == len(S), "jumlah baris rencana != jumlah kalimat"
cuts = []; k = 0; shots = []; t_acc = OFF  # shots: catatan klip per kalimat untuk cek.py
for i, row in enumerate(PLAN2[n]):
    span = durs[i] + GAP + (0.2 if i == len(S) - 1 else 0)
    for j, c in enumerate(row):
        d = span / len(row)
        out = f"{work}/cuts/c{k:02d}.mp4"; F = int(round(d * 30))
        if c[0] == "w":  # foto: gerak Ken Burns pelan
            img, mode = f"aset/w_{c[1]}.jpg", c[2]
            zp = f"zoompan=z='1+0.08*on/{F}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={F}:s=1080x1920:fps=30"
            if mode == "fit":  # utuh (bagian depan uang) di atas latar blur
                vf = (f"[0:v]crop=iw:ih/2:0:0,split[a][b];[a]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,"
                      f"boxblur=40:2,eq=brightness=-0.15[bg];[b]scale=2000:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,{zp},format=yuv420p,setsar=1")
            else:  # top: crop 9:16 condong ke atas (wajah)
                vf = f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840:(iw-ow)/2:(ih-oh)*0.25,{zp},format=yuv420p,setsar=1"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", img, "-filter_complex", vf, "-frames:v", str(F)] + ENC + [out], check=True)
        elif c[0] == "k":  # kanal Kemenhaj: ambil 900 baris atas (buang subtitle tertanam), potong 9:16
            ch = {"k_GZpfBF3LObw": 800}.get(c[1], 900)  # video lansia: subtitle 2-3 baris naik sampai ~baris 860
            vf = (f"crop=1920:{ch}:0:0,scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*{c[3]}:0,"
                  "fps=30,format=yuv420p,setsar=1")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{c[2]:.2f}", "-i", rf"{R}\footage\kemenhaj\{c[1]}.mp4",
                            "-frames:v", str(F), "-vf", vf] + ENC + [out], check=True)
        elif c[0] == "j":  # footage pejabat: ambil c[4] baris teratas (buang subtitle), potong 9:16 di posisi x
            vf = (f"crop=iw:{c[4]}:0:0,scale=-2:1920:flags=lanczos,crop=1080:1920:(iw-1080)*{c[3]}:0,"
                  "fps=30,format=yuv420p,setsar=1")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{c[2]:.2f}", "-i", c[1], "-frames:v", str(F), "-vf", vf] + ENC + [out], check=True)
        elif c[0] == "s":  # footage Saudi vertikal: mulai di detik yang sudah dicek
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{c[2]:.2f}", "-i", c[1], "-frames:v", str(F), "-vf", FC] + ENC + [out], check=True)
        else:
            f = f"aset/p{c[1]}.mp4" if c[0] == "p" else c[1]
            avail = dur(f)
            st = min(1.5 + 2.0 * (k % 3), max(0, avail - d - 0.1))  # hindari detik awal yang sering kosong
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-ss", f"{st:.2f}", "-i", f, "-frames:v", str(F), "-vf", FC] + ENC + [out], check=True)
        cuts.append(out); shots.append(dict(kal=i, mulai=round(t_acc, 2), durasi=round(F / 30, 2), sumber=str(c[:3])))
        t_acc += F / 30; k += 1
json.dump(shots, open(f"{work}/shots.json", "w"))
open(f"{work}/list.txt", "w").write("".join(f"file 'cuts/{os.path.basename(c)}'\n" for c in cuts))
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{work}/list.txt", "-c", "copy", f"{work}/visual.mp4"], check=True)

# thumbnail dari template Canva
# detik frame thumbnail; default 1.0, diganti bila klip pembuka sama dengan video lain
THUMB_T = {5: 41, 12: 13.5, 13: 28.5, 14: 5}
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(THUMB_T.get(n, 1.0)), "-i", f"{work}/visual.mp4", "-frames:v", "1", f"{work}/frame.png"], check=True)
tpl = Image.open(R + r"\aset_brand\canva_template.png").convert("RGB")
ph = Image.open(f"{work}/frame.png").convert("RGB")
w, h = ph.size; sc = max(1080 / w, 1170 / h)
ph = ph.resize((int(w * sc), int(h * sc)), Image.LANCZOS)
ph = ph.crop(((ph.width - 1080) // 2, (ph.height - 1170) // 2, (ph.width - 1080) // 2 + 1080, (ph.height - 1170) // 2 + 1170))
img = Image.new("RGB", (1080, 1920), "white")
img.paste(ph, (0, 0))
img.paste(tpl.crop((0, 600, 1080, 1350)), (0, 1170))
# kotak putih berisi teks: bersihkan placeholder "isi berita" lalu tulis ulang
dr = ImageDraw.Draw(img)
dr.rectangle((80, 1412, 960, 1684), fill="white")
t1, t2, t3 = info["thumb"]
def fit(txt, path, size, maxw):
    while size > 20:
        f = ImageFont.truetype(path, size)
        if dr.textlength(txt, font=f) <= maxw: return f
        size -= 2
    return f
BOLD = r"C:\Windows\Fonts\arialbd.ttf"; REG = r"C:\Windows\Fonts\arial.ttf"
for txt, path, size, color, y in ((t1, BOLD, 58, (20, 80, 190), 1496), (t2, BOLD, 38, (30, 110, 210), 1575), (t3, BOLD, 32, (90, 90, 90), 1630)):
    f = fit(txt, path, size, 820)
    dr.text((520 - dr.textlength(txt, font=f) / 2, y - f.size / 2), txt, font=f, fill=color)
img.save(f"{work}/thumb.png")
img.convert("RGB").save(f"{work}/thumb.jpg", quality=92)

# subtitle gaya contoh kiswah: potongan 2-4 kata kapital, satu kata disorot kotak biru (gaya.py)
os.makedirs(f"{work}/sub", exist_ok=True)
Image.new("RGBA", (1080, 1920), (0, 0, 0, 0)).save(f"{work}/sub/kosong.png")
seq = [("kosong.png", OFF)]; m = 0
for i, (disp, _) in enumerate(S):
    chunks = gaya.potong(disp)
    tot = sum(len(" ".join(c)) for c in chunks)
    for c in chunks:
        gaya.gambar_sub(c, f"{work}/sub/s{m:03d}.png")
        seq.append((f"s{m:03d}.png", durs[i] * len(" ".join(c)) / tot)); m += 1
    seq.append(("kosong.png", GAP))
open(f"{work}/sub/list.txt", "w").write("".join(f"file '{f}'\nduration {d:.3f}\n" for f, d in seq) + "file 'kosong.png'\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{work}/sub/list.txt",
                "-vf", "fps=30,format=rgba", "-c:v", "png", f"{work}/sub.mov"], check=True)

# render akhir: frame thumbnail + visual + subtitle + logo + suara (+ musik latar bila ada aset_brand\musik.mp3)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-t", f"{OFF}", "-i", f"{work}/thumb.png",
                "-vf", "scale=1080:1920,format=yuv420p,setsar=1", "-c:v", "libx264", "-crf", "17", f"{work}/first.mp4"], check=True)
open(f"{work}/list2.txt", "w").write("file 'first.mp4'\nfile 'visual.mp4'\n")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", f"{work}/list2.txt", "-c:v", "libx264", "-crf", "17", "-preset", "fast", f"{work}/full_visual.mp4"], check=True)
MUSIK = R + r"\aset_brand\musik.mp3"
fc = (f"[0:v]eq=contrast=1.04:saturation=1.1[v0];[v0][3:v]overlay=0:0:eof_action=pass[v1];"
      f"[1:v]scale=400:-1[lg];[v1][lg]overlay=(W-w)/2:80:enable='gte(t,{OFF})',format=yuv420p[v];"
      f"[2:a]adelay={int(OFF*1000)}:all=1,loudnorm=I=-16:TP=-1.5[nr]")
ins = ["-i", f"{work}/full_visual.mp4", "-i", R + r"\aset_brand\logo_biru.png", "-i", f"{work}/narr.wav", "-i", f"{work}/sub.mov"]
if os.path.exists(MUSIK):
    ins += ["-stream_loop", "-1", "-i", MUSIK]
    fc += f";[4:a]volume=0.12,afade=t=out:st={total + OFF - 2:.2f}:d=2[bg];[nr][bg]amix=inputs=2:duration=first:normalize=0[a]"
else:
    fc += ";[nr]anull[a]"
mid = f"{work}/mid.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y"] + ins + ["-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-t", f"{total + OFF:.2f}",
                "-movflags", "+faststart", mid], check=True)
final = f"{OUT}\\Video_{n}_{info['slug']}.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mid, "-i", f"{work}/thumb.jpg", "-map", "0", "-map", "1", "-c", "copy",
                "-disposition:v:1", "attached_pic", "-movflags", "+faststart", final], check=True)
img.save(f"{OUT}\\Thumbnail_{n}_{info['slug']}.png")
open(f"{OUT}\\caption_{n}.txt", "w", encoding="utf-8").write(info["cap"])
open(f"{OUT}\\narasi_{n}.txt", "w", encoding="utf-8").write("\n".join(d for d, _ in S))
print("SELESAI", final, round(total + OFF, 1))

