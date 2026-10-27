"""Gaya video contoh (kiswah): logo biru bergaris putih, subtitle kapital 2-4 kata dengan satu kata disorot kotak biru."""
from PIL import Image, ImageDraw, ImageFilter, ImageFont

R = r"D:\newshaji"
FONT = R + r"\aset_brand\Montserrat-ExtraBold.ttf"
BIRU = (24, 112, 235)
STOP = set("dan di ke dari yang untuk dengan pada itu ini atau akan juga lebih telah sudah masih bagi oleh saat agar karena "
           "tidak belum bisa ada para sebuah setiap selama hingga kini lewat secara serta namun tetap adalah ya kamu kita "
           "sebagai sejak tersebut menurutnya mereka ia dua satu".split())


def logo_biru(out=R + r"\aset_brand\logo_biru.png"):
    src = Image.open(R + r"\aset_brand\logo_sh.png").convert("RGBA")
    pad = 16
    a = Image.new("L", (src.width + 2 * pad, src.height + 2 * pad), 0)
    a.paste(src.getchannel("A"), (pad, pad))
    grad = Image.new("RGBA", a.size)
    gd = ImageDraw.Draw(grad)
    for y in range(a.height):  # gradasi biru muda -> biru tua
        t = y / a.height
        gd.line([(0, y), (a.width, y)], fill=(int(70 - 55 * t), int(170 - 80 * t), int(255 - 30 * t), 255))
    rim = a.filter(ImageFilter.MaxFilter(9))
    shadow = rim.filter(ImageFilter.GaussianBlur(6)).point(lambda v: v * 0.45)
    img = Image.new("RGBA", a.size, (0, 0, 0, 0))
    img.paste((0, 0, 0, 255), (3, 4), shadow)
    img.paste((255, 255, 255, 255), (0, 0), rim)
    img.paste(grad, (0, 0), a)
    img.save(out)
    return out


def sorot(words):
    """indeks kata yang disorot: angka atau kata terpanjang yang bukan kata sambung"""
    bersih = [w.strip(".,?!:;\"'()").lower() for w in words]
    cand = [i for i, w in enumerate(bersih) if w and w not in STOP]
    if not cand:
        return None
    num = [i for i in cand if any(ch.isdigit() for ch in bersih[i])]
    return num[0] if num else max(cand, key=lambda i: len(bersih[i]))


def potong(disp):
    """bagi kalimat jadi potongan 2-4 kata (maks 2 baris pendek)"""
    words = disp.split(); out = []; cur = []
    for w in words:
        cur.append(w)
        n = len(" ".join(cur))
        if n >= 22 or len(cur) == 4 or (w.endswith((".", ",", "?")) and len(cur) >= 2):
            out.append(cur); cur = []
    if cur:
        if len(cur) == 1 and out and len(" ".join(out[-1] + cur)) <= 30:
            out[-1] += cur
        else:
            out.append(cur)
    return out


def gambar_sub(words, path, size=62, maxw=900):
    """PNG transparan 1080x1920 berisi potongan subtitle"""
    f = ImageFont.truetype(FONT, size)
    up = [w.upper().rstrip(",.") for w in words]
    hi = sorot(words)
    img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    sp = d.textlength(" ", font=f)
    lines = [[]]  # bungkus baris
    for i, w in enumerate(up):
        test = " ".join(up[j] for j in lines[-1] + [i])
        if lines[-1] and d.textlength(test, font=f) > maxw * 0.85:
            lines.append([])
        lines[-1].append(i)
    lh = size * 1.22; y0 = 1470 - lh * len(lines) / 2
    asc, desc = f.getmetrics()
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0)); sd = ImageDraw.Draw(sh)
    for li, line in enumerate(lines):
        wl = sum(d.textlength(up[i], font=f) for i in line) + sp * (len(line) - 1)
        x = 540 - wl / 2; y = y0 + li * lh
        for i in line:
            tw = d.textlength(up[i], font=f)
            if i == hi:
                d.rounded_rectangle((x - 12, y - 4, x + tw + 12, y + asc + 10), radius=8, fill=BIRU + (255,))
            else:
                sd.text((x + 3, y + 4), up[i], font=f, fill=(0, 0, 0, 200))
            x += tw + sp
    sh = sh.filter(ImageFilter.GaussianBlur(3))
    base = Image.alpha_composite(sh, img)
    d = ImageDraw.Draw(base)
    for li, line in enumerate(lines):
        wl = sum(d.textlength(up[i], font=f) for i in line) + sp * (len(line) - 1)
        x = 540 - wl / 2; y = y0 + li * lh
        for i in line:
            d.text((x, y), up[i], font=f, fill="white", stroke_width=1, stroke_fill=(0, 0, 0, 90) if i != hi else BIRU)
            x += d.textlength(up[i], font=f) + sp
    base.save(path)


if __name__ == "__main__":
    logo_biru()
    gambar_sub("Menariknya, penggantian kiswah bukan".split(), r"D:\newshaji\work7\ref\sub_tes.png")
