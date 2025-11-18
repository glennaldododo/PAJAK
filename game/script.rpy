#INISIALISASI
default mc_name = ""
default moral = 0
default relasi_made = 0
default relasi_raras = 0
default relasi_raden = 0
default mc_debt = 0

define narator = Character(None)     # untuk narasi tanpa nama
define mc = Character("[mc_name]")    # untuk dialog MC
define raras = Character("Raras Wulandari")
define made = Character("Made Arya Wiradipa")
define raden = Character("Raden Bagus")

#START VISUAL NOVEL
label start:
    $ mc_name = renpy.input("Masukkan nama karaktermu:") #input nama pemain
    $ mc_name = mc_name.strip()
    if mc_name == "":
        jump start
    jump prolog_0

#ADEGAN 0 PROLOG - RUANG KERJA {NAMA PEMAIN}
label prolog_0:
    narator "Suara detik jam bergema di ruang kerja yang sepi. Di layar komputer, angka dan grafik berjajar seperti tentara menunggu perintah."
    narator "Duduklah seorang pegawai muda Pajak yang baru bekerja 3 bulan yang kerap disapa dengan [mc_name]."
    narator "Dirinya terlahir dari keluarga ningrat yang idealis dan berintegritas untuk membangun negeri."

    narator "Dunia kerja memberikan banyak pelajaran bagi [mc_name]." 
    narator "Setiap angka bukan sekadar tulisan tapi angka punya konsekuensi yang akan berubah menjadi tanggung jawab."

    # (Suara notifikasi masuk di komputer {nama pemain}. --> sound

    narator "\"Tugas Audit Baru: PT Cahaya Purnama Bakti — Penanggung Jawab: [mc_name].\""

    narator "[mc_name] menatap layar dengan alis berkerut."
    narator "Perusahaan itu terasa tak asing baginya. Ia membuka dokumen, dan detik itu juga jantungnya berdetak lebih cepat."

    narator "PT Cahaya Purnama Bakti. Perusahaan tekstil yang sedang naik daun di Kota Bali, ..."
    narator "...dengan pemilik Made Arya Wiradipa yang merupakan teman kuliah [mc_name]. Orang yang sering membantu [mc_name] saat masa-masa sulit."

    narator "[mc_name] terdiam sejenak, dunia memang terasa sempit."

    jump prolog_1

#ADEGAN 1 PROLOG - KANTOR PAJAK, PAGI HARI
label prolog_1:
    # (Suara keyboard dan notifikasi sistem) --> sound
    raras "Pagi, wah kelihatannya kamu seneng banget, dapet tugas audit pertama nih, iya gak [mc_name]?"
    
    mc "Ehh Iya, makasi ya. Tapi sebetulnya, ini tentang perusahaan teman lamaku." #tersenyum kecil, menutup dokumen

    raras "Wah makin enak dong! Asal laporan sesuai, beres lah."

    mc "Semoga begitu... Tapi aku harus tetap profesional." #dalam hati

    jump prolog_2

#ADEGAN 2 PROLOG - RUANG RAPAT
label prolog_2:
    narator "Tiba di ruang rapat dengan peralatan serba digital. [mc_name] melangkah masuk dengan map di tangan, mengenakan tanda pengenal resmi pegawai pajak."

    narator "Di ruang rapat, Made Arya Wiradipa menunggunya dengan senyum lebar."

    made "[mc_name]! Wah, nggak nyangka sekarang lu kerja di pajak."
    made "Dunia kecil banget ya?"

    mc "Iya, lama banget kita nggak ketemu." #tersenyum kaku
    mc "Kebetulan banget ini tugas audit pertama gue."

    made "Ya ampun, berarti kita harus saling bantu nih."
    made "Kan dulu gue juga sering bantu lu waktu di kuliah"
    made "Sekarang giliran lu bantu gue."

    mc "Apaan nih maksudnya Made..?" #dalam hati

    narator "Made meletakkan map tebal di meja dan menatap [mc_name] dengan serius."

    made "Gue tau perusahaan gue lagi diaudit karena ada selisih laporan."
    made "Tapi, [mc_name], semua ini bisa dibicarakan baik-baik."
    made "Gue nggak mau ada masalah besar. Lo ngerti kan maksud gue?"

    jump pilihan_mc

