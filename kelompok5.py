import os
import time

class CarDiagnosticSystem:
    def __init__(self):
        #  untuk menyimpan riwayat diagnosa
        self.history = []
        
        # --- basis pengetahuan umum ---
        self.general_questions = [
            {"tanya": "Apakah mesin sulit dinyalakan/bunyi tek-tek?", "masalah": "Aki/Starter Lemah", "solusi": "Cek Aki & Dinamo Starter"},
            {"tanya": "Apakah indikator Check Engine menyala?", "masalah": "Sensor Malfungsi/Engine Trouble", "solusi": "Scan OBD"},
            {"tanya": "Bunyi berdecit saat mengerem?", "masalah": "Kampas Rem Tipis/Kotor", "solusi": "Bersihkan/Ganti Kampas Rem"},
            {"tanya": "Setir bergetar di kecepatan tinggi?", "masalah": "Ban tidak Balance", "solusi": "Balancing & Spooring"},
            {"tanya": "Mobil lari kiri/kanan saat setir dilepas?", "masalah": "Spooring Meleset/Rack Steer", "solusi": "Lakukan Spooring & Cek Rack"},
            {"tanya": "Asap knalpot warna biru?", "masalah": "Ring Piston Aus (Oli Terbakar)", "solusi": "Overhaul Mesin"},
            {"tanya": "Suhu mesin naik diatas setengah/Overheat?", "masalah": "Sistem Pendingin (Radiator)", "solusi": "Cek Radiator, Kipas & Thermostat"},
            {"tanya": "Bunyi gluduk-gluduk di jalan rusak?", "masalah": "Kaki-kaki (Shock/Link Stabilizer)", "solusi": "Servis Kaki-kaki"},
            {"tanya": "AC tidak dingin (hanya angin)?", "masalah": "Magnetic Clutch/Freon", "solusi": "Servis AC"},
        ]

       # --- Basis Pengetahuan Spesifik ---
        self.brand_specific_questions = {
            "HONDA": [
                {"tanya": "Bunyi 'kletek-kletek' pada setir saat jalan keriting?", "masalah": "Rack Steer (EPS) Lemah", "solusi": "Servis/Ganti Bushing Rack Steer"},
                {"tanya": "Getaran mesin terasa kuat sampai kabin saat diam?", "masalah": "Engine Mounting Jebol", "solusi": "Ganti Engine Mounting Kanan/Kiri"}
            ],
            "TOYOTA": [
                {"tanya": "RPM sering drop/ngedrop saat AC nyala?", "masalah": "Throttle Body Kotor/ISC", "solusi": "Bersihkan Throttle Body & Idle Learning"},
                {"tanya": "Terdengar bunyi 'ngelitik' (knocking) saat tanjakan?", "masalah": "Bahan Bakar Tidak Sesuai", "solusi": "Gunakan BBM Oktan Tinggi/Carbon Clean"}
            ],
            "NISSAN": [
                {"tanya": "Tenaga hilang total saat panas (Limp Mode)?", "masalah": "Overheat Transmisi CVT", "solusi": "Pasang Oil Cooler Tambahan/Ganti Oli CVT"},
                {"tanya": "Bunyi dengung kasar dari roda?", "masalah": "Wheel Bearing", "solusi": "Ganti Bearing Roda"}
            ],
            "WULING": [
                {"tanya": "Setir terasa speleng/bunyi cetek-cetek?", "masalah": "Steering Rack Housing", "solusi": "Cek Rack Steer Assembly"},
                {"tanya": "Indikator ABS menyala tiba-tiba?", "masalah": "Sensor ABS Kotor/Rusak", "solusi": "Bersihkan Sensor Roda"}
            ],
            # --- TAMBAHAN BARU ---
            "BMW": [
                {"tanya": "Plafon/Interior terasa lengket/turun?", "masalah": "Lem Plafon Usia Lanjut", "solusi": "Retrim Plafon"},
                {"tanya": "Ada warning 'Coolant Low' padahal air penuh?", "masalah": "Sensor Level Air Radiator Error", "solusi": "Ganti Sensor Level/Tabung Reservoir"}
            ],
            # Gunakan spasi pada Key agar cocok jika user mengetik "Land Rover"
            "LANDROVER": [ 
                {"tanya": "Suspensi udara terasa keras/tidak rata?", "masalah": "Kompressor Air Sus Rusak/Bocor", "solusi": "Cek Kompressor & Balon Suspensi"},
                {"tanya": "Lampu warning 'Suspension Fault' menyala?", "masalah": "Sensor Ketinggian Error", "solusi": "Kalibrasi Ulang Sensor"}
            ],
            "SUZUKI": [
                {"tanya": "Bunyi 'krek-krek' saat belok tajam?", "masalah": "As Roda/CV Joint Aus", "solusi": "Ganti CV Joint/As Roda"},
                {"tanya": "Mesin brebet/ndut-ndutan?", "masalah": "Coil/Busi atau Sensor Oksigen", "solusi": "Tune Up & Cek Pengapian"}
            ],
            "MITSUBISHI": [
                {"tanya": "AC berbau apek saat baru nyala?", "masalah": "Evaporator Kotor/Jamur", "solusi": "Cuci Evaporator & Ganti Filter Kabin"},
                {"tanya": "Bunyi jedug saat oper gigi (Matic)?", "masalah": "Oli Transmisi Kotor/Mounting Transmisi", "solusi": "Ganti Oli Matic/Cek Mounting"}
            ]
        }

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # --- LOGIKA DIAGNOSA TRANSMISI (DIPERDALAM) ---
    def get_transmission_questions(self, trans_type):
        if trans_type == 'M': # Manual
            return [
                {"tanya": "Bau hangus menyengat saat tanjakan/setengah kopling?", "masalah": "Kampas Kopling Terbakar", "solusi": "Dinginkan Kopling/Ganti Kampas"},
                {"tanya": "Pedal kopling terasa ambles/kosong?", "masalah": "Master Kopling Bocor", "solusi": "Ganti Master Kopling Atas/Bawah"},
                {"tanya": "Gigi susah masuk terutama gigi 1 atau Mundur?", "masalah": "Sinkronis Gigi Aus", "solusi": "Overhaul Gearbox"}
            ]
        elif trans_type == 'CVT': # Continuous Variable Transmission
            return [
                {"tanya": "RPM naik tinggi tapi kecepatan tidak bertambah (Rubber Band Effect)?", "masalah": "Belt CVT Slip Parah", "solusi": "Ganti Belt & Pulley CVT"},
                {"tanya": "Terasa hentakan kasar (jedug) saat pindah dari N ke D/R?", "masalah": "Body Valve Kotor/Solenoid Macet", "solusi": "Flushing Oli Matic/Bersihkan Body Valve"},
                {"tanya": "Ada bunyi 'nging' (whining) yang mengikuti putaran mesin?", "masalah": "Pompa Oli Transmisi/Bearing", "solusi": "Cek Pompa Oli CVT"}
            ]
        elif trans_type == 'DCT': # Dual Clutch Transmission (Ford/VW/Hyundai)
            return [
                {"tanya": "Mobil bergetar (shudder) saat macet-macetan/stop-n-go?", "masalah": "Kopling Ganda (Dual Clutch) Panas/Aus", "solusi": "Adaptasi Software/Ganti Clutch Pack"},
                {"tanya": "Terdengar bunyi besi beradu (klotok) saat pindah gigi rendah?", "masalah": "Garpu Pemindah (Shift Fork) Oblak", "solusi": "Cek Shift Fork/TCM"},
                {"tanya": "Gigi loncat atau hilang (misal dari 1 langsung 3)?", "masalah": "Mechatronic Error", "solusi": "Servis Mechatronic Unit"}
            ]
        return []

    # --- LOGIKA DIAGNOSA MERK ---
    def get_brand_questions(self, brand_input):
        # Normalisasi input agar cocok dengan key dictionary (misal: "Honda Jazz" -> check "HONDA")
        brand_input = brand_input.upper()
        
        # Cek apakah salah satu key ada di dalam input user
        for key in self.brand_specific_questions:
            if key in brand_input:
                return self.brand_specific_questions[key]
        
        # Kembalikan list kosong jika merk tidak dikenal/tidak ada data khusus
        return [] 

    def process_diagnosis(self, existing_name=None, existing_trans=None, existing_brand=None):
        self.clear_screen()
        print("--- INPUT DATA DIAGNOSA ---")
        
        # 1. Input Nama
        if existing_name:
            print(f"Edit Data: {existing_name}")
            nama = existing_name
        else:
            nama = input("Masukkan Nama Pemilik: ")

        # 2. Input Merk (BARU)
        if existing_brand:
            print(f"Merk Mobil: {existing_brand}")
            merk = existing_brand
        else:
            print("\nMerk Populer: Honda, Toyota, Nissan, Wuling, BMW, LandRover(tanpa spasi1), Suzuki, Mitsubishi")
            merk = input("Masukkan Merk & Tipe Mobil (Misal: Honda Jazz): ")

        # 3. Input Transmisi
        if existing_trans:
             trans_choice = existing_trans
        else:
            while True:
                print("\nPilih Jenis Transmisi:")
                print("[M]   Manual (Gigi tangan/kopling)")
                print("[CVT] Matic CVT (Honda/Toyota modern/Nissan)")
                print("[DCT] Dual Clutch (Ford Fiesta/VW/Mobil Eropa/Hyundai)")
                trans_choice = input("Pilihan (M/CVT/DCT): ").upper()
                if trans_choice in ['M', 'CVT', 'DCT']: break
                print("Input salah! Masukkan kode dalam kurung siku.")

        print(f"\nDiagnosa dimulai untuk {nama} - {merk} ({trans_choice})...")
        print("Jawab: 'y' (Ya), 't' (Tidak), 'idk' (Tak Tau)")
        print("-" * 50)

        # MENGGABUNGKAN SEMUA PERTANYAAN
        # Urutan: Pertanyaan Merk Khusus -> Pertanyaan Transmisi -> Pertanyaan Umum
        questions_sequence = []
        
        # A. Pertanyaan Merk
        brand_q = self.get_brand_questions(merk)
        if brand_q:
            print(f"[INFO] Mendeteksi merk {merk}, memuat pertanyaan spesifik...")
            questions_sequence += brand_q
            
        # B. Pertanyaan Transmisi
        questions_sequence += self.get_transmission_questions(trans_choice)
        
        # C. Pertanyaan Umum
        questions_sequence += self.general_questions

        found_problems = []
        
        for i, item in enumerate(questions_sequence, 1):
            while True:
                ans = input(f"{i}. {item['tanya']} (y/t/idk): ").lower()
                if ans in ['y', 't', 'idk']: break
            
            if ans == 'y':
                found_problems.append(item)
            elif ans == 'idk':
                found_problems.append({"masalah": f"Kemungkinan {item['masalah']}", "solusi": f"CEK MANUAL: {item['solusi']}"})

        return {
            "nama": nama,
            "merk": merk, # Simpan merk
            "transmisi": trans_choice,
            "diagnosa": found_problems,
            "waktu": time.strftime("%Y-%m-%d %H:%M:%S")
        }

    # --- MANAJEMEN SESI ---
    def new_session(self):
        result = self.process_diagnosis()
        self.history.append(result)
        self.print_report(result)
        input("\nData tersimpan! Tekan Enter kembali ke menu...")

    def print_report(self, data):
        self.clear_screen()
        print("=" * 60)
        print(f"LAPORAN HASIL DIAGNOSA")
        print("=" * 60)
        print(f"Nama      : {data['nama']}")
        print(f"Kendaraan : {data['merk']} ({data['transmisi']})") # Tampilkan merk
        print(f"Waktu     : {data['waktu']}")
        print("-" * 60)
        
        if not data['diagnosa']:
            print("HASIL: Kondisi mobil Prima/Tidak ada keluhan signifikan.")
        else:
            print(f"Ditemukan {len(data['diagnosa'])} Potensi Masalah:\n")
            for i, d in enumerate(data['diagnosa'], 1):
                print(f"{i}. INDIKASI: {d['masalah']}")
                print(f"   SOLUSI  : {d['solusi']}")
                print("-" * 30)

    # --- RIWAYAT & EDIT ---
    def history_menu(self):
        while True:
            self.clear_screen()
            print("=== RIWAYAT DATA DIAGNOSA ===")
            if not self.history:
                print("Belum ada data.")
                input("\nTekan Enter kembali...")
                return

            print(f"{'No':<4} {'Nama':<12} {'Merk':<12} {'Trans':<6} {'Masalah'}")
            print("-" * 60)
            for i, item in enumerate(self.history):
                jml = len(item['diagnosa'])
                merk_short = (item['merk'][:10] + '..') if len(item['merk']) > 10 else item['merk']
                print(f"{i+1:<4} {item['nama']:<12} {merk_short:<12} {item['transmisi']:<6} {jml}")
            
            print("-" * 60)
            print("Ketik nomor urut untuk DETAIL / EDIT / HAPUS.")
            print("Ketik '0' untuk KEMBALI.")
            
            pilihan = input("\nPilihan >> ")
            
            if pilihan == '0':
                break
            
            if pilihan.isdigit():
                idx = int(pilihan) - 1
                if 0 <= idx < len(self.history):
                    self.manage_history_item(idx)
                else:
                    print("Nomor tidak ditemukan!")
                    time.sleep(1)
            else:
                print("Input harus angka.")
                time.sleep(1)

    def manage_history_item(self, idx):
        while True:
            data = self.history[idx]
            self.print_report(data)
            
            print("\nOPSI MENU:")
            print("1. Edit Data (Nama/Merk)")
            print("2. Diagnosa Ulang (Update Kondisi)")
            print("3. Hapus Data Ini")
            print("4. Kembali")
            
            opsi = input("Pilih (1-4): ")
            
            if opsi == '1':
                print("\nBiarkan kosong jika tidak ingin mengubah.")
                new_name = input(f"Nama Baru [{data['nama']}]: ")
                new_merk = input(f"Merk Baru [{data['merk']}]: ")
                
                if new_name: self.history[idx]['nama'] = new_name
                if new_merk: self.history[idx]['merk'] = new_merk
                print("Data update!")
                time.sleep(1)
            
            elif opsi == '2':
                confirm = input("Diagnosa ulang akan menghapus hasil lama. Lanjut? (y/n): ")
                if confirm.lower() == 'y':
                    # Panggil fungsi diagnosa dengan data lama 
                    new_data = self.process_diagnosis(
                        existing_name=data['nama'], 
                        existing_brand=data['merk'] # Pass brand lama
                        # Transmisi sengaja tidak di-lock agar bisa diganti jika salah input awal
                    )
                    self.history[idx] = new_data
                    print("Diagnosa diperbarui!")
                    time.sleep(1)
            
            elif opsi == '3':
                if input("Hapus data? (y/n): ").lower() == 'y':
                    del self.history[idx]
                    return
            
            elif opsi == '4':
                break

    def main_menu(self):
        while True:
            self.clear_screen()
            print("=== sistem identifikasi kerusakan pada mobil ===")
            print("1. Diagnosa Baru")
            print("2. Lihat Riwayat")
            print("3. Keluar")
            
            pil = input("Pilih: ")
            if pil == '1': self.new_session()
            elif pil == '2': self.history_menu()
            elif pil == '3': break

if __name__ == "__main__":
    app = CarDiagnosticSystem()
    app.main_menu()