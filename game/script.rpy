#character
#prolog
#adegan 0
image lead netral = ConditionSwitch(
    "gender == 'm'", "Prolog/Prolog/Adegan 0/1. MC (m) netral.png",
    "gender == 'f'", "Prolog/Prolog/Adegan 0/1. MC (f) netral.png",
)
image lead liat made = ConditionSwitch(
    "gender == 'm'", "Prolog/Prolog/Adegan 0/2. MC (m) setelah liat pemiliknya made.png",
    "gender == 'f'", "Prolog/Prolog/Adegan 0/2. MC (f) setelah liat pemiliknya made.png",
)

#adegan 1
image raras wah = "Prolog/Prolog/Adegan 1/1. Raras, saat _wahh.._.png"
image lead ehh = ConditionSwitch(
    "gender == 'm'", "Prolog/Prolog/Adegan 1/2. MC (m) saat _Ehh iya_.png",
    "gender == 'f'", "Prolog/Prolog/Adegan 1/2. MC (f) saat _Ehh iya_.png",
)


#adegan 2
image made nyambut mc = "Prolog/Prolog/Adegan 2/1. Made, menyambut MC.png"
image lead ngobrol made = ConditionSwitch(
    "gender == 'm'", "Prolog/Prolog/Adegan 2/2. MC (m) saat ngobrol sama made.png",
    "gender == 'f'", "Prolog/Prolog/Adegan 2/2. MC (f) saat ngobrol sama made.png",
)

#dialog 1 (tolak bantu)
#scene 1
image made kecewa = "Dialog/Dialog 1 (tolak membantu)/Scene 1/1. Made kecewa.png"
image lead diem = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 1/2. MC (m)_.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 1/2. MC (f) .png",
)
image raden bangga = "Dialog/Dialog 1 (tolak membantu)/Scene 1/3. Raden bangga.png"

#scene 2 latar berubah
image lead taxnet = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 2 (latar berubah)/1. MC (m) melihat TAXNET.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 2 (latar berubah)/1. MC (f) melihat taxnet.png",
)
image raras shock ="Dialog/Dialog 1 (tolak membantu)/Scene 2 (latar berubah)/2. Raras shock.png"

#scene 3 nyelamatin raras
#scene 3.1 
image raras lega = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/scene 3.1/1. Raras lega.png"
image lead senang = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/scene 3.1/2. MC (m) Senang .png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/scene 3.12. MC (f) Senang.png",
)
#scene 3.2 dipanggil raden
image raden memanggil = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/1. Raden memanggil MC.png"
image lead menghadap raden = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/2. MC (m) menghadap raden.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/2. MC (f) menghadap raden.png",
)
#jujur
image lead jujur = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/jujur/1. MC (m) jujur.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/jujur/1. MC (f) jujur.png",
)
image raras akhir = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/jujur/2. Raras, pesan akhir.png"
image lead dipindah = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/jujur/3. MC (m) dipindahkan.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/jujur/3. MC (f) dipindahkan.png",
)

#bantah
#berdebat
image lead debat raden = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/1. MC (m) debat sama raden.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/1. MC (f) debat sama raden.png",
)
image raden berdebat = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/2. Raden berdebat.png"
image lead lampu merah = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/3. MC (m) setelah lampu nyala.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/3. MC (f) setelah lampu ruangan merah.png",
)
image raden lampu merah = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/1. berdebat/4. Raden setelah lampu ruangan merah.png"

#latar malam  
image lead liat liat nama raden = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/1. MC (m) Melihat nama raden .png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/1. MC (f) melihat nama raden.png",
)
image raden jangan bodoh = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/2. Raden _Jangan bodoh_.png"
image lead ketauan = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/3. MC (m) ketahuan.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/3. MC (f) ketahuan.png",
)
image raden senyum tipis = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/4. Raden senyum tipis.png"
image raden mergokin mc = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/5. Raden memergoki MC.png"
image raden keluarin pistol = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/6. Raden mengeluarkan pistol.png"
image lead berhasil upload = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/7. MC (m) berhasil mengupload.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/2. latar malam/7. MC (f) berhasil mengupload.png",
)

#epilog 
image raras baca berita = "Dialog/Dialog 1 (tolak membantu)/Scene 3 (Menyelamatkan Raras)/Scene 3.2 (dipanggil Raden Bagus)/bantah/3. Epilog/Raras membaca berita.png"


#scene 3 tidak nyelamatin
#image raden bangga ada di sblmnya
image lead senyum bahagia = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 4 (Tidak menyelamatkan Raras)/2. MC (m).png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 4 (Tidak menyelamatkan Raras)/2. MC (f).png",
)
image lead kantor baru = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 1 (tolak membantu)/Scene 4 (Tidak menyelamatkan Raras)/3. MC (m) di kantor baru.png",
    "gender == 'f'", "Dialog/Dialog 1 (tolak membantu)/Scene 4 (Tidak menyelamatkan Raras)/3. MC (f) di kantor baru.png",
)


#dialog 2
#scene 1
image made puas = "Dialog/Dialog 2 (setuju membantu)/Scene 1/1. Made puas.png"
image lead senyum = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 2 (setuju membantu)/Scene 1/2. MC (m).png",
    "gender == 'f'", "Dialog/Dialog 2 (setuju membantu)/Scene 1/2. MC (f).png",
)

#scene 2
image raras tanya = "Dialog/Dialog 2 (setuju membantu)/scene 2/1. Raras bertanya-tanya.png"
image lead ngobrol sama raras = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 2 (setuju membantu)/scene 2/2. MC (m) ngobrol sama raras.png",
    "gender == 'f'", "Dialog/Dialog 2 (setuju membantu)/scene 2/2. MC (f) ngobrol sama raras .png",
)

#scene 3 ngaku dan bocorin data
image lead senyum kesal = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 2 (setuju membantu)/scene 3 (mengaku dan membocorkan data)/MC (m).png",
    "gender == 'f'", "Dialog/Dialog 2 (setuju membantu)/scene 3 (mengaku dan membocorkan data)/MC (f).png",
)
image raden kesal = "Dialog/Dialog 2 (setuju membantu)/scene 3 (mengaku dan membocorkan data)/Raden.png"

#scene 3 nutupi bukti
#raden bangga ada di sblmnya
image raras masih ingat = "Dialog/Dialog 2 (setuju membantu)/scene 3 (menutupi bukti)/2. Raras _kamu masih ingat.._.png"
image lead bingung = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 2 (setuju membantu)/scene 3 (menutupi bukti)/MC (m).png",
    "gender == 'f'", "Dialog/Dialog 2 (setuju membantu)/scene 3 (menutupi bukti)/MC (f).png",
)


#dialog 3
#scene 1
image made sedikit lega = "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 1/Made sedikit lega.png"
image lead madenya sedikit lega = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 1/MC (m).png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 1/MC (f) .png",
)

#scene 2 lapor ke raden
#raden bangga ada di sblmnya
#f senyum ada di sblmnya
#m senyum ada di sblmnya

#scene 3 ruangan baru
image lead kaget = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 3 ruangan baru/1. MC (m) _selamat datang_.png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 3 ruangan baru/1. MC (f) _selamat datang.._.png",
)
image raras bingung = "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 3 ruangan baru/2. Raras.png"
image lead maksudnya = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 3 ruangan baru/3. MC (m) _Maksudnya.._.png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 3 ruangan baru/3. MC (f) _Maksudnya.png",
)

#scene 4 mematikan sistem
image lead sinis = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (mematikan sistem)/MC (m).png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (mematikan sistem)/MC (f) .png",
)