#3 PILIHAN MC
label pilihan_mc:
    menu:
        "Bantu Made dengan senang hati": #Relasi dengan Made menurun, Moralitas membaik
            $ moral -= 1
            $ relasi_made += 1
            jump bantu_made

        "Tolak membantu Made": #Relasi dengan Made membaik, Moralitas menurun
            $ moral += 1
            $ relasi_made -= 1
            jump tolak_made

        "Ragu-ragu untuk membantu Made":
            jump ragu_made

#PILIHAN TOLAK MEMBANTU MADE
label tolak_made:
    narator "Made menatap [mc_name] lama, matanya penuh kekecewaan." 
    
    made "Lu masih sama aja ya..."
    made "Dunia itu udah berubah. Integritas nggak bisa bikin lu bertahan lama di sistem pajak gini."
    #[mc_name] menatap Made tanpa kata, lalu berdiri dan menutup map di depannya
    mc "Sebetulnya, kalau data lu bersih dari awal, nggak ada yang perlu dikhawatirkan."
    mc "Sekarang, aku harus profesional."

    narator "[mc_name] pergi meninggalkan ruangan yang sunyi."
    narator "Di luar, hujan turun pelan seperti mengiringi keputusan yang mungkin benar, tapi tidak mudah."

    narator "Beberapa minggu berlalu. Laporan audit selesai."
    narator "PT Cahaya Purnama Bakti dinyatakan bersalah atas manipulasi pajak."
    narator "Made dijatuhi hukuman penutupan usaha, sementara [mc_name] dipanggil oleh Raden Bagus ke ruangannya."

    raden "Kerja bagus, [mc_name]."
    raden "Di instansi ini, orang seperti kamu langka."
    raden "Aku ingin kamu memimpin sektor Zona Selatan"
    raden "Mulai minggu depan, kamu akan memantau Tax Counter warga di TAXNET. Semua datanya langsung di bawah pengawasanmu."
    #latar tempat berubah menjadi ruang kerja mc yang baru, tempat yang lebih besar dan nyaman
    narator "[mc_name] menatap layar besar di ruang kerjanya yang baru - ribuan nama, angka, dan warna."
    narator "Hijau artinya aman. Kuning artinya diawasi. Merah artinya... 30 hari menuju eksekusi."

    mc "Eksekusi...? Apa yang dimaksud dengan kebijakan eksekusi...?" #dalam hati termenung

    narator "Beberapa bulan kemudian, [mc_name] mulai terbiasa memantau Tax Counter warga di TAXNET."
    narator "Hingga suatu malam, nama Raras Wulandari muncul di daftar merah."
    narator "Penyebab: \"Ketidaksesuaian pelaporan gaji.\""

    narator "[mc_name] tahu Raras tidak bersalah."
    narator "Tapi untuk menyelematkannya, [mc_name] harus mengubah sistem TAXNET, dan itu merupakan aksi yang dianggap pengkhianatan."
    
    narator "[mc_name] pergi untuk menemui Raras tentang masalah ini."
    
    raras "Hah...kok bisa?? Tapi, kau tau aku bukan orang jahat, kan?"
    raras "Mereka nggak peduli data benar atau salah, sistem ini janggal!"

    mc "Sistem ini... nggak pernah salah."
    mc "Tapi yang salah mungkin... orang yang percaya penuh padanya."
    mc "Raras, aku..."

    jump pilihan_selamatkan_raras

#PILIHAN MENYELEMATKAN RARAS ATAU TIDAK
label pilihan_selamatkan_raras:
    menu:
        "Menyelamatkan Raras": #Relasi dengan Raras membaik, moral membaik
            $ relasi_raras += 2
            $ moral += 1
            jump selamatkan_raras

        "Tidak menyelematakan Raras": #Relasi dengan Raras menurun, moral menurun
            $ relasi_raras -= 2
            $ moral -= 1
            jump tidak_selamatkan_raras

