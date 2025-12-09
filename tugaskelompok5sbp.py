def print_header():
    print("=" * 60)
    print("       SISTEM PAKAR DIAGNOSA KERUSAKAN MOBIL")
    print("=" * 60)
    print("Jawablah pertanyaan berikut dengan 'y' (ya) atau 'n' (tidak).")
    print("-" * 60)

def get_input(pertanyaan):
    """Fungsi untuk memvalidasi input y/n"""
    while True:
        jawaban = input(f"{pertanyaan} (y/n): ").lower().strip()
        if jawaban in ['y', 'n']:
            return jawaban
        print("Input salah! Harap masukkan 'y' atau 'n'.")

def tampilkan_solusi(penyakit, solusi):
    print("\n" + "=" * 60)
    print("HASIL DIAGNOSA:")
    print(f"Penyakit Teridentifikasi: {penyakit}")
    print("-" * 60)
    print("SOLUSI LENGKAP:")
    for i, langkah in enumerate(solusi, 1):
        print(f"{i}. {langkah}")
    print("=" * 60)

def main():
    print_header()

    # --- CABANG 1: MASALAH STARTING (MESIN TIDAK HIDUP) ---
    if get_input("Apakah mobil sulit di-starter atau tidak mau hidup sama sekali?") == 'y':
        
        if get_input("Apakah terdengar bunyi 'klik-klik' saat kunci diputar?") == 'y':
            tampilkan_solusi(
                "Masalah pada Starter Motor atau Solenoid",
                [
                    "Cek tegangan aki, pastikan tidak drop.",
                    "Periksa kabel koneksi ke motor starter (kemungkinan kendor/korosi).",
                    "Coba ketuk perlahan body motor starter dengan kunci pas (terkadang brush macet).",
                    "Jika tetap tidak bisa, motor starter perlu diservis atau diganti."
                ]
            )
        elif get_input("Apakah lampu dashboard redup/mati dan tidak ada suara mesin berputar?") == 'y':
            tampilkan_solusi(
                "Aki (Battery) Soak atau Koneksi Kotor",
                [
                    "Periksa terminal aki, bersihkan jika ada jamur putih (korosi).",
                    "Kencangkan baut terminal aki.",
                    "Lakukan 'Jump Start' menggunakan kabel jumper dengan mobil lain.",
                    "Jika mobil menyala lalu mati lagi, kemungkinan Alternator (pengisian) rusak.",
                    "Ganti aki jika usia sudah lebih dari 2 tahun."
                ]
            )
        elif get_input("Mesin berputar (cranking) kuat, tapi tidak mau menyala?") == 'y':
            tampilkan_solusi(
                "Masalah Sistem Bahan Bakar atau Pengapian",
                [
                    "Pastikan bensin terisi (indikator bensin bisa saja rusak).",
                    "Cek sekring (fuse) pompa bensin.",
                    "Periksa kondisi Busi dan Koil (apakah ada percikan api).",
                    "Dengarkan bunyi dengung pompa bensin di tangki saat kunci kontak 'ON'. Jika hening, pompa bensin mungkin mati."
                ]
            )
        else:
            print("\nMaaf, gejala terlalu kompleks. Segera hubungi bengkel terdekat.")

    # --- CABANG 2: MASALAH PERFORMA & SUHU ---
    elif get_input("Apakah temperatur mesin naik tinggi (Overheat)?") == 'y':
        

[Image of car radiator cap]

        tampilkan_solusi(
            "Sistem Pendinginan Bermasalah (Overheat)",
            [
                "BERHENTI SEGERA! Jangan paksa jalan.",
                "Tunggu mesin dingin (minimal 30 menit) sebelum membuka tutup radiator.",
                "Periksa volume air radiator (coolant) di reservoir tank.",
                "Cek apakah kipas radiator berputar saat mesin panas.",
                "Periksa kebocoran pada selang-selang radiator.",
                "Cek kondisi Fan Belt (tali kipas), pastikan tidak putus."
            ]
        )

    # --- CABANG 3: MASALAH PENGEREMAN ---
    elif get_input("Apakah ada masalah saat melakukan pengereman (bunyi/getar)?") == 'y':
        if get_input("Terdengar bunyi mencicit (squealing) saat rem diinjak?") == 'y':
            tampilkan_solusi(
                "Kampas Rem (Brake Pads) Tipis/Habis",
                [
                    "Segera ganti kampas rem depan/belakang.",
                    "Periksa piringan cakram (disc brake), jika baret perlu dibubut.",
                    "Bersihkan sistem rem dari debu kotoran."
                ]
            )
        elif get_input("Pedal rem terasa bergetar naik-turun saat diinjak?") == 'y':
            tampilkan_solusi(
                "Piringan Cakram (Disc Rotor) Tidak Rata/Gelombang",
                [
                    "Lakukan pembubutan (resurfacing) pada piringan cakram.",
                    "Ganti piringan cakram jika sudah terlalu tipis.",
                    "Pastikan baut roda dikencangkan dengan torsi yang rata."
                ]
            )
        else:
            print("\nMasalah rem tidak spesifik. Periksa ke bengkel demi keselamatan.")

    # --- CABANG 4: MASALAH KAKI-KAKI & STABILITAS ---
    elif get_input("Apakah ada bunyi 'gluduk-gluduk' saat melewati jalan rusak?") == 'y':
        tampilkan_solusi(
            "Kerusakan Suspensi / Kaki-kaki",
            [
                "Periksa Shockbreaker (apakah ada rembesan oli).",
                "Cek kondisi Bushing Arm (karet-karet penyangga).",
                "Periksa Link Stabilizer dan Tie Rod End.",
                "Lakukan spooring dan balancing setelah penggantian part."
            ]
        )
    
    # --- CABANG 5: MASALAH INDIKATOR ---
    elif get_input("Apakah lampu 'Check Engine' menyala di dashboard?") == 'y':
        

[Image of car dashboard warning lights]

        tampilkan_solusi(
            "Sensor Mesin Mendeteksi Error",
            [
                "Periksa tutup tangki bensin (kadang tutup kendor memicu sensor).",
                "Periksa volume oli mesin dan air radiator.",
                "Cabut kepala aki negatif (-) selama 5 menit untuk mereset ECU (sementara).",
                "Solusi Paling Tepat: Lakukan Scan ECU menggunakan alat OBD2 Scanner di bengkel untuk mengetahui kode error spesifik."
            ]
        )

    else:
        print("\nSistem tidak mengenali gejala tersebut.")
        print("Saran: Lakukan servis berkala atau konsultasi dengan mekanik profesional.")

if __name__ == "__main__":
    main()