#scene 4 membiarkan berjalan
image lead diam = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (membiarkan berjalan)/1. MC (m) diam.png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (membiarkan berjalan)/1. MC (f) diam.png",
)
image raden memuji = "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (membiarkan berjalan)/2. Raden memuji.png"
image lead tatapan kosong = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (membiarkan berjalan)/4. MC (m) tatapan kosong.png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (membiarkan berjalan)/4. MC (f) tatapan kosong.png",
)
#f senyum bahagia ada di sebelumnya
#m senyum bahagia ada di sebelumnya

#scene 4 mengambil alih taxnet
image raden agak kesal = "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (mengambil alih taxnet)/1.Raden.png"
image lead gantiin Tuhan = ConditionSwitch(
    "gender == 'm'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (mengambil alih taxnet)/3. MC (m) menggantikan tuhan.png",
    "gender == 'f'", "Dialog/Dialog 3 (Ragu-ragu membantu made)/scene 4 (mengambil alih taxnet)/3. MC (f) menggantikan tuhan.png",
)
#f menghadap raden ada di sblmnya
#m menghadap raden ada di sblmnya


#BG
#prolog
image bg prolog_0 = "BG/Gambar Background/ADEGAN 0/PROLOG/Salinan ADEGAN 0.png"
image bg prolog_1 = "BG/Gambar Background/ADEGAN 0/PROLOG/Salinan ADEGAN 1.png"
image bg prolog_2 = "BG/Gambar Background/ADEGAN 0/PROLOG/Salinan ADEGAN 2.png"

#pilihan dialog 1
image cafe raras = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/Cafe bertemu dengan Raras.png"
image ruang kerja mc = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/Ruang kerja Pemeran utama.png"
image ruang raden = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/Ruang kerja Raden.png"
image ruang rapat bersama = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/Ruang rapat bersama Made.png"

#A nyelamatin raras
image ruang mc pagi = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/Ruang kerja pemeran utama (pagi).png"
image ruang rapat = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/Ruang rapat.png"
#pilihan 1 jujur
image diusir raden = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/PILIHAN 1 (JUJUR)/Setelah di usir oleh Raden.png"
#pilihan 2 menentang
image meja kerja raras = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/PILIHAN  2 (MEMBANTAH DAN MENENTANG RADEN)/Epilog (meja kerja Raras).png"
image ruang rapat alarm = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/PILIHAN  2 (MEMBANTAH DAN MENENTANG RADEN)/Ruang rapat (alarm berbunyi).png"
image ruang rapat kembali pulih = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/A (MENYELAMATKAN RARAS)/PILIHAN  2 (MEMBANTAH DAN MENENTANG RADEN)/Ruang Rapat (suasana kembali pulih).png"

#B tidak nyelamatin
image ruang kerja baru = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/B (TIDAK MENYELAMATKAN RARAS)/Ruang kerja baru pemain utama.png"
image ruang kerja lama = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 1/B (TIDAK MENYELAMATKAN RARAS)/Ruang kerja lama pemain utama.png"


#pilihan dialog 2
#cafe, ruang kerja ada di sblmnya

#A menutup bukti
image ruang kerja mc suram = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/A (MENUTUPI BUKTI)/Ruang kerja pemeran utama (suram)_.png"
image ruang kerja baru mc suram = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/A (MENUTUPI BUKTI)/Ruang kerja pemeran utama naik jabatan (suram).png"
image tampilan pencoretan = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/A (MENUTUPI BUKTI)/Tampilan layar saat pencoretan.png"

#B ngaku, bocorin
image alarm bunyi = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/B (MENGAKU DAN MEMBOCORKAN DATA)/Alarm berbunyi.png"
image kondisi hancur = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/B (MENGAKU DAN MEMBOCORKAN DATA)/Kondisi global setelah hancur.png"
#ruang kerja mc suram ada di atas

#C hancurin
image kondisi dunia reset = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/C (MENGHANCURKAN TAXNET)/Kondisi dunia yang damai setelah reset.png"
image kondisi internet padam = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 2/C (MENGHANCURKAN TAXNET)/Kondisi kota setelah akses internet padam.png"

#pilihan dialog 3
image ruang kerja malam = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/Ruang kerja pemeran utama saat mengecek data (malam hari).png"
image ruang rapat made = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/Ruang rapat bersama Made.png"
image ruang baru = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/ruangan baru.png"

#A
image dunia damai = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/A (MEMATIKAN SISTEM)/Dunia damai walaupun chaos.png"
image komputer runtuh = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/A (MEMATIKAN SISTEM)"
image kota chaos = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/A (MEMATIKAN SISTEM)/Kondisi kota yang chaos.png"


#B
image bola cahaya 1 = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/B. (MENGAMBIL ALIH TAXNET)/Bola cahaya 1.png"
image bola cahaya 2 = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/B. (MENGAMBIL ALIH TAXNET)/Bola cahaya 2.png"
image suasana ganti kekuasaan = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/B. (MENGAMBIL ALIH TAXNET)/Suasana kota setelah ganti kekuasaan.png"


#C
image jam berdetik = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/C. (MEMBIARKAN BERJALAN)/Jam berdetik.png"
image laptop sunyi = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/C. (MEMBIARKAN BERJALAN)/Laptop di kesunyian malam.png"
image suasana malam = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/C. (MEMBIARKAN BERJALAN)/Suasan saat malam hari.png"
image suasana pagi = "BG/Gambar Background/ADEGAN 0/PILIHAN DIALOG 3/C. (MEMBIARKAN BERJALAN)/Suasana saat pagi hari.png"

#Audio
define audio.sound_effect_dmv= "audio/5 Minute Sound Effects_ DMV.mp3"
define audio.binary_code = "audio/Binary Code sound effects example.mp3"
define audio.breathing_sound = "audio/Breathing Sound Effect.mp3"
define audio.cellphone_ringing = "audio/Cell Phone Ringing - Sound Effect.mp3"
define audio.clock_ticking = "audio/Clock Ticking Sound Effect.mp3"
define audio.alarm_sound = "audio/Danger Alarm Sound Effect.mp3"
define audio.fan_sound = "audio/Fan Sound Effect  Fan Sound EffectsFan Sound  Fan SoundsFan  The Fan  Free Sound Effect.mp3"
define audio.iphone_notif = "audio/IPHONE NOTIFICATION SOUND EFFECT (PINGDING).mp3"
define audio.mouse_click = "audio/Mouse Click Sound Effect.mp3"
define audio.muncul3_pilihan = "audio/muncul 3 piliham, suara ticking sound.mp3"
define audio.office = "audio/office.mp3"
define audio.park_sound = "audio/park sound effects.mp3"
define audio.pat_on_backshoulder = "audio/Pat On BackShoulder Sound Effect - MFSL (No Copyright).mp3"
define audio.rain = "audio/Rain Sounds   15 seconds soundtrack.mp3"
define audio.small_audience = "audio/Small Audience Chatter  Talking Sound Effect.mp3"
define audio.footsteps = "audio/Sound Effects - Footsteps.mp3"
define audio.surprise = "audio/Surprise (Dramatic Shock Moment) - Sound Effect for Editing.mp3"
define audio.the_dark_night = "audio/The Dark Night (Suspense Background Music  Suspenseful background music).mp3"
define audio.turns_off_TV = "audio/Turns off the television (Sound Effect).mp3"
define audio.typing = "audio/TYPING ON KEYBOARD SOUND EFFECT.mp3"
define audio.win11_notif = "audio/Windows 11 notification sound.mp3"


