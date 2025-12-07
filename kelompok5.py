def print_header():
    print("=" * 80)
    print("             SISTEM PAKAR DIAGNOSA KERUSAKAN MOBIL")
    print("=" * 80)
    print("Jawablah setiap pertanyaan sub-gejala (a, b, c) dengan 'y' (ya) atau 'n' (tidak).")
    print("Semua hasil diagnosa akan dirangkum di akhir.")
    print("-" * 80)

def get_input(pertanyaan):
    """Fungsi untuk memvalidasi input y/n"""
    while True:
        jawaban = input(f"{pertanyaan} (y/n): ").lower().strip()
        if jawaban in ['y', 'n']:
            return jawaban
        print("Input salah! Harap masukkan 'y' atau 'n'.")

def diagnosa_gejala_multi(pertanyaan_utama, sub_gejala, hasil_diagnosa):
    """
    Fungsi untuk menangani pertanyaan multi-cabang dan menyimpan hasilnya.
    hasil_diagnosa: list yang akan diisi dengan dict {'penyakit', 'solusi'}
    """
    print(f"\n--- {pertanyaan_utama} ---")
    
    gejala_ditemukan = False
    
    # Iterasi melalui setiap sub-gejala (a, b, c, dst.)
    for i, (pertanyaan_sub, penyakit, solusi) in enumerate(sub_gejala):
        kode_gejala = chr(ord('a') + i) # Membuat kode a, b, c
        
        if get_input(f"   {kode_gejala}. {pertanyaan_sub}") == 'y':
            # SIMPAN HASIL, BUKAN CETAK LANGSUNG
            hasil_diagnosa.append({
                'penyakit': penyakit,
                'solusi': solusi
            })
            gejala_ditemukan = True
            
    return gejala_ditemukan

def tampilkan_kesimpulan(hasil_diagnosa):
    """
    Fungsi untuk menampilkan ringkasan dan solusi lengkap di akhir proses.
    """
    print("\n\n" + "#" * 80)
    print("############### HASIL AKHIR DIAGNOSA KERUSAKAN MOBIL ###############")
    print("#" * 80)
    
    if not hasil_diagnosa:
        print("\n TIDAK ADA GEJALA KRITIS TERIDENTIFIKASI.")
        print("Saran: Lakukan servis rutin dan pemeliharaan berkala.")
        print("\n" + "#" * 80)
        return

    # 1. LIST PENYAKIT YANG DIDERITA
    print("\n DAFTAR PENYAKIT YANG TERIDENTIFIKASI:")
    for i, hasil in enumerate(hasil_diagnosa, 1):
        print(f"   {i}. **{hasil['penyakit']}**")

    print("\n" + "-" * 80)

    # 2. SOLUSI LENGKAP UNTUK SETIAP PENYAKIT
    print(" SOLUSI LENGKAP UNTUK SEMUA MASALAH:")
    
    for i, hasil in enumerate(hasil_diagnosa, 1):
        print("\n" + "=" * 80)
        print(f"[{i}] PENYAKIT: {hasil['penyakit']}")
        print("=" * 80)
        for j, langkah in enumerate(hasil['solusi'], 1):
            print(f"   {j}. {langkah}")
    
    print("\n" + "#" * 80)
    print("### DIAGNOSA SELESAI. Hubungi bengkel untuk penanganan lebih lanjut. ###")
    print("#" * 80)