#PILIHAN SELAMATKAN RARAS
label selamatkan_raras:
    narator "Lampu berkedip. Jari [mc_name] menekan perintah \"DELETE LOG\"."
    narator "Sistem berhenti beberapa detik, lalu menampilkan pesan:"
    narator "✅ Data Alomani Dihapus. Counter Raras Wulandari: 0."
    narator "Raras selamat."
    narator "Namun, di sistem keamanan pusat, ada jejak log yang mencurigakan - tanda digital yang tidak bisa dihapus sepenuhnya."

    narator "Keesokan harinya, Raras datang ke meja [mc_name]."

    raras "Aduhh [mc_name], aku nggak tau gimana, tapi tiba-tiba data pajakku normal lagi."
    raras "Kayaknya ada malaikat di kantor ini."

    mc "Tapi, bukannya Raras tahu cuman aku yang punya akses ke data internal TAXET...?" #dalam hati, tersenyum kecil, menahan rasa bersalah

    narator "Beberapa minggu kemudian, Raden Bagus memanggilnya ke ruang rapat."
    narator "Ruang itu dingin, suara mesin server bergema di dinding logam."

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

#2 PILIHAN ALASAN KE RADEN (JUJUR ATAU TIDAK)
label pilihan_alasan_ke_raden:
    menu:
        "Jujur pada Raden": #Relasi dengan Raden membaik, moral membaik
            $ moral += 1
            $ relasi_raden += 1
            jump alasan_jujur

        "Tidak jujur pada Raden": #Relasi dengan Raden menurun
            $ relasi_raden -= 2
            jump alasan_tidak_jujur

#PILIHAN JUJUR PADA RADEN
label alasan_jujur:
    mc "Saya tahu ini salah, Pak."
    mc "Tapi kalau saya biarkan, Raras akan dihapus dari sistem."
    mc "Saya cuma... nggak bisa tinggal diam."

    narator "Raden menatap [mc_name] lama. Wajahnya tenang, tapi matanya tajam, seperti sedang menimbang sesuatu yang lebih dalam dari sekadar laporan pelanggaran."

    raden "Dulu saya juga pernah melakukan hal yang sama."
    raden "Menyelamatkan seseorang berdasarkan keinginan saya sendiri." #menatap layar sejenak, lalu menutupnya
    raden "Kau sudah memilih jadi manusia, bukan mesin. Tapi mulai hari ini, kau tidak bisa lagi bekerja di sistem ini."

    mc "Saya... mengerti, Pak."

    raden "Keluar lewat pintu belakang. Aku akan hapus log terakhirmu... satu kali lagi."

    narator "[mc_name] menatap Raden dengan tatapan kosong."
    narator "Ia meninggalkan kantor dengan langkah pelan."
    narator "Di luar, sinar matahari sore memantul di gedung-gedung logam - indah tapi terasa asing."

    raras "[mc_name]! Aku dengar kamu dipindahkan ya?"
    raras "Jangan lupa kirim pesan, ya!"

    narator "[mc_name] menoleh sebentar, tersenyum kecil."
    narator "Ia kehilangan pekerjaannya, tapi menemukan kembali nuraninya."

    jump ending_honesty

#ENDING "In Honesty, Lies Clarity"
label ending_honesty:
    scene black
    with fade

    narator "ENDING: In Honesty, Lies Clarity"
    narator "Dalam dunia yang menghapus kesalahan dengan satu klik, [mc_name] memilih untuk tetap salah demi menjadi manusia."

    return