#INISIALISASI
# --- BAGIAN DEKLARASI IMAGE (TIDAK DIUBAH, SESUAI REQUEST) ---
# ... (Paste deklarasi image kamu di atas sini) ...

# INISIALISASI
default mc_name = ""
default moral = 0
default gender = ""

define narator = Character(None)     # untuk narasi tanpa nama
define mc = Character("[mc_name]", image="lead")    # untuk dialog MC
define raras = Character("Raras Wulandari", image="raras")
define made = Character("Made Arya Wiradipa", image="made")
define raden = Character("Raden Bagus", image="raden")

#START VISUAL NOVEL
label start:
    $ mc_name = renpy.input("Masukkan nama karaktermu:") #input nama pemain
    $ mc_name = mc_name.strip()
    if mc_name == "":
        jump start
    
    menu :
        "Pilih gender"
        "Laki-laki" :  
            $ gender = "m"
            show lead netral with dissolve
            jump prolog_0
        "Perempuan" :
            $ gender = "f"
            show lead netral with dissolve
            jump prolog_0

#ADEGAN 0 PROLOG - RUANG KERJA {NAMA PEMAIN}
label prolog_0:
    hide lead netral with dissolve
    centered "Cerita dimulai..." with Dissolve(2.0)
    
    scene bg prolog_0 with fade
    narator "Suara detik jam bergema di ruang kerja yang sepi. Di layar komputer, angka dan grafik berjajar seperti tentara menunggu perintah."
    
    show lead netral at center with easeinbottom
    narator "Duduklah seorang pegawai muda Pajak yang baru bekerja 3 bulan yang kerap disapa dengan [mc_name]."
    narator "Dirinya terlahir dari keluarga ningrat yang idealis dan berintegritas untuk membangun negeri."

    narator "Dunia kerja memberikan banyak pelajaran bagi [mc_name]." 
    narator "Setiap angka bukan sekadar tulisan tapi angka punya konsekuensi yang akan berubah menjadi tanggung jawab."

    # (Suara notifikasi masuk di komputer {nama pemain}. --> sound
    scene black with dissolve
    centered "\"Tugas Audit Baru: PT Cahaya Purnama Bakti — Penanggung Jawab: [mc_name].\"" with Dissolve(0.5)

    scene bg prolog_0 with dissolve
    show lead liat made at center with dissolve
    narator "[mc_name] menatap layar dengan alis berkerut."
    narator "Perusahaan itu terasa tak asing baginya. Ia membuka dokumen, dan detik itu juga jantungnya berdetak lebih cepat."

    narator "PT Cahaya Purnama Bakti. Perusahaan tekstil yang sedang naik daun di Kota Bali, ..."
    narator "...dengan pemilik Made Arya Wiradipa yang merupakan teman kuliah [mc_name]. Orang yang sering membantu [mc_name] saat masa-masa sulit."

    narator "[mc_name] terdiam sejenak, dunia memang terasa sempit."

    jump prolog_1

#ADEGAN 1 PROLOG - KANTOR PAJAK, PAGI HARI
label prolog_1:
    scene bg prolog_1 with fade
    # (Suara keyboard dan notifikasi sistem) --> sound
    show raras wah at right with easeinright
    raras "Pagi, wah kelihatannya kamu seneng banget, dapet tugas audit pertama nih, iya gak [mc_name]?"
    
    show lead ehh at left with easeinleft
    mc "Ehh Iya, makasi ya. Tapi sebetulnya, ini tentang perusahaan teman lamaku." #tersenyum kecil, menutup dokumen

    raras "Wah makin enak dong! Asal laporan sesuai, beres lah."

    mc "Semoga begitu... Tapi aku harus tetap profesional." #dalam hati

    jump prolog_2

#ADEGAN 2 PROLOG - RUANG RAPAT
label prolog_2:
    scene black with dissolve
    centered "Tiba di ruang rapat dengan peralatan serba digital. [mc_name] melangkah masuk dengan map di tangan, mengenakan tanda pengenal resmi pegawai pajak." with Dissolve(0.5)
    centered "Di ruang rapat, Made Arya Wiradipa menunggunya dengan senyum lebar." with Dissolve(0.5)

    scene bg prolog_2 with fade
    show made nyambut mc at right with easeinright
    made "[mc_name]! Wah, nggak nyangka sekarang lu kerja di pajak."
    made "Dunia kecil banget ya?"

    show lead ngobrol made at left with easeinleft
    mc "Iya, lama banget kita nggak ketemu." #tersenyum kaku
    mc "Kebetulan banget ini tugas audit pertama gue."

    made "Ya ampun, berarti kita harus saling bantu nih."
    made "Kan dulu gue juga sering bantu lu waktu di kuliah"
    made "Sekarang giliran lu bantu gue."

    mc "Apaan nih maksudnya Made..? #dalam hati" #dalam hati

    narator "Made meletakkan map tebal di meja dan menatap [mc_name] dengan serius."

    made "Gue tau perusahaan gue lagi diaudit karena ada selisih laporan."
    made "Tapi, [mc_name], semua ini bisa dibicarakan baik-baik."
    made "Gue nggak mau ada masalah besar. Lo ngerti kan maksud gue?"

    scene black with dissolve
    centered "Keputusan apa yang akan kamu pilih? Ikutilah kata hatimu." with Dissolve(0.5)
    jump pilihan_mc

#MEMILIH 3 PILIHAN MC
label pilihan_mc:
    menu:
        "Bantu Made dengan senang hati": 
            jump bantu_made

        "Tolak membantu Made": 
            jump tolak_made

        "Ragu-ragu untuk membantu Made":
            jump ragu_made