def main_diagnosa():
    # Daftar untuk menampung semua hasil diagnosa
    hasil_diagnosa = [] 

    # --- DEFINISI KASUS ---
    # Daftar kasus dan sub-gejala yang sama dari versi sebelumnya
    daftar_kasus = [
        # KASUS 1: MASALAH STARTING
        ("1. Apakah ada masalah saat MENYALAKAN (STARTING) mobil?", [
            ("Terdengar bunyi 'klik-klik' saat kunci diputar?", 
             "Starter Motor/Solenoid Bermasalah", ["Cek tegangan aki. Periksa kabel koneksi starter. Coba ketuk motor starter. Servis/ganti motor starter."]),
            ("Lampu dashboard redup/mati dan tidak ada suara mesin berputar?", 
             "Aki Soak atau Koneksi Kotor", ["Bersihkan terminal aki. Kencangkan baut. Lakukan Jump Start. Jika mati lagi, Alternator bermasalah."]),
            ("Mesin berputar (cranking) kuat, tapi tidak mau menyala?", 
             "Sistem Bahan Bakar/Pengapian Terganggu", ["Cek sekring pompa bensin. Periksa kondisi Busi dan Koil. Dengarkan bunyi pompa bensin saat kunci ON."])
        ]),
        
        # KASUS 2: MASALAH PENDINGINAN
        ("2. Apakah temperatur mesin NAIK TINGGI (OVERHEAT)?", [
            ("Suhu naik cepat, tapi radiator hose (selang) dingin?",
             "Termostat Macet Tertutup/Air Radiator Kurang", ["BERHENTI SEGERA. Cek air radiator (setelah dingin). Ganti Termostat jika macet."]),
            ("Suhu naik saat macet, tapi normal saat jalan cepat?",
             "Kipas Radiator (Extra Fan) Mati", ["Periksa motor kipas. Cek sekring/relay kipas. Ganti kipas jika tidak berputar."]),
            ("Ada rembesan air/uap dari ruang mesin?",
             "Kebocoran Sistem Pendinginan", ["Cari kebocoran pada selang, klem, atau tutup radiator. Cek Gasket Cylinder Head jika parah."])
        ]),

        # KASUS 3: MASALAH REM
        ("3. Apakah ada masalah serius saat MELAKUKAN PENGEREMAN?", [
            ("Pedal rem terasa bergetar naik-turun (pulsasi) saat diinjak?", 
             "Piringan Cakram (Disc Rotor) Tidak Rata", ["Lakukan pembubutan (resurfacing) cakram. Ganti cakram jika terlalu tipis."]),
            ("Pedal rem terasa DALAM atau 'kosong' saat diinjak?", 
             "Masuk Angin (Udara) atau Kebocoran Minyak Rem", ["JANGAN JALAN. Segera cek minyak rem. Lakukan proses 'Bleeding' rem. Cari dan perbaiki kebocoran."]),
            ("Terdengar bunyi mencicit/gesekan logam saat rem diinjak?", 
             "Kampas Rem Tipis/Habis", ["Segera ganti kampas rem depan/belakang. Periksa piringan cakram."])
        ]),

        # KASUS 4: MASALAH KNALPOT / EMISI
        ("4. Apakah keluar ASAL TEBAL atau BAU ANEH dari knalpot?", [
            ("Asap berwarna PUTIH kebiruan?", 
             "Pembakaran Oli (Ring Piston/Seal Klep Rusak)", ["Cek level oli mesin. Perbaikan wajib: Ganti ring piston atau seal klep."]),
            ("Asap berwarna HITAM pekat dan bau bensin?", 
             "Pembakaran Terlalu Kaya (Over-Fueling)", ["Cek Filter Udara. Bersihkan/ganti sensor O2 dan MAF. Cek injektor yang bocor."]),
            ("Bau bensin kuat di luar mobil setelah parkir?", 
             "Kebocoran Sistem Bahan Bakar", ["Cek visual di sekitar tangki dan selang-selang bensin. Segera perbaiki kebocoran."])
        ]),

        # KASUS 5: MASALAH KELISTRIKAN/PENGISIAN
        ("5. Apakah ada indikasi MASALAH KELISTRIKAN atau pengisian daya?", [
            ("Aki sering tekor meskipun mobil sering dipakai?",
             "Alternator (Dinamo Isi) Rusak", ["Cek tegangan pengisian (harus 13.8V-14.2V). Ganti carbon brush atau IC Regulator alternator."]),
            ("Lampu 'Check Engine' atau Lampu Oli menyala?",
             "Sensor/Tekanan Oli Bermasalah", ["Lakukan Scan ECU (OBD2) untuk Check Engine. Jika Lampu Oli, SEGERA MATIKAN MESIN dan cek level oli."]),
            ("Ada perangkat kelistrikan (Wiper/Lampu) yang mati total?",
             "Sekring (Fuse) Putus atau Relay Rusak", ["Periksa kotak sekring, ganti sekring yang putus dengan ukuran ampere yang SAMA."])
        ]),
        
        # KASUS 6: MASALAH GETARAN MESIN
        ("6. Apakah mesin terasa BERGETAR HEBAT atau 'brebet'?", [
            ("Getaran parah saat langsam (idle) atau RPM rendah?", 
             "Mounting Mesin (Engine Mounting) Rusak", ["Ganti mounting mesin yang rusak atau sudah keras."]),
            ("Getaran saat akselerasi atau suara mesin tidak rata?", 
             "Pengapian atau Bahan Bakar Tidak Sempurna (Misfire)", ["Periksa Busi, Koil, dan kabel busi. Bersihkan Throttle Body dan Injektor."]),
            ("Mobil bergetar hebat di kecepatan tinggi (>80 km/jam)?", 
             "Ban Tidak Balance atau Pelek Peyang", ["Lakukan spooring dan balancing roda di bengkel."])
        ]),

        # KASUS 7: MASALAH AC (AIR CONDITIONER)
        ("7. Apakah AC mobil tidak dingin atau bermasalah?", [
            ("AC tidak dingin dan ada suara desis/angin keras?", 
             "Freon Habis atau Bocor", ["Lakukan pengecekan Freon di bengkel AC. Cari dan perbaiki kebocoran."]),
            ("AC tidak dingin dan Kompresor tidak menyala (tidak ada bunyi 'klak')?", 
             "Kompresor/Kopling Magnet Rusak", ["Cek sekring AC. Periksa tekanan freon. Ganti Kompresor jika fatal."]),
            ("AC dingin tapi aliran udara dari ventilasi sangat lemah?", 
             "Filter Kabin Sangat Kotor", ["Ganti atau bersihkan Filter Kabin (filter AC). Cek motor Blower AC."])
        ]),

        # KASUS 8: MASALAH KAKI-KAKI/SUSPENSI
        ("8. Apakah terdengar BUNYI ANEH dari bagian bawah mobil saat jalan?", [
            ("Bunyi 'gluduk-gluduk' saat melewati jalan rusak/polisi tidur?", 
             "Kerusakan Shockbreaker atau Bushing Arm", ["Periksa Shockbreaker (rembesan oli). Ganti karet Bushing Arm atau Link Stabilizer."]),
            ("Bunyi 'krek-krek' saat berbelok tajam (khusus penggerak depan)?", 
             "CV Joint (Kopel As Roda) Rusak", ["Periksa karet boot CV Joint. Segera ganti CV Joint jika bunyi semakin keras."]),
            ("Bunyi mencicit seperti kasur pegas di jalan bergelombang?", 
             "Karet Stabilizer atau Bushing Per (Belakang) Aus", ["Lumasi atau ganti karet stabilizer/bushing per."])
        ]),

        # KASUS 9: MASALAH KOPLING/TRANSMISI MANUAL
        ("9. Khusus Transmisi Manual: Apakah ada masalah dengan kopling/perpindahan gigi?", [
            ("Kopling 'nggantung' dan mesin meraung tapi mobil lambat (slip)?", 
             "Kampas Kopling (Clutch Plate) Habis", ["Segera ganti set kopling lengkap (kampas, matahari, deklaher)."]),
            ("Pedal kopling terasa sangat keras atau sulit masuk gigi?", 
             "Master Kopling atau Kabel Kopling Bermasalah", ["Cek level minyak kopling. Ganti Master Kopling Atas/Bawah (hidrolik) atau setel/ganti kabel kopling."]),
            ("Gigi transmisi mental/lompat saat akselerasi?", 
             "Kerusakan Internal Transmisi/Bushing Tuas", ["Periksa oli transmisi. Perbaikan wajib: Bongkar transmisi untuk perbaikan Synchronizer Ring/gigi."])
        ]),

        # KASUS 10: MASALAH SUARA ANEH MESIN
        ("10. Apakah terdengar BUNYI ANEH dari mesin saat idle?", [
            ("Bunyi 'cit-cit' seperti karet berdecit?", 
             "Fan Belt/V-Belt Kendor atau Aus", ["Kencangkan tensioner Fan Belt. Ganti belt jika sudah retak."]),
            ("Bunyi 'ketek-ketek' dari bagian atas mesin?", 
             "Setelan Klep Longgar atau Lifter Aus", ["Cek level oli. Lakukan setel klep manual. Periksa Hydraulic Valve Lifter (HLV) jika mobil hidrolik."]),
            ("Bunyi 'nguung' seperti mesin jet saat akselerasi?", 
             "Bearing Roda atau Bearing Pompa Air/Alternator Rusak", ["Tentukan sumber bunyi: jika berubah saat berbelok, itu bearing roda; jika konstan, cek bearing pompa/alternator."])
        ]),

        # KASUS 11: MASALAH POWER STEERING
        ("11. Apakah setir (kemudi) terasa berat atau tidak responsif?", [
            ("Setir terasa berat tiba-tiba (khusus hidrolik)?", 
             "Oli Power Steering Kurang atau Pompa Lemah", ["Cek level oli power steering. Cari kebocoran. Cek kondisi V-Belt pompa."]),
            ("Setir terasa kaku/berat dan ada bunyi aneh dari bagian setir?", 
             "Rack Steer atau Tie Rod Rusak", ["Periksa Rack Steer dari kebocoran/oblask. Ganti Tie Rod End/Long Tie Rod."]),
            ("Lampu indikator EPS menyala (khusus elektrik)?", 
             "Kerusakan Sistem EPS", ["Lakukan scan error EPS di bengkel untuk mengetahui kode error spesifik."])
        ]),

        # KASUS 12: MASALAH REM TANGAN/PARKIR
        ("12. Apakah rem tangan (parkir) tidak berfungsi optimal?", [
            ("Rem tangan sudah ditarik tinggi, tapi mobil masih bisa bergerak?", 
             "Setelan Rem Tangan Kendor", ["Lakukan penyetelan ulang kabel rem tangan (biasanya di konsol tengah atau roda belakang)."]),
            ("Rem tangan macet dan sulit dilepas?", 
             "Kabel Rem Tangan Berkarat/Seret", ["Lumasi kabel rem tangan. Ganti jika sudah parah."]),
            ("Ada bunyi 'ngiik-ngiik' dari roda belakang saat berjalan perlahan?", 
             "Setelan Rem Tromol Terlalu Rapat", ["Setel ulang jarak kampas rem tromol."])
        ]),

        # KASUS 13: MASALAH BENSIN (PERFORMA)
        ("13. Apakah mobil terasa berat/tenaga hilang saat di gas?", [
            ("Tenaga hilang mendadak saat kecepatan tinggi?", 
             "Pompa Bensin Lemah/Filter Bensin Mampet", ["Ganti filter bensin. Cek tekanan pompa bensin. Ganti pompa bensin jika tekanan drop."]),
            ("Akselerasi lambat dan terasa 'ngok' di awal gas?", 
             "Filter Udara Kotor atau Sensor MAF/MAP Rusak", ["Bersihkan/ganti Filter Udara. Bersihkan atau ganti sensor MAF/MAP."]),
            ("Mobil sulit mencapai kecepatan tertentu di tanjakan?", 
             "Catalytic Converter Mampet", ["Lakukan pembersihan/flushing Catalytic Converter. Ganti jika sudah fatal."])
        ]),

        # KASUS 14: MASALAH BODI/PINTU
        ("14. Apakah ada masalah pada Power Window atau Central Lock?", [
            ("Jendela Power Window bergerak lambat atau macet?", 
             "Motor Power Window Lemah/Rel Berkarat", ["Lumasi rel kaca dengan pelumas silikon. Cek motor power window."]),
            ("Central Lock (kunci pintu otomatis) tidak berfungsi/terkunci kembali?", 
             "Actuator Central Lock Rusak atau Sekring Putus", ["Periksa sekring central lock. Ganti Actuator pintu yang bermasalah."]),
            ("Lampu di dashboard berkedip saat menyalakan lampu besar?", 
             "Kabel/Massa (Grounding) Kelistrikan Kurang Baik", ["Periksa dan bersihkan semua koneksi massa (grounding) di bodi dan mesin."])
        ]),

        # KASUS 15: MASALAH TRANSMISI MATIC
        ("15. Khusus Transmisi Matic: Apakah ada masalah saat perpindahan gigi?", [
            ("Perpindahan gigi terasa 'jedug' atau hentakan kuat?", 
             "Oli Transmisi Kotor/Kualitas Menurun", ["Lakukan kuras Oli Transmisi Otomatis (ATF). Cek Engine Mounting."]),
            ("Gigi tertahan di satu posisi (tidak mau pindah ke atas)?", 
             "Kerusakan Valve Body atau Solenoid Transmisi", ["Lakukan Scan Transmisi untuk kode error. Perbaikan wajib: Bongkar Valve Body."]),
            ("Ada suara mendengung dari transmisi matic?", 
             "Bearing Transmisi Rusak atau Level Oli Kurang", ["Cek level oli ATF (saat mesin panas). Periksa bearing internal transmisi."])
        ])
    ]

    # Menjalankan Diagnosa Berdasarkan Daftar Kasus
    for pertanyaan_utama, sub_gejala_list in daftar_kasus:
        diagnosa_gejala_multi(pertanyaan_utama, sub_gejala_list, hasil_diagnosa)

    # Menampilkan Kesimpulan Setelah Semua Pertanyaan Selesai
    tampilkan_kesimpulan(hasil_diagnosa)

