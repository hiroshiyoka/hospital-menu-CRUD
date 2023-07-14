import os
import random
from database_pasien import MenuPasien
from database_dokter import MenuDokter
from database_fasilitas import MenuFasilitas

pesan_random = [
    "Selamat datang di Aplikasi Rumah Sakit Raka.",
    "Selamat datang di Rumah Sakit Raka, Selamat berkunjung.",
    "Selamat datang! Aplikasi Rumah Sakit siap digunakan."
]

while True:
    os.system ('cls')
    print(random.choice(pesan_random))
    print ("----------------------------------------------")
    print ("Silakan pilih menu berikut.")
    print ("1. Kelola data pasien")
    print ("2. Kelola data dokter")
    print ("3. Kelola fasilitas ")
    print ("4. Keluar")
    pilihan = input ("Silakan masukkan pilihan Anda (1/2/3/4): ")
    print ("")
    if pilihan == '1':
        menu_pasien = MenuPasien()
        continue
    elif pilihan == '2':
        menu_dokter = MenuDokter()
        continue
    elif pilihan == '3':
        menu_fasilitas = MenuFasilitas()
    elif pilihan == '4':
        print ("Terima kasih")
        break
    else:
        print ("Anda tidak memasukkan pilihan dengan benar.")

    input ("Tekan enter untuk melanjutkan")