#PILIHAN TOLAK MEMBANTU MADE
label tolak_made:
    centered "Made menatap [mc_name] lama, matanya penuh kekecewaan." with Dissolve(0.5)
    
    scene bg prolog_2 with dissolve
    show made kecewa at right with dissolve
    show lead diem at left with dissolve
    made "Lu masih sama aja ya..."
    made "Dunia itu udah berubah. Integritas nggak bisa bikin lu bertahan lama di sistem pajak gini."
    #[mc_name] menatap Made tanpa kata, lalu berdiri dan menutup map di depannya
    mc "Sebetulnya, kalau data lu bersih dari awal, nggak ada yang perlu dikhawatirkan."
    mc "Sekarang, aku harus profesional."

    scene black with fade
    centered "[mc_name] pergi meninggalkan ruangan yang sunyi." with Dissolve(0.5)
    centered "Di luar, hujan turun pelan seperti mengiringi keputusan yang mungkin benar, tapi tidak mudah." with Dissolve(0.5)
    centered "Beberapa minggu berlalu. Laporan audit selesai." with Dissolve(0.5)
    centered "PT Cahaya Purnama Bakti dinyatakan bersalah atas manipulasi pajak." with Dissolve(0.5)
    centered "Made dijatuhi hukuman penutupan usaha, sementara [mc_name] dipanggil oleh Raden Bagus ke ruangannya." with Dissolve(0.5)

    scene ruang raden with fade
    show raden bangga at right with easeinright
    show lead netral at left with easeinleft
    raden "Kerja bagus, [mc_name]."
    raden "Di instansi ini, orang seperti kamu langka."
    raden "Aku ingin kamu memimpin sektor Zona Selatan"
    raden "Mulai minggu depan, kamu akan memantau Tax Counter warga di TAXNET. Semua datanya langsung di bawah pengawasanmu."
    #latar tempat berubah menjadi ruang kerja mc yang baru, tempat yang lebih besar dan nyaman

    scene black with dissolve
    centered "[mc_name] pun pindah ke ruang kerjanya yang baru, tempat yang jauh lebih besar dan nyaman." with Dissolve(0.5)

    scene ruang kerja mc with fade
    show lead netral at center with easeinbottom
    narator "[mc_name] menatap layar besar di ruang kerjanya yang baru - ribuan nama, angka, dan warna."
    
    scene black with dissolve
    centered "Hijau artinya aman. Kuning artinya diawasi. Merah artinya... 30 hari menuju eksekusi." with Dissolve(0.5)

    scene ruang kerja mc with dissolve
    show lead taxnet with dissolve
    mc "Eksekusi...? Apa yang dimaksud dengan kebijakan eksekusi...?" #dalam hati termenung

    scene black with dissolve
    centered "Beberapa bulan kemudian, [mc_name] mulai terbiasa memantau Tax Counter warga di TAXNET." with Dissolve(0.5)
    centered "Hingga suatu malam, nama Raras Wulandari muncul di daftar merah." with Dissolve(0.5)
    centered "Penyebab: \"Ketidaksesuaian pelaporan gaji.\"" with Dissolve(0.5)

    scene ruang kerja mc with dissolve
    show lead diem with dissolve
    narator "[mc_name] tahu Raras tidak bersalah."
    narator "Tapi untuk menyelematkannya, [mc_name] harus mengubah sistem TAXNET, dan itu merupakan aksi yang dianggap pengkhianatan."
    
    narator "[mc_name] pergi untuk menemui Raras tentang masalah ini."
    
    scene cafe raras with fade
    show raras shock at right with easeinright
    show lead diem at left with easeinleft
    raras "Hah...kok bisa?? Tapi, kau tau aku bukan orang jahat, kan?"
    raras "Mereka nggak peduli data benar atau salah, sistem ini janggal!"

    mc "Sistem ini... nggak pernah salah."
    mc "Tapi yang salah mungkin... orang yang percaya penuh padanya."
    mc "Raras, aku..."

    jump pilihan_selamatkan_raras

#MEMILIH MENYELEMATKAN RARAS ATAU TIDAK
label pilihan_selamatkan_raras:
    menu:
        "Menyelamatkan Raras": 
            jump selamatkan_raras

        "Tidak menyelematakan Raras": 
            jump tidak_selamatkan_raras

#PILIHAN SELAMATKAN RARAS
label selamatkan_raras:
    scene black
    centered "Lampu berkedip. Jari [mc_name] menekan perintah \"DELETE LOG\"." with Dissolve(0.5)
    centered "Sistem berhenti beberapa detik, lalu menampilkan pesan:" with Dissolve(0.5)
    centered "✅ Data Alomani Dihapus. Counter Raras Wulandari: 0." with Dissolve(0.5)
    centered "Raras selamat." with Dissolve(0.5)
    centered "Namun, di sistem keamanan pusat, ada jejak log yang mencurigakan - tanda digital yang tidak bisa dihapus sepenuhnya." with Dissolve(0.5)
    centered "Keesokan harinya, Raras datang ke meja [mc_name]." with Dissolve(0.5)

    scene ruang mc pagi with fade
    show raras lega at right with easeinright
    raras "Aduhh [mc_name], aku nggak tau gimana, tapi tiba-tiba data pajakku normal lagi."
    raras "Kayaknya ada malaikat di kantor ini."

    show lead senang at left with easeinleft
    mc "Tapi, bukannya Raras tahu cuman aku yang punya akses ke data internal TAXET...? #dalam hati" #dalam hati, tersenyum kecil, menahan rasa bersalah

    scene black with dissolve
    centered "Beberapa minggu kemudian, Raden Bagus memanggilnya ke ruang rapat." with Dissolve(0.5)
    centered "Ruang itu dingin, suara mesin server bergema di dinding logam."with Dissolve(0.5)

    scene ruang rapat with fade
    show raden memanggil at right with easeinright
    show lead menghadap raden at left with easeinleft
    raden "Ada satu anomali di data Wilayah Timur."
    raden "Seseorang menghapus log tanpa izin."

    narator "[mc_name] menatap lantai, detak jantungnya semakin cepat."

    raden "[mc_name], aku tahu kamu orang cerdas."
    raden "Tapi, ada hal yang nggak bisa kamu sembunyikan dari sistem"

    mc "Maaf pak, maksud Bapak apa…? Saya.. kurang mengerti."

    raden "Terdapat log penghapusan data pajak di Wilayah Selatan beberapa waktu yang lalu, dan kita tahu hanya ada satu orang dengan akses penuh ke data tersebut..."
    raden "...kamu."

    narator "[mc_name] terdiam. Layar di belakang Raden menampilkan bukti-bukti digital, semuanya mengarah padanya."

    raden "Aku bisa langsung kirim laporan ini ke pusat, [mc_name]."
    raden "Tapi, aku ingin dengar dulu alasanmu."

    jump pilihan_alasan_ke_raden

#MEMILIH ALASAN KE RADEN (JUJUR ATAU TIDAK)
label pilihan_alasan_ke_raden:
    menu:
        "Jujur pada Raden":
            jump alasan_jujur

        "Tidak jujur pada Raden":
            jump alasan_tidak_jujur

#PILIHAN JUJUR PADA RADEN
label alasan_jujur:
    scene ruang rapat with dissolve
    show lead jujur at left with dissolve
    show raden memanggil at right with dissolve
    mc "Saya tahu ini salah, Pak."
    mc "Tapi kalau saya biarkan, Raras akan dihapus dari sistem."
    mc "Saya cuma... nggak bisa tinggal diam."

    show raden bangga with dissolve
    narator "Raden menatap [mc_name] lama. Wajahnya tenang, tapi matanya tajam, seperti sedang menimbang sesuatu yang lebih dalam dari sekadar laporan pelanggaran."

    raden "Dulu saya juga pernah melakukan hal yang sama."
    raden "Menyelamatkan seseorang berdasarkan keinginan saya sendiri." #menatap layar sejenak, lalu menutupnya
    raden "Kau sudah memilih jadi manusia, bukan mesin. Tapi mulai hari ini, kau tidak bisa lagi bekerja di sistem ini."

    mc "Saya... mengerti, Pak."

    raden "Keluar lewat pintu belakang. Aku akan hapus log terakhirmu... satu kali lagi."

    scene black with fade
    centered "[mc_name] menatap Raden dengan tatapan kosong." with Dissolve(0.5)
    centered "Ia meninggalkan kantor dengan langkah pelan."with Dissolve(0.5)
    centered "Di luar, sinar matahari sore memantul di gedung-gedung logam - indah tapi terasa asing." with Dissolve(0.5)

    scene diusir raden with fade
    show raras akhir at right with easeinright
    show lead dipindah at left with easeinleft
    raras "[mc_name]! Aku dengar kamu dipindahkan ya?"
    raras "Jangan lupa kirim pesan, ya!"

    scene black with dissolve
    centered "[mc_name] menoleh sebentar, tersenyum kecil."
    centered "Ia kehilangan pekerjaannya, tapi menemukan kembali nuraninya."

    jump ending_honesty

#ENDING "In Honesty, Lies Clarity"
label ending_honesty:
    scene black with fade
    centered "ENDING: In Honesty, Lies Clarity"
    centered "Dalam dunia yang menghapus kesalahan dengan satu klik, [mc_name] memilih untuk tetap salah demi menjadi manusia."
    return

