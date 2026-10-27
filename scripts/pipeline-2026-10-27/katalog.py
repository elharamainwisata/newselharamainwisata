# file relatif ke D:\newshaji\footage\pejabat ; t = detik mulai ; dur = detik bersih ; x = posisi crop 0..1 ; crop = "top900" (default Kemenhaj 1920x1080) atau keterangan lain
#
# CATATAN crop:
#   "topN" = ambil N baris teratas frame sumber (bukan 900), lalu scale ke tinggi 1920 dan crop 1080 lebar di posisi x.
#   top780 / top760 / top740 dipakai pada video bersubtitle burn-in (subtitle Kemenhaj/BPKH ada di y~790-890,
#   jadi top900 standar AKAN memuat subtitle). Renderer harus memakai nilai topN ini, bukan 900.
#   dahnil_anzar_JPLFqYL13Dc.mp4 berukuran 1920x1072 (top740).
#   irfan_yusuf_pzxkySlOHGs.mp4 berukuran 1280x720 (top600 = setara top900 pada 1080p).
#   File *_sNNNN.mp4 = potongan (download-sections) mulai detik NNNN dari video asli; t relatif ke file potongan.
#   Filter ffmpeg: crop=iw:N:0:0,scale=-2:1920,crop=1080:1920:(iw-1080)*X:0
PEJABAT = {
  "irfan_yusuf": {"nama": "Mochamad Irfan Yusuf", "jabatan": "Menteri Haji dan Umrah RI", "adegan": [
    {"file": "irfan_yusuf_FjBmi-piLxs.mp4", "t": 40.0, "dur": 6.0, "x": 0.50, "crop": "top780", "ket": "pesan video Hari Khidmat Haji dan Umrah, latar putih, close-up bicara ke kamera (yt FjBmi-piLxs)"},
    {"file": "irfan_yusuf_EbXVf_yWFvM.mp4", "t": 20.0, "dur": 6.0, "x": 0.526, "crop": "top780", "ket": "pesan ajakan Sensus Ekonomi 2026, jas hitam dasi kupu-kupu, ruang kerja (yt EbXVf_yWFvM)"},
    {"file": "irfan_yusuf_P0fCwLr9OVg_s2435.mp4", "t": 14.0, "dur": 5.0, "x": 0.487, "crop": "top900", "ket": "pidato di podium, Pembukaan Rakernas Evaluasi Haji 2026, seragam krem + topi; nametag 'Dr. KH. M. IRFAN' (yt P0fCwLr9OVg @2449s)"},
    {"file": "irfan_yusuf_L8UYIfFKJ6M_s5198.mp4", "t": 5.0, "dur": 6.0, "x": 0.48, "crop": "top900", "ket": "sambutan di podium, Doa & Zikir Hari Khidmat + launching Hotline Bongkar Mafia Haji (yt L8UYIfFKJ6M @5203s); ada logo Kemenhaj kecil di pojok atas"},
    {"file": "fadlul_imansyah_HP3iEhpEjt8.mp4", "t": 51.5, "dur": 6.0, "x": 0.50, "crop": "top760", "pakai": False, "ket": "TIDAK DIPAKAI: gambar terlalu buram (cek 27 Okt). close-up pidato di BPKH Annual Meeting & Hajj Banking Award 2025, baju koko coklat; lower-third 'KH. Mochamad Irfan Yusuf Hasyim, Menteri Haji dan Umrah RI' di detik 44-48 (kanal BPKH)"},
    {"file": "fadlul_imansyah_HP3iEhpEjt8.mp4", "t": 60.2, "dur": 4.0, "x": 0.41, "crop": "top760", "ket": "sudut samping di podium BPKH Annual Meeting 2025 (acara sama dgn adegan sebelumnya, sudut berbeda)"},
    {"file": "irfan_yusuf_pzxkySlOHGs.mp4", "t": 2.5, "dur": 3.0, "x": 0.608, "crop": "top600", "ket": "berjalan/tersenyum menyambut tamu, pertemuan dengan Menkes Budi Gunadi Sadikin, kemeja putih (sumber 1280x720)"},
  ]},
  "dahnil_anzar": {"nama": "Dahnil Anzar Simanjuntak", "jabatan": "Wakil Menteri Haji dan Umrah RI", "adegan": [
    {"file": "dahnil_anzar_oO_gW-RoSxc.mp4", "t": 40.0, "dur": 6.0, "x": 0.506, "crop": "top780", "ket": "pesan Hari Khidmat, kemeja batik, latar dinding bata (yt oO_gW-RoSxc)"},
    {"file": "dahnil_anzar_IKJ5Q_ZKbYQ.mp4", "t": 45.0, "dur": 6.0, "x": 0.50, "crop": "top780", "ket": "pernyataan resmi soal eskalasi konflik Timur Tengah, baju putih, latar oranye; lower-third nama di detik 0-3"},
    {"file": "dahnil_anzar_JPLFqYL13Dc.mp4", "t": 295.0, "dur": 6.0, "x": 0.458, "crop": "top740", "ket": "pernyataan usai kecelakaan bus Jabal Magnet, jas biru dasi kupu-kupu (sumber 1920x1072)"},
    {"file": "dahnil_anzar_W3nGeLcEtiM_s1495.mp4", "t": 20.0, "dur": 6.0, "x": 0.554, "crop": "top900", "ket": "pidato di podium, Penutupan Rakernas Evaluasi Haji 2026, jas krem, close-up (yt W3nGeLcEtiM @1515s)"},
    {"file": "dahnil_anzar_W3nGeLcEtiM_s2195.mp4", "t": 12.0, "dur": 6.0, "x": 0.459, "crop": "top900", "ket": "pidato di podium Penutupan Rakernas, shot medium dengan gestur tangan (yt W3nGeLcEtiM @2207s)"},
    {"file": "dahnil_anzar_L8UYIfFKJ6M_s3410.mp4", "t": 5.0, "dur": 6.0, "x": 0.473, "crop": "top900", "ket": "sambutan di podium Hari Khidmat, jas abu dasi kupu-kupu merah (yt L8UYIfFKJ6M @3415s); logo Kemenhaj kecil di pojok atas"},
    {"file": "dahnil_anzar_kWguDWHwyvo_s385.mp4", "t": 30.5, "dur": 4.5, "x": 0.391, "crop": "top900", "ket": "presentasi alokasi kuota haji, close-up depan layar biru (yt kWguDWHwyvo @415s); ada jump-cut antar sudut"},
    {"file": "dahnil_anzar_kWguDWHwyvo_s1058.mp4", "t": 12.5, "dur": 4.0, "x": 0.554, "crop": "top900", "ket": "presentasi alokasi kuota, close-up latar abu (yt kWguDWHwyvo @1070s)"},
    {"file": "dahnil_anzar_kWguDWHwyvo_s1330.mp4", "t": 6.0, "dur": 5.0, "x": 0.432, "crop": "top900", "ket": "presentasi alokasi kuota, close-up latar heksagon hijau (yt kWguDWHwyvo @1336s)"},
  ]},
  "harun_alrasyid": {"nama": "Harun Al Rasyid", "jabatan": "Direktur Jenderal Pengendalian Haji dan Umrah, Kemenhaj", "adegan": [
    {"file": "harun_alrasyid_he1ku1a-gjs_s2112.mp4", "t": 27.0, "dur": 6.0, "x": 0.617, "crop": "top900", "ket": "bicara berdiri dengan mikrofon, Diskusi Panel 2 Rakernas Konsolidasi 2026; layar panggung menampilkan nama+foto 'Dr. H. Harun Al Rasyid' tepat sebelum (yt he1ku1a-gjs @2139s)"},
    {"file": "harun_alrasyid_he1ku1a-gjs_s2280.mp4", "t": 8.0, "dur": 6.0, "x": 0.581, "crop": "top900", "ket": "lanjutan paparan, shot lebih rapat (yt he1ku1a-gjs @2288s)"},
  ]},
  "puji_raharjo": {"nama": "Puji Raharjo", "jabatan": "Direktur Jenderal Bina Penyelenggaraan Haji dan Umrah, Kemenhaj", "adegan": [
    {"file": "puji_raharjo_8RcHOY7W_0k_s395.mp4", "t": 10.5, "dur": 6.0, "x": 0.595, "crop": "top900", "ket": "bicara duduk di sofa panel, jas hitam; slide biodata 'Puji Raharjo - Direktur Jenderal Bina PHU' dgn foto ditampilkan di sesi yang sama (yt 8RcHOY7W_0k @405s)"},
    {"file": "puji_raharjo_8RcHOY7W_0k_s395.mp4", "t": 28.0, "dur": 6.0, "x": 0.432, "crop": "top900", "ket": "panel Rakernas, sudut frontal (yt 8RcHOY7W_0k @423s)"},
  ]},
  "jaenal_effendi": {"nama": "Jaenal Effendi", "jabatan": "Direktur Jenderal Pengembangan Ekosistem Ekonomi Haji dan Umrah, Kemenhaj", "adegan": [
    {"file": "dirjen_pehu_he1ku1a-gjs_s610.mp4", "t": 13.0, "dur": 5.0, "x": 0.418, "crop": "top900", "ket": "bicara duduk di panel, jas abu; layar menampilkan nama+foto 'Prof. Dr. Rer nat Jaenal Effendi' di detik 6-10 file ini (yt he1ku1a-gjs @623s)"},
    {"file": "dirjen_pehu_he1ku1a-gjs_s610.mp4", "t": 40.0, "dur": 6.0, "x": 0.418, "crop": "top900", "ket": "lanjutan panel, latar teks layar (yt he1ku1a-gjs @650s)"},
  ]},
  "fadlul_imansyah": {"nama": "Fadlul Imansyah", "jabatan": "Kepala Badan Pelaksana BPKH", "adegan": [
    {"file": "fadlul_imansyah_HP3iEhpEjt8.mp4", "t": 22.0, "dur": 6.0, "x": 0.371, "crop": "top760", "ket": "sambutan di podium BPKH Annual Meeting & Hajj Banking Award 2025, baju merah; lower-third 'Fadlul Imansyah, Kepala Badan Pelaksana BPKH RI' di detik 16-20 (kanal BPKH)"},
  ]},
  "tawfiq_rabiah": {"nama": "Tawfiq bin Fawzan Al-Rabiah", "jabatan": "Menteri Haji dan Umrah Arab Saudi", "adegan": [
    {"file": "tawfiq_rabiah_-ePBbZEny2E.mp4", "t": 26.5, "dur": 4.5, "x": 0.473, "crop": "top900", "ket": "pidato di podium Konferensi Pers Pemerintah (Mei 2025), latar foto Ka'bah; kanal resmi Kementerian Haji Saudi"},
    {"file": "tawfiq_rabiah_nNFI1YexCh8.mp4", "t": 18.0, "dur": 7.0, "x": 0.432, "crop": "top900", "ket": "pidato acara 'Khitamuhu Misk' penutupan musim haji 1446, close-up samping"},
    {"file": "tawfiq_rabiah_nNFI1YexCh8.mp4", "t": 100.0, "dur": 6.0, "x": 0.459, "crop": "top900", "ket": "acara sama, shot lebar di podium dengan bendera Saudi"},
  ]},
}