def main_loop():
    while True:
        main_diagnosa()
        
        print("\n" + "~" * 80)
        ulang = input("Apakah Anda ingin melakukan diagnosa lagi? (y/n) atau ketik 'exit' untuk keluar: ").lower().strip()
        print("~" * 80 + "\n")
        
        if ulang == 'n' or ulang == 'exit':
            print("Terima kasih telah menggunakan Sistem Diagnosa Kerusakan Mobil. Semoga perjalanan Anda lancar!")
            break

if __name__ == "__main__":
    main_loop()


    ##Tentu, ini adalah ringkasan lengkap mengenai program diagnosa kerusakan mobil yang telah Anda buat.

## Ringkasan Program Diagnosa Kerusakan Mobil

##Program Python ini berfungsi sebagai **Sistem Pakar Sederhana** yang dirancang untuk membantu pengguna mengidentifikasi potensi kerusakan pada mobil berdasarkan gejala-gejala yang dialami.

### 1.  Struktur Logika Program

##Program menggunakan pendekatan **Pohon Keputusan Multi-Cabang**, tetapi dengan mekanisme output yang disatukan di akhir.

##* **Input Non-Stop:** Pengguna akan melalui **15 pertanyaan utama** secara berurutan. Di setiap pertanyaan utama, terdapat hingga **3 sub-gejala (a, b, c)** yang harus dijawab dengan 'y' (ya) atau 'n' (tidak).
##* **Pengumpulan Data:** Hasil diagnosa **tidak langsung ditampilkan**. Setiap kali pengguna menjawab 'y' pada sub-gejala, informasi detail tentang **Penyakit** dan **Solusi** disimpan ke dalam *list* bernama `hasil_diagnosa`.
##* **Looping Utama:** Fungsi `main_loop()` memungkinkan pengguna untuk mengulang seluruh proses diagnosa atau memilih untuk keluar (`exit`).