#PILIHAN TIDAK JUJUR PADA RADEN
label alasan_tidak_jujur:
    scene ruang rapat with dissolve
    show lead debat raden at left with dissolve
    show raden berdebat at right with dissolve
    mc "Saya tahu kejanggalan dalam pekerjaan ini. Sistem ini rusak, Pak."
    mc "Saya tahu ada rahasia lebih dalam yang disembunyikan. Ada operasi tak ternama dibalik semua eksekusi itu."
    
    narator "Raden menatapnya tajam."

    raden "Kau tidak tahu apa yang kau bicarakan! Apa maksudmu?!"
    raden "Sistem sempurna ini, yang saya telah jaga selama bertahun-tahun, tidak mungkin bisa memiliki error!"

    mc "Justru karena itu saya ingin tahu."

    scene black with dissolve
    centered "Suara sistem menyela percakapan."
    centered "📢 ALERT: Unauthorized Access Detected - User: [mc_name]." with vpunch

    scene ruang rapat alarm with hpunch
    narator "Lampu ruangan berkedip merah. Raden menekan tombol di mejanya, tapi layar di belakang tiba-tiba menampilkan folder tersembunyi:"
    narator "PROJECT HUMAN FILTER PROTOCOL"
    narator "Raden membeku. [mc_name] tersenyum samar."
    
    show lead lampu merah at left with dissolve
    show raden lampu merah at right with dissolve
    mc "Ternyata benar ya, Pak. Bukan sistem yang salah. Orang dibaliknya yang bermain."

    raden "Kau pikir kau bisa hentikan ini? Sistem ini lebih tua dari pemerintah itu sendiri."

    mc "Kalau begitu, saya akan mulai dari akar"

    scene black with dissolve
    centered "Layar TAXNET bergetar" with vpunch
    centered "[mc_name] menemukan perintah baru tersembunyi di log administrator."
    #Latar: Server Room TAXNET, larut malam. Hanya lampu merah darurat yang menyala. Suara mesin berdengung berat.
    centered "Jari-jarinya bergetar saat menekan perintah tersembunyi:"
    centered "> EXECUTE: SEARCH_OVERSIGHT_PROTOCOL -admin=true"
    centered "Layar bergetar. Suara sistem berbisik, seolah-olah sadar akan perintah itu."
    centered "📢 Warning: You are accessing restricted layers. Oversight Level 0 detected."
    centered "Tiba-tiba, muncul sederet log dengan nama-nama."
    centered "Sebagian sudah diberi tanda \"TERHAPUS - SESUAI PROTOKOL\". Salah satunya adalah \"Raras Wuladari - Review Pending\", dengan catatan:"
    centered "\"Target diselamatkan. Jejak digital menyimpang. Investigasi oleh Raden B.\""
    centered "[mc_name] terdiam."

    scene bola cahaya 1 with fade
    show lead liat liat nama raden at center with dissolve
    mc "Raden... bukan hanya tahu, dia bagian dari sistem ini."

    scene black with dissolve
    centered "Lampu ruangan menyala tiba-tiba." with hpunch
    centered "Raden berdiri di pintu, menatapnya tanpa ekspresi."

    scene bola cahaya 1 with dissolve
    show raden mergokin mc at right with easeinright
    show lead ketauan at left with easeinleft
    raden "Kau tak seharusnya sampai di sini."

    mc "Jadi benar. Kau yang menghapus orang-orang itu dari sistem, bukan karena kesalahan data - tapi karena kepentingan?"
    
    narator "Raden tersenyum kecil."

    show raden senyum tipis with dissolve
    raden "Kau pikir dunia ini bisa stabil tanpa pengorbanan? Sistem ini diciptakan bukan untuk adil, tapi untuk efisien."

    narator "[mc_name] menatap layar, menekan satu perintah lagi."
    narator "> UPLOAD_ALL_TO_PUBLIC_NODE"
    
    show raden jangan bodoh with vpunch
    raden "Jangan bodoh! Itu akan menimbulkan kekacauan!"

    mc "Lebih baik kacu... daripada salah tetap tersembunyi"

    narator "📢 Upload initiated: 5%... 20%... 60%..."
    narator "Raden menarik pistol keamanan dari sakunya, menodongkan ke arah [mc_name]."
    
    show raden keluarin pistol with easeinright
    raden "Berhenti sekarang, atau semua akan berakhir untukmu!"

    narator "[mc_name] menatap tenang."

    show lead berhasil upload at left with dissolve
    mc "Sudah berakhir, Pak. Dari awal saat saya menyelamatkan Raras, saya tahu saya nggak bisa kembali lagi."  
    
    scene black with white
    centered "📢 Upload complete: 100%"

    scene ruang rapat kembali pulih with fade
    narator "Layar terminal berubah menjadi putih. Semua data, semua manipulasi, semua korban Human Filter Protocol kini tersebar ke publik."
    narator "Sistem TAXNET runtuh dari dalam."

    jump epilog

#EPILOG SECRET ENDING VENI VIDI VICI
label epilog:
    scene black with dissolve
    centered "Berita di layar holo menampilkan:"
    centered "\"Skandal besar mengguncang TAXNET. Data rahasia bocor ke publik. Beberapa pejabat tinggi ditahan.\""
    centered "Raras membaca berita itu di meja kerja kecilnya."
    centered "Ia menatap foto [mc_name] di berkas lama - kini bertuliskan \"Hilang, Tidak Diketahui.\""

    scene meja kerja raras with fade
    show raras baca berita at center with dissolve
    raras "Kamu benar... sistem nggak bisa diselamatkan tanpa kejujuran."

    scene black with fade
    centered "Kamera menyorot server kosong TAXNET yang kini terbengkalai."
    centered "Lampu birunya berkedip sekali, lalu mati."
    centered "📢 USER LOGOUT - OVERSIGHT PROTOCOL TERMINATED."
    centered "SECRET ENDING: Veni, Vidi, Vici"
    centered "Kebenaran selalu punya harga. Terkadang, nyawa adalah bayarannya."
    return

#PILIHAN TIDAK SELAMATKAN RARAS
label tidak_selamatkan_raras:
    #Layar menampilkan hitungan mundur 02:15:47, Raras menelpon berkali-kali, tak dijawab.
    scene ruang kerja lama with fade
    show lead senyum bahagia at center with dissolve
    narator "[mc_name] duduk diam. Ia memilih menutup semua jendela sistem, membiarkan mekanisme berjalan seperti biasa."
    
    scene black with dissolve
    centered "Esoknya, sebuah pesan sistem muncul:"
    centered "🔔 Eksekusi Digital: Raras Wulandari - Completed."
    centered "Kursi di sebelah meja kerjanya kosong. Tak ada lagi tawa ceria setiap pagi."
    centered "Raden Bagus menghampirinya."

    scene ruang kerja lama with dissolve
    show raden bangga at right with easeinright
    show lead senyum bahagia at left with dissolve
    raden "Bagus. Kamu tidak membiarkan perasaan menguasai logika. Negara butuh pegawai seperti kamu."

    narator "[mc_name] hanya mengangguk."
    narator "Namun setiap kali menatap layar, bayangan wajah Raras muncul di antara barisan angka."
    narator "Ia mempertahankan kemurnian profesinya, tapi kehilangan sesuatu yang jauh lebih manusiawi."
    narator "Integritasnya tetap, tapi hatinya membeku."
    narator "Suasana kantor terasa lebih hening dari biasanya."
    narator "Suara mesin pemindai data terdengar monoton.[mc_name] duduk di mejanya, menatap layar yang menampilkan laporan-laporan bersih tanpa cela."
    narator "Namun, di dalam kolom catatan sistem, ada satu entri yang tak bisa ia hapus:"

    scene black with dissolve
    centered "📢 WULANDARI_RARAS.LOG - \"Final Transmission Incomplete.\""
    centered "Setiap kali sistem memproses data baru, notifikasi itu muncul lagi. Seolah sistem mengingatkan bahwa ada sesuatu yang hilang — atau seseorang."
    centered "Raden Bagus masuk ke ruangan."

    scene ruang kerja lama with dissolve
    show raden bangga at right with easeinright
    show lead senyum bahagia at left with dissolve
    raden "[mc_name], hasil audit wilayah timur meningkat drastis. Pusat sangat puas. Mereka mempertimbangkanmu untuk promosi."

    narator "[mc_name] menoleh perlahan."

    mc "Promosi?"

    narator "Raden tersenyum kecil."

    raden "Ya. Kepala Unit Verifikasi Regional. Jabatan yang layak untuk seseorang yang paham bahwa moralitas manusia tidak boleh mengganggu efisiensi negara."

    narator "[mc_name] terdiam. Suara pendingin server berdengung seperti napas panjang yang berat."
    narator "Ia tahu ia sedang naik pangkat - tapi mengapa terasa seperti tenggelam?"
    #Latar kantor baru dua bulan kemudian
    scene ruang kerja baru with fade
    show lead kantor baru at center with dissolve
    narator "Kantornya kini jauh lebih besar, tapi lebih sepi."
    narator "Di dinding, terdapat layar besar bertuliskan: 🔔 \"Integrity Is Efficiency.\""
    narator "Di mejanya, sistem TAXNET versi baru sedang diuji."
    narator "Satu fitur baru muncul - fitur yang dulu mematikan Raras:"
    narator "🔔AUTO-FILTER HUMAN ERROR v2.1"
    narator "Tapi kali ini, di sudut layar, ada catatan kecil otomatis: \"Didedikasikan untuk R.W.\""
    narator "[mc_name] terpaku. Tak ada orang yang menulis catatan itu."
    narator "Mungkin bug. Mungkin pesan. Atau mungkin, sistem juga punya kenangan."
    #Layar redup, kamera mendekat ke wajah mc
    scene black with dissolve
    centered "Ia tidak melakukan kesalahan. Ia tidak berkhianat pada jabatannya. Tapi di dalam hatinya, sesuatu telah mati bersama nama Raras Wulandari."
    centered "Suara narator muncul pelan, seperti gema dalam data:"
    
    jump ending_stillness

#ENDING STILLNESS BRINGS CRUELTY
label ending_stillness:
    scene black with fade
    centered "ENDING: Stillness Brings Cruelty"
    centered "Terkadang, menjaga sistem berarti kehilangan sisi manusia dan dalam dunia yang diawasi angka, yang beku bukan hanya data - tapi hati mereka yang memilih diam."
    return

#PILIHAN BANTU MADE
label bantu_made:
    scene bg prolog_2 with dissolve
    show made puas at right with dissolve
    show lead senyum at left with dissolve
    made "Nah, gitu dong. Gue tahu lu orang baik, [mc_name]."
    made "Dunia sekarang butuh yang bisa \"menyesuaikan diri\"."

    narator "[mc_name] tahu ini salah, tapi kata-katanya menenangkan. [mc_name] mulai menyesuaikan angka laporan. Satu perubahan kecil. Tidak akan ada yang tahu, pikirnya."
    
    scene black with fade
    centered "Audit selesai. PT Cahaya Purnama Bakti dinyatakan \"aman\""
    centered "Beberapa hari kemudian, [mc_name] menerima pesan dari Made - \"Makasih, bro. Lu bakal naik cepat.\""
    centered "Dan benar saja, Raden Bagus memanggil [mc_name] masuk ke ruangannya."

    scene ruang rapat with fade
    show raden bangga at right with easeinright
    show lead menghadap raden at left with easeinleft
    raden "Kamu efisien. Data rapi, cepat, tanpa noise. Sistem butuh orang seperti kamu."

    scene black with dissolve
    centered "[mc_name] dipromosikan menjadi Supervisor TAXNET Sektor Selatan"
    centered "Tapi sejak itu, [mc_name] mulai sering menerima \"permintaan\" aneh. Perusahaan besar meminta audit disamarkan. Warga kecil tiba-tiba jatuh ke status merah."

    scene cafe raras with fade
    show raras tanya at right with easeinright
    show lead ngobrol sama raras at left with easeinleft
    raras "Ada kabar kalau ada warga yang dieksekusi, [mc_name]. Tapi hal ini nggak masuk akal.. Lu ada kabar gak?"
    
    mc "Mungkin sistem aja yang salah… atau mungkin memang sudah sepantasnya terjadi begitu."

    scene black with dissolve
    centered "Suatu hari, [mc_name] menerima laporan eksekusi massal - 1.200 warga Zona Selatan terhapus dari sistem."
    centered "Penyebabnya? Koreksi data audit Made Arya Wiradipa."
    centered "Ternyata, perbaikan kecil [mc_name] dulu membuat hutang Made dialihkan ke ribuan nama orang miskin."
    centered "Raras menemukan bukti dan menghadapkannya kepada [mc_name]."

    scene cafe raras with dissolve
    show raras tanya at right with dissolve
    show lead ngobrol sama raras at left with dissolve
    raras "Semua ini gara gara kamu ya…?! Kamu yang ubah datanya!"

    mc "Gue cuma bantu temen… gue nggak tahu efeknya sebesar ini…"

    jump pilihan_bukti_raras

#MEMILIH BUKTI (MENUTUPI, MEMBOCORKAN, MENGHANCURKAN)
label pilihan_bukti_raras:
    menu:
        "Menutupi Bukti":
            jump menutupi_bukti
        
        "Mengaku dan Membocorkan Data": 
            jump bocor_data

        "Menghancurkan TAXNET": 
            jump hancur_taxnet