#PILIHAN TIDAK JUJUR PADA RADEN
label alasan_tidak_jujur:
    mc "Saya tahu kejanggalan dalam pekerjaan ini. Sistem ini rusak, Pak."
    mc "Saya tahu ada rahasia lebih dalam yang disembunyikan. Ada operasi tak ternama dibalik semua eksekusi itu."
    
    narator "Raden menatapnya tajam."

    raden "Kau tidak tahu apa yang kau bicarakan! Apa maksudmu?!"
    raden "Sistem sempurna ini, yang saya telah jaga selama bertahun-tahun, tidak mungkin bisa memiliki error!"

    mc "Justru karena itu saya ingin tahu."

    narator "Suara sistem menyela percakapan."
    narator "📢 ALERT: Unauthorized Access Detected - User: [mc_name]."

    narator "Lampu ruangan berkedip merah. Raden menekan tombol di mejanya, tapi layar di belakang tiba-tiba menampilkan folder tersembunyi:"
    narator "PROJECT HUMAN FILTER PROTOCOL"
    narator "Raden membeku. [mc_name] tersenyum samar."

    mc "Ternyata benar ya, Pak. Bukan sistem yang salah. Orang dibaliknya yang bermain."

    raden "Kau pikir kau bisa hentikan ini? Sistem ini lebih tua dari pemerintah itu sendiri."

    mc "Kalau begitu, saya akan mulai dari akar"

    narator "Layar TAXNET bergetar"
    narator "[mc_name] menemukan perintah baru tersembunyi di log administrator."
    #Latar: Server Room TAXNET, larut malam. Hanya lampu merah darurat yang menyala. Suara mesin berdengung berat.
    narator "Jari-jarinya bergetar saat menekan perintah tersembunyi:"
    narator "> EXECUTE: SEARCH_OVERSIGHT_PROTOCOL -admin=true"
    narator "Layar bergetar. Suara sistem berbisik, seolah-olah sadar akan perintah itu."
    narator "📢 Warning: You are accessing restricted layers. Oversight Level 0 detected."
    narator "Tiba-tiba, muncul sederet log dengan nama-nama."
    narator "Sebagian sudah diberi tanda \"TERHAPUS - SESUAI PROTOKOL\". Salah satunya adalah \"Raras Wuladari - Review Pending\", dengan catatan:"
    narator "\"Target diselamatkan. Jejak digital menyimpang. Investigasi oleh Raden B.\""
    narator "[mc_name] terdiam."

    mc "Raden... bukan hanya tahu, dia bagian dari sistem ini."

    narator "Lampu ruangan menyala tiba-tiba."
    narator "Raden berdiri di pintu, menatapnya tanpa ekspresi."

    raden "Kau tak seharusnya sampai di sini."

    mc "Jadi benar. Kau yang menghapus orang-orang itu dari sistem, bukan karena kesalahan data - tapi karena kepentingan?"
    
    narator "Raden tersenyum kecil."

    raden "Kau pikir dunia ini bisa stabil tanpa pengorbanan? Sistem ini diciptakan bukan untuk adil, tapi untuk efisien."

    narator "[mc_name] menatap layar, menekan satu perintah lagi."
    narator "> UPLOAD_ALL_TO_PUBLIC_NODE"

    raden "Jangan bodoh! Itu akan menimbulkan kekacauan!"

    mc "Lebih baik kacu... daripada salah tetap tersembunyi"

    narator "📢 Upload initiated: 5%... 20%... 60%..."
    narator "Raden menarik pistol keamanan dari sakunya, menodongkan ke arah [mc_name]."

    raden "Berhenti sekarang, atau semua akan berakhir untukmu!"

    narator "[mc_name] menatap tenang."

    mc "Sudah berakhir, Pak. Dari awal saat saya menyelamatkan Raras, saya tahu saya nggak bisa kembali lagi."

    narator "📢 Upload complete: 100%"
    narator "Layar terminal berubah menjadi putih. Semua data, semua manipulasi, semua korban Human Filter Protocol kini tersebar ke publik."
    narator "Sistem TAXNET runtuh dari dalam."

    jump epilog

#EPILOG
label epilog:
    scene black
    with dissolve

    narator "Berita di layar holo menampilkan:"
    narator "\"Skandal besar mengguncang TAXNET. Data rahasia bocor ke publik. Beberapa pejabat tinggi ditahan.\""
    narator "Raras membaca berita itu di meja kerja kecilnya."
    narator "Ia menatap foto [mc_name] di berkas lama - kini bertuliskan \"Hilang, Tidak Diketahui.\""

    raras "Kamu benar... sistem nggak bisa diselamatkan tanpa kejujuran."

    narator "Kamera menyorot server kosong TAXNET yang kini terbengkalai."
    narator "Lampu birunya berkedip sekali, lalu mati."
    narator "📢 USER LOGOUT - OVERSIGHT PROTOCOL TERMINATED."
    narator "SECRET ENDING: Veni, Vidi, Vici"
    narator "Kebenaran selalu punya harga. Terkadang, nyawa adalah bayarannya."

    return

#PILIHAN TIDAK SELAMATKAN RARAS
label tidak_selamatkan_raras:
    #Layar menampilkan hitungan mundur 02:15:47