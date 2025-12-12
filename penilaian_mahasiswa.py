## SISTEM IDENTIFIKASI KELULUSAN MAHASISWA (CRUD, BASIS PENGETAHUAN, PYTHON)

# import library
from tabulate import tabulate



## Basis Pengetahuan (Kelulusan Mahasiswa)
def status_lulus(uts, uas, tugas, kehadiran):
    # hitung nilai akhir
    nilai_akhir = 0.4*uts + 0.45*uas +0.15*tugas
    #RULE KELULUSAN (Lulus, Lulus Bersyarat, Tidak Lulus)
    if (nilai_akhir >= 70) & (kehadiran >= 75):
        return "Lulus" # Kondisi 1
    elif (nilai_akhir >= 70) & (kehadiran < 75):
        return "Lulus Bersyarat" ## Kondisi 2
    elif (60 <= nilai_akhir <= 70) & (kehadiran >= 75):
        return "Lulus Bersyarat" ## Kondisi 3
    else:
        return "Tidak Lulus" ## Kondisi 4

## Database
data_mahasiswa=[
    ["Adi",80,85,90,90,status_lulus(80,85,90,90)],
    ["Bayu",60,67,65,85,status_lulus(60,67,65,85)],
    ["Charlie",50,57,65,55,status_lulus(50,57,65,55)]
    ]

## Menu Tampilkan Data (READ)
def tampilkan_data():
    headers=["No.","Nama","UTS","UAS","Tugas","Kehadiran","Status"] #header tabel
    tabel=[] #inital data(list kosong)
    for i, mhs in enumerate(data_mahasiswa):
        tabel.append([i+1]+mhs) #proses menambahkan data
    print(tabulate(tabel, headers=headers,tablefmt='heavy_outline'))

## Menu Tambah Data (CREATE)
def tambah_data():
    nama=input("Masukkan nama mahasiswa :")
    uts=int(input("Masukkan nilai uts :"))
    uas=int(input("Masukkan nilai uas :"))
    tugas=int(input("Masukkan nilai tugas :"))
    kehadiran=int(input("Masukkan persentase kehadiran :"))
    status=status_lulus(uts,uas,tugas,kehadiran)
    data_mahasiswa.append([nama, uts,uas, tugas, kehadiran, status])
    print(f"Data {nama} telah ditambahkan !\n")
    tampilkan_data()

## Menu Ubah Data (UPDATE)
def ubah_data():
    tampilkan_data()
    index_mahasiswa=int(input("Masukkan nomor mahasiswa yang ingin diubah :"))-1
    indeks_kolom=int(input("""
                Kolom yang bisa diubah:
                1. Nama
                2. UTS
                3. UAS
                4. Tugas
                5. Kehadiran
                """))-1
    if indeks_kolom==0:
        nama_mahasiswa=input("Masukkan nama mahasiswa yang baru :")
        print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil diubah.\n")
        data_mahasiswa[index_mahasiswa][0]=nama_mahasiswa
    elif indeks_kolom==1:
        nilai_uts=int(input("Masukkan nilai uts yang baru :"))
        print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil diubah.\n")
        data_mahasiswa[index_mahasiswa][1]=nilai_uts
    elif indeks_kolom==2:
        nilai_uas=int(input("Masukkan nilai uas yang baru :"))
        print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil diubah.\n")
        data_mahasiswa[index_mahasiswa][2]=nilai_uas
    elif indeks_kolom==3:
        nilai_tugas=int(input("Masukkan nilai tugas yang baru :"))
        print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil diubah.\n")
        data_mahasiswa[index_mahasiswa][3]=nilai_tugas
    elif indeks_kolom==4:
        kehadiran=int(input("Masukkan persentase kehadiran yang baru :"))
        print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil diubah.\n")
        data_mahasiswa[index_mahasiswa][4]=kehadiran
    else:
        print("Pilihan tidak valid")
    tampilkan_data()

## Menu Ubah Data (UPDATE)
def hapus_data():
    tampilkan_data()
    index_mahasiswa=int(input("Masukkan nomor mahasiswa yang ingin dihapus :"))-1
    print(f"Data {data_mahasiswa[index_mahasiswa][0]} sudah berhasil dihapus.\n")
    del data_mahasiswa[index_mahasiswa]
    tampilkan_data()
    


## Main Menu
def main():
    while True:
        print("""
        ====== SISTEM KELULUSAN MAHASISWA ======
        1. Tampilkan Data
        2. Tambah Data
        3. Ubah Data
        4. Hapus Data
        5. Exit        
        """) #Homepage

        pilihan = input("Pilih menu :")

        if pilihan == '1':
            tampilkan_data()
        elif pilihan == '2':
            tambah_data()
        elif pilihan == '3':
            ubah_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            print("Program selesai. \nTerima Kasih !")
            break
        else:
            print("Pilihan tidak valid !")

main()