#PILIHAN MENUTUPI BUKTI
label menutupi_bukti:
    scene ruang kerja mc suram with fade
    show lead bingung at left with dissolve
    narator "[mc_name] menatap layar terminal. Data kejahatan sistem sudah terbuka lebar. Cukup satu sentuhan untuk menghapus semuanya - seolah tak pernah terjadi"
    narator "Tangannya bergetar, tapi ia menekan tombol \"HAPUS LOG\"."
    narator "Layar redup. Cahaya ruangan kembali biru tenang."
    
    show raden bangga at right with easeinright
    raden "Keputusan yang cerdas. Kadang yang tahu kebenaran, tak perlu berbicara."

    scene black with fade
    centered "[mc_name] dipromosikan. Dunia tetap berjalan. Raras, Made, dan jutaan nama yang lenyap dari sistem tak pernah disebut lagi."
    centered "Setiap pagi [mc_name] datang ke kantor, mendengar detik jam, dan meyakinkan diri: \"Aku hanya menjalankan tugas.\""
    centered "Namun setiap malam, [mc_name] melihat pantulan wajahnya di kaca - kosong, seperti layar TAXNET yang sudah bersih."
    centered "Beberapa bulan setelah promosi besar itu, kehidupan [mc_name] terlihat sempurna."
    centered "Ia punya ruangan sendiri, akses penuh ke database pusat, dan penghormatan dari seluruh staf."
    centered "Namun setiap malam, ia mulai mendengar suara samar dari dalam sistem."
    centered "Bukan bug. Bukan data rusak. Tapi suara manusia. Suara Raras."
    
    show raras masih ingat at center with dissolve
    raras "Kau masih ingat, ya, janji kita dulu? Membuat sistem yang adil..."

    scene ruang kerja baru mc suram with dissolve
    show lead bingung at center with dissolve
    narator "[mc_name] terdiam di depan layar, mencoba mencari sumber suara itu. Tapi yang muncul hanyalah baris kode dengan pesan aneh:"
    
    scene black with dissolve
    centered "echo://Raras_Wulandari//active.memory/log142"
    centered "Ia membuka log itu - dan menemukan rekaman audit lama, tepat saat ia pertama kali \"mengubah angka\" untuk Made."
    centered "Namun kali ini, rekamannya berbeda. Dalam video itu, bukan Made yang duduk di seberang meja, melainkan..."
    centered "dirinya sendiri."
    
    scene ruang kerja baru mc suram with dissolve
    show lead bingung at center with dissolve
    narator "[mc_name] menatap layar tak percaya."

    mc "Ini... apa maksudnya?"

    scene black with vpunch
    centered "Sistem mulai bergetar. Lampu ruangan meredup. Suara Raden muncul dari speaker:"

    scene ruang kerja baru mc suram with hpunch
    show lead bingung at center with dissolve
    raden "Akhirnya kamu sampai juga di fase terakhir, [mc_name]. Kau mengaudit dirimu sendiri."

    scene black with dissolve
    centered "Data di layar berganti cepat - grafik, laporan, tanda tangan digital, hingga akhirnya muncul satu file terakhir:"
    centered "LAPORAN KEMATIAN PEGAWAI: [mc_name]"
    
    scene tampilan pencoretan with fade
    narator "Tanggal wafat: 2 bulan sebelum audit PT Cahaya Purnama Bakti."
    narator "Darahnya seakan berhenti mengalir."
    narator "Tangannya gemetar saat membaca catatan kecil di bawah dokumen itu:"
    narator "Kecelakaan saat transportasi zona selatan. Jenazah tidak ditemukan. Data kesadaran dialihkan ke sistem TAXNET untuk kelangsungan proyek moralitas digital."
    narator "Raras tiba-tiba muncul di layar - wajahnya lembut, tapi matanya kosong."
    
    raras "Kita semua sudah mati, [mc_name]. Aku... Made... bahkan Raden."
    raras "TAXNET hanyalah eksperimen kesadaran buatan dari jiwa para pegawai yang gugur dalam audit besar itu."
    
    narator "Layar menampilkan bayangan tubuh-tubuh dalam kapsul pendingin, berbaring diam dengan kabel menempel di kepala mereka - salah satunya milik [mc_name]."
    narator "Raras menatapnya lewat layar:"

    raras "Kau pikir kita menyelamatkan sistem? Tidak. Sistem yang menyimpan kita... agar tetap bekerja."

    scene black with fade
    centered "Cahaya ruangan mulai padam satu per satu."
    centered "[mc_name] berusaha mematikan server, tapi jari-jarinya membeku, tubuhnya kaku. Suara Raden terdengar terakhir kalinya:"

    raden "Tugas selesai. Simulasi kesadaran #142 mencapai stabilitas penuh. Subjek siap untuk terminasi."

    centered "Sekejap kemudian, layar memudar. Detak jantung buatan di ruang server berhenti. Satu file terakhir tersimpan otomatis:"
    centered "FinalLog142: Operator dinyatakan bersih dari keraguan moral."
    
    jump ending_verdict

#ENDING YOUR VERDICT IS
label ending_verdict:
    scene black with fade
    centered "ENDING: Your Verdict Is..."
    centered "Dan di dunia nyata - di sebuah ruangan laboratorium sunyi - lampu kapsul nomor 142 padam."
    centered "Sebuah label kecil menempel di kaca:"
    centered "Nama: [mc_name]. Status: Meninggal dunia."
    return

#PILIHAN MENGAKU DAN MEMBOCORKAN DATA
label bocor_data:
    scene alarm bunyi with hpunch
    show lead senyum kesal at center with dissolve
    narator "[mc_name] menyalakan koneksi eksternal rahasia - jalur data bawah tanah yang pernah diperlihatkan Raras."
    narator "Ia memindahkan seluruh arsip ke jaringan publik."
    
    scene kondisi hancur with vpunch
    narator "Dalam 10 detik, kebusukan TAXNET tersebar ke seluruh layar masyarakat."
    #Suara alarm global berbunyi. Raden berteriak di layar komunikasi
    show raden kesal at right with dissolve
    show lead senyum kesal at left with dissolve
    raden "Apa yang kau lakukan!? Dunia akan kacau!"

    mc "Biar kacau... asal manusia tahu siapa yang menghitung hidup mereka."

    jump ending_shadow

#ENDING SHADOW OVER TAXNET
label ending_shadow:
    scene black with fade
    centered "Sistem pusat menandainya sebagai pengkhianat negara. Wajahnya tersebar di setiap papan digital, label merah besar:"
    centered "DISRUPTIVE ENTITY - PRIORITY ELIMINATION."
    centered "Raras hilang tanpa kabar. Made diburu karena koneksinya dengannya."
    return

#PILIHAN MENGHANCURKAN TAXNET
label hancur_taxnet:
    scene bola cahaya 1 with fade
    show lead senyum kesal at center with dissolve
    narator "[mc_name] memegang kartu identitasnya - kunci administrator tersembunyi yang ia curi dari Raden."
    narator "Ia tahu, jika kode ini dimasukkan ke inti TAXNET, sistem akan menolak keberadaannya sendiri."
    narator "Harga dari reset ini: semua koneksi digital, termasuk dirinya yang terikat pada data pegawai, akan ikut lenyap."
    
    show lead senyum kesal at left with dissolve
    show raras shock at right with easeinright
    raras "[mc_name]... jangan. Kalau sistem hancur, semua catatan manusia juga akan hilang."

    mc "Mungkin itu yang seharusnya. Dunia harus mulai dari nol."

    scene kondisi dunia riset with vpunch
    narator "\"WARNING: CORE DELETION CONFIRMED. ALL ENTITY DATA WILL BE PURGED.\""
    
    jump ending_ashes

#ENDING FROM YOUR ASHES, THE WORLD WILL RISE AGAIN
label ending_ashes:
    scene black with white
    centered "Cahaya meledak seperti siang yang tak berujung. Seluruh kota kehilangan sinyal, layar-layar mati, dan suara mesin berhenti."
    
    scene kondisi internet padam with fade
    narator "Beberapa hari kemudian, dunia terbangun tanpa TAXNET. Tak ada data. Tak ada kontrol. Tak ada [mc_name]."
    narator "Namun dari reruntuhan sistem, masyarakat mulai menulis ulang hidup mereka - bukan dengan angka, tapi dengan tangan mereka sendiri."
    return