### 2.  Komponen dan Fungsi Utama

#| Fungsi Utama              | Peran                                                                                                                                             |
#| :---                      | :---                                                                                                                                              |
#| `print_header()`          | Menampilkan judul dan instruksi program.                                                                                                          |
#| `get_input()`             | Memvalidasi input pengguna, memastikan hanya 'y' atau 'n' yang diterima.                                                                          |
#| `diagnosa_gejala_multi()` | Fungsi inti yang menyajikan pertanyaan multi-cabang (15 kasus utama), menerima input, dan **menyimpan hasil diagnosa** ke dalam `hasil_diagnosa`. |
#| `tampilkan_kesimpulan()`  | Fungsi output final. Mengambil semua data dari `hasil_diagnosa` untuk menampilkan ringkasan di akhir.                                             |
#| `main_diagnosa()`         | Menginisialisasi `hasil_diagnosa` dan memanggil semua pertanyaan (`daftar_kasus`).                                                                |

#---

### 3.  Fokus Diagnosa

#Program ini mencakup berbagai sistem mobil, dengan total **45 potensi diagnosa** yang dikelompokkan ke dalam 15 kategori utama, meliputi:

#| Kategori Utama                   | Contoh Penyakit                                           |
#| :---                             | :---                                                      |
#| **Starting** (Menghidupkan)      | Starter rusak, Aki soak, Masalah Pompa Bensin.            |
#| **Pendinginan**                  | Overheat, Kipas Mati, Termostat Macet.                    |
#| **Rem**                          | Piringan Cakram Tidak Rata, Kebocoran Minyak Rem.         |
#| **Emisi/Knalpot**                | Asap Putih (bakar oli), Asap Hitam (boros bensin).        |
#| **Kelistrikan**                  | Alternator rusak, Sekring putus, Sensor Tekanan Oli.      |
#| **Getaran Mesin**                | Mounting mesin rusak, Misfire (pengapian/bahan bakar).    |
#| **AC**                           | Freon habis, Kompresor/Kopling Magnet rusak.              |
#| **Suspensi/Kaki-kaki**           | Bunyi 'Gluduk-gluduk', CV Joint rusak.                    |
#| **Transmisi (Manual/Matic)**     | Kopling slip, Gigi mental, Matic 'jedug' (Valve Body).    |
#| **Performa Bensin**              | Pompa bensin lemah, Catalytic Converter mampet.           |

### 4.  Format Kesimpulan (Output)

#Jika ada satu atau lebih gejala yang dijawab 'y', output di akhir akan terbagi menjadi dua bagian yang jelas:

#1.  **Daftar Penyakit:** Daftar singkat semua masalah yang teridentifikasi.
#2.  **Solusi Lengkap:** Setiap masalah diulang dan diikuti oleh langkah-langkah perbaikan yang detail dan terperinci.

#Program ini kini sangat **komprehensif** dan dirancang untuk memberikan pengalaman diagnostik yang terstruktur.#