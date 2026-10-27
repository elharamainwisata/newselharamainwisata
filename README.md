# News Elharamain Wisata - reels berita haji & umrah

Video reels Instagram/TikTok/Threads/X untuk @newselharamainwisata (news.elharamainwisata.com).

## berita-2026-10-26
Tiga video (maks 60 detik, 1080x1920) beserta thumbnail dan teks narasi:

1. Dua Tahun Pembenahan Haji
2. Konferensi Haji Keenam di Jeddah dan Paket All-Inclusive 2027
3. Umrah Terhalang: Ihshar, Tahallul, dan Hadyu

Thumbnail sudah tertanam sebagai frame pertama dan cover tiap video.

## berita-2026-10-27
Tiga puluh video (maks 60 detik, 1080x1920) gaya narasi bercerita, subtitle kapital dengan sorotan biru, dan logo NEWS biru. Tiap video dilengkapi thumbnail, caption, dan narasi. Daftar video ada di `CATATAN.txt` dan sumber berita (diutamakan situs resmi pemerintah) di `sumber.txt`.

## scripts
Skrip ffmpeg/Python yang dipakai: menyusun potongan footage (`bv.py`), transkripsi kata per kata (`trw.py`), membuat subtitle .ass dari naskah (`mkass2.py`), dan render akhir dengan logo dan suara (`fin.py`).

`scripts/pipeline-2026-10-27` berisi pipeline batch 27 Okt: suara dari Voice Studio (`tts.py`), naskah (`narasi_*.py`), rencana footage per kalimat (`plan3.py`, `katalog.py`, `saudi_sel.json`), gaya subtitle dan logo (`gaya.py`), render (`build2.py N`), dan lembar cek per klip (`cek.py N`).

Aturan produksi: footage hanya dari Drive sendiri, tanpa teks sumber di video, penutup suara "News Elharamain Wisata".