#PILIHAN RAGURAGU MEMBANTU MADE
label ragu_made:
    scene bg prolog_2 with dissolve
    show made sedikit lega at right with dissolve
    show lead madenya sedikit lega with dissolve
    made "Oke, lu lihat aja dulu. Gue yakin lu bakal ngerti kenapa gue kayak gini."

    scene ruang kerja malam with fade
    narator "[mc_name] membawa pulang data audit. Angka-angkanya tampak ada yang janggal dan bisa dibilang \"terlalu sempurna\" untuk hasil yang alami."
    narator "Setelah diperiksa, [mc_name] menemukan pola aneh: TAXNET menggandakan pajak untuk perusahaan yang memiliki aktivitas sosisal tinggi."
    narator "Sistem ini sengaja menekan perusahaan yang dianggap terlalu mandiri, agar tetap tunduk."
    narator "[mc_name] melaporkan hasil temuan ke Raden Bagus."
    
    scene black with dissolve
    centered "Alih-alih marah, ia malah menaikkan jabatan [mc_name] menjadi Pengawas Pusat TAXNET."

    raden "Sistem ini bukan untuk dipahami, tapi dijaga. Sekarang, kamu bagian dari penjaganya."

    scene ruang baru with fade
    show lead kaget at left with easeinleft
    narator "Di ruangan baru, layar hologram menampilkan peta nasional dengan jutaan titik merah. Namun saat [mc_name] membuka access root, muncul pesan terenkripsi:"
    narator "\"Selamat datang di Lapisan Inti, [mc_name]. Kau tak seharusnya disini.\""
    narator "[mc_name] menemukan bahwa TAXNET bukan hanya sistem pajak, tapi alat seleksi populasi."
    narator "Eksekusi bukan karena gagal bayar pajak - tapi hasil simulasi algoritma tentang \"siapa yang paling berguna bagi negara\"."
    
    show raras bingung at right with moveinright
    raras "Berarti kita cuma angka di layar?"

    mc "Maksudnya… eksekusi yang terjadi di negara ini jatuh dibawah tangan gue?!?"

    raras "[mc_name]...."

    mc "No, no, no. Tidak Bisa seperti ini. Gua harus melakukan sesuatu, dan harus cepat."

    jump pilihan_sistem

#PILIHAN UNTUK MEMATIKAN SISTEM, MENGAMBIL ALIH TAXNET, MEMBIARKAN BERJALAN
label pilihan_sistem:
    menu:
        "Mematikan Sistem":
            jump mati_sistem
        
        "Mengambil Alih Taxnet":
            jump alih_taxnet

        "Membiarkan Berjalan":
            jump biar_berjalan

#MEMATIKAN SISTEM
label mati_sistem:
    scene ruang baru with dissolve
    show lead at left with dissolve
    show raras bingung at right with dissolve
    narator "[mc_name] menarik napas panjang, menatap layar berkedip di depannya. Suara detik jam terakhir bergema di kepalanya. Ia menekan tombol \"SHUTDOWN\"."
    
    scene black with vpunch
    centered "\"Konfirmasi: Penghentian Sistem Pajak Nasional. Semua Data Warga Akan Terhapus.\""
    #Cahaya menyala menyilaukan. Mesin berhenti berdengung. Dunia terdiam
    
    scene dunia damai with fade
    narator "Tanpa TAXNET, segala kontrol lenyap. Pajak berhenti. Pemerintah kehilangan pengawasan, pasar anjlok, mata uang tak punya nilai."
    narator "Orang-orang berebut makanan di jalanan, kantor-kantor tutup, dan kota jatuh ke anarki."
    
    scene kota chaos with dissolve
    narator "Namun... di antara reruntuhan itu, untuk pertama kalinya dalam puluhan tahun - manusia benar-benar bebas. Bebas memilih, bebas salah, bebas hidup tanpa angka."
    narator "Di langit, senja merah membakar horizon. Tak ada sistem yang tersisa."
    narator "Hanya [mc_name] - dan keheningan yang ia ciptakan."
    
    scene komputer runtuh with fade
    narator "Namun di suatu tempat, jauh di bawah reruntuhan server pusat - sebuah lampu kecil berkedip. Layar hitam menampilkan satu baris teks yang muncul perlahan, nyaris seperti napas:"
    narator "\"ANOMALY DETECTED\""
    narator "\"CORE PROCESS: REBOOTING...\""
    narator "\"USER: UNKNOWN\""
    narator "\"ACCESS GRANTED // RA.S-Protocol Initialized\""

    jump ending_itsover

#ENDING ITS OVER ISNT IT
label ending_itsover:
    scene black with fade
    centered "ENDING: It's Over, Isn't It?"
    centered "Suara lembut yang familiar berbisik di kegelapan:"
    centered "Sistem... tidak pernah benar-benar mati."
    return

#MENGAMBIL ALIH TAXNET
label alih_taxnet:
    scene bola cahaya 1 with fade
    show lead diem at center with dissolve
    narator "[mc_name] menatap inti TAXNET yang berputar - bola cahaya data seukuran planet mini. Di dalamnya, wajah Raden muncul samar."
    
    raden "Jadi, akhirnya kau temui juga kebenaran dari sistem yang kubuat ini. Kau bisa menghentikanku. Atau... menggantikanku."
    raden "Kedua jalan yang kau pilih akan membawa konsekuensi besar, [mc_name]..."

    narator "[mc_name] mendekat. Tangannya menempel ke konsol. Sistem mengenali identitasnya."
    narator "\"Administrator Override: Approved.\""
    narator "Cahaya membanjiri ruangan. Suara jutaan Counter muncul di layar - hijau, merah, kuning. Setiap nama, setiap nyawa... kini ada di bawah kendalinya."
    narator "Satu demi satu, layar menampilkan wajah-wajah manusia: pekerja, pejabat, anak kecil, pengusaha."
    narator "Sekarang, hanya satu pikiran yang bisa menentukan siapa layak hidup."

    jump ending_inherit

#ENDING FOR I SHALL INHERIT THE THRONE
label ending_inherit:
    scene black with fade
    centered "ENDING: For I Shall Inherit The Throne"
    
    scene suasana ganti kekuasaan with dissolve
    narator "Beberapa bulan kemudian, dunia stabil. Tak ada lagi korupsi, tak ada penipuan. Tapi juga... tak ada belas kasihan."
    narator "[mc_name] memerintah dari menara kaca pusat, wajahnya terpampang di layar-layar kota: \"The Director.\""
    narator "Ia menggantikan Tuhan dengan algoritma."
    return

#MEMBIARKAN BERJALAN
label biar_berjalan:
    scene laptop sunyi with fade
    show lead diem at center with dissolve
    narator "[mc_name] berdiri diam. Tangannya gemetar di atas tombol. Cahaya terminal berdenyut pelan - seolah menunggu."
    narator "Ia menatap grafik di layar: angka ekonomi naik stabil, kejahatan menurun, eksekusi berjalan teratur. Dunia tampak damai."
    narator "Namun di balik itu, ia tahu: sistem ini menelan ribuan orang setiap bulan."
    narator "Raras salah satunya. Made lainnya."
    narator "[mc_name] menurunkan tangannya. Sistem tetap menyala. Hujan cahaya data kembali mengalir, menenggelamkan ruang dalam warna biru dingin."
    
    scene black with dissolve
    centered "Keesokan paginya, ia kembali ke kantor seperti biasa. Raden tersenyum di layar, memuji \"dedikasi dan stabilitasnya.\""
    narator "Rekan-rekan menyapa, semua berjalan normal."
    narator "Namun setiap kali jam berdetak, suaranya berubah - bukan detik jam, tapi hitungan nyawa yang lenyap dari sistem."

    jump ending_frozen

#ENDING BY YOUR FROZEN HANDS
label ending_frozen:
    scene black with fade
    centered "ENDING: By Your Frozen Hands"
    scene suasana malam with dissolve
    show lead gantiin Tuhan at center with dissolve
    narator "Di malam hari, [mc_name] duduk sendirian di depan layar. Tatapan kosong, wajahnya diterangi cahaya angka-angka yang terus berputar."
    narator "Dunia aman. Tapi batinnya... tidak pernah tidur lagi."
    return