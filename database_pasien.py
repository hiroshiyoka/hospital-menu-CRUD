import os
from pasien import Pasien

class MenuPasien:
    def __init__ (self):
        self.menu_pasien = ['1. Print data pasien', 
                '2. Tambah data pasien', 
                '3. Cari data pasien', 
                '4. Hapus data pasien', 
                '5. Edit data pasien', 
                '6. Keluar']
        
        self.menu_cari_pasien = [
            '1. Cari berdasarkan nama',
            '2. Cari berdasarkan alamat',
            '3. Cari berdasarkan umur',
            '4. Cari berdasarkan gender',
            '5. Cari berdasarkan penyakit',
            '6. Keluar'
        ]

        self.db_pasien = DbPasien()
        self.run_menu_pasien()

    def run_menu_pasien (self):
        while True:
            os.system ('cls')
            print ("Selamat datang di menu data pasien.")
            print ("-----------------------------------")
            for menu in self.menu_pasien:
                print (menu)

            pilihan = input ("Silakan pilih menu: ")
            if pilihan == '1':
                self.db_pasien.print_semua_pasien ()
            elif pilihan == '2':
                nama = ''
                while self.db_pasien.pasien_ada (nama) or nama == '':
                    nama = input ("Nama pasien: ")
                    if self.db_pasien.pasien_ada (nama):
                        print ("Nama sudah terdaftar")

                alamat = input ("Alamat: ")
                umur = int (input ("Umur: "))
                gender = input ("Jenis kelamin (L/P): ")
                if gender == 'L' or 'l': gender = 1
                elif gender == 'P' or 'p': gender = 0
                penyakit = input("Penyakit pasien: ")
                self.db_pasien.tambah_data_pasien (nama = nama, alamat = alamat, umur = umur, gender = gender, penyakit = penyakit)
            elif pilihan == '3':
                self.run_menu_cari_pasien()
            elif pilihan == '4':
                self.db_pasien.print_semua_nama_pasien()
                nama = input ("Silakan masukkan nama pasien yang akan dihapus datanya: ")
                self.db_pasien.hapus_data_pasien_by_nama (nama)
            elif pilihan == '5':
                nama = input ("Silakan masukkan nama pasien yang akan diedit: ")
                self.db_pasien.edit_data_pasien_by_nama (nama)
            elif pilihan == '6':
                return
            else:
                print ("Anda tidak memasukkan pilihan dengan benar")

            input ("Tekan enter untuk melanjutkan")
            
    def run_menu_cari_pasien(self):
        while True:
            os.system('cls')
            print("Selamat datang di menu cari pasien")
            print("----------------------------------")
            for menu_cari in self.menu_cari_pasien:
                print(menu_cari)
            pilih = input("Pilih menu cari pasien yang anda inginkan: ")
            if pilih == '1':
                nama = input("Masukkan nama pasien yang ingin dicari: ")
                pasien = self.db_pasien.cari_data_pasien_by_nama(nama)
                if pasien is None:
                    print("Pasien dengan nama", nama, "tidak ditemukan.")
                else:
                    pasien.print_data()
            elif pilih == '2':
                alamat = input("Silakan masukkan alamat pasien yang ingin dicari: ")
                pasien = self.db_pasien.cari_data_pasien_by_alamat(alamat)
                if not pasien:
                    print("Pasien dengan nama", nama, "tidak ditemukan.")
                else:
                    for data_pasien in pasien:
                        data_pasien.print_data()
            elif pilih == '3':
                umur = int(input("Masukkan umur pasien yang ingin dicari: "))
                pasien = self.db_pasien.cari_data_pasien_by_umur(umur)
                if not pasien:
                    print("Pasien dengan umur", umur, "tidak ditemukan.")
                else:
                    for data_pasien in pasien:
                        data_pasien.print_data()
            elif pilih == '4':
                gender = input("Masukkan gender pasien yang ingin dicari: ")
                if gender.lower() == 'l':
                    gender = 1
                elif gender.lower() == 'p':
                    gender = 0
                else:
                    print("Anda tidak memasukkan data dengan benar.")
                    continue
                pasien = self.db_pasien.cari_data_pasien_by_gender(gender)
                if not pasien:
                    print("Pasien dengan jenis kelamin", gender, "tidak ditemukan.")
                else:
                    for data_pasien in pasien:
                        data_pasien.print_data()
            elif pilih == '5':
                penyakit = input("Masukkan penyakit pasien yang ingin dicari: ")
                pasien = self.db_pasien.cari_data_pasien_by_penyakit(penyakit)
                if not pasien:
                    print("Pasien dengan penyakit", penyakit, "tidak ditemukan.")
                else:
                    for data_pasien in pasien:
                        data_pasien.print_data()
            elif pilih == '6':
                break
            else:
                print("Anda tidak memasukkan pilihan dengan benar")
            input("Tekan enter untuk melanjutkan")
                

class DbPasien:
    def __init__ (self):
        self.db_pasien = []
        
    def print_semua_pasien (self):
        for pasien in self.db_pasien:
            pasien.print_data()

    def print_semua_nama_pasien (self):
        print ("== Daftar nama pasien ==")
        for pasien in self.db_pasien:
            print (pasien.nama)

        print ("")


    def cari_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.nama == nama:
                return pasien

    def cari_data_pasien_by_alamat(self, alamat: str):
        hasil_pencarian = []
        for pasien in self.db_pasien:
            if pasien.alamat.lower() == alamat.lower():
                hasil_pencarian.append(pasien)
        return hasil_pencarian
    
    def cari_data_pasien_by_umur(self, umur: str):
        hasil_pencarian = []
        for pasien in self.db_pasien:
            if pasien.umur == umur:
                hasil_pencarian.append(pasien)
        return hasil_pencarian
    
    def cari_data_pasien_by_gender(self, gender: str):
        hasil_pencarian = []
        for pasien in self.db_pasien:
            if pasien.gender == gender:
                hasil_pencarian.append(pasien)
        return hasil_pencarian
    
    def cari_data_pasien_by_penyakit(self, penyakit: str):
        hasil_pencarian = []
        for pasien in self.db_pasien:
            if pasien.penyakit.lower() == penyakit.lower():
                hasil_pencarian.append(pasien)
        return hasil_pencarian
    
    def tambah_data_pasien (self, nama, alamat, umur, gender, penyakit):
        daftar_nama = [pasien.nama for pasien in self.db_pasien]
        if nama in daftar_nama:
            print ("Pasien sudah ada dalam database.")
        else:
            nomor = len(self.db_pasien) + 1
            pasien = Pasien (nomor, nama, alamat, umur, gender, penyakit)
            self.db_pasien.append (pasien)
            print ("Pasien dengan nama", pasien.nama, "berhasil disimpan.")

    def pasien_ada (self, nama: str):
        daftar_nama = [pasien.nama for pasien in self.db_pasien]
        if nama in daftar_nama:
            return True

        return False

    def hapus_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.nama == nama:
                self.db_pasien.remove (pasien)
                print("Data pasien dengan nama", pasien.nama, "telah dihapus.")
                return

        print ("Pasien dengan nama", nama, "tidak terdaftar dalam database.")

    def edit_data_pasien_by_nama (self, nama: str):
        for pasien in self.db_pasien:
            if pasien.nama == nama:
                print ("Pasien dengan nama", nama, "ditemukan.")
                edit = True
                while (edit):
                    print ("Pilih data yang akan diedit:")
                    print ("1. Nama")
                    print ("2. Alamat")
                    print ("3. Umur")
                    print ("4. Gender")
                    print ("5. Penyakit")
                    pilih = input ("Silakan pilih (1/2/3/4/5): ")
                    if pilih == '1':
                        nama_baru = input ("Silakan masukan nama baru pasien: ")
                        pasien.nama = nama_baru
                    elif pilih == '2':
                        alamat_baru = input ("Silakan masukan alamat baru pasien: ")
                        pasien.alamat = alamat_baru
                    elif pilih == '3':
                        umur_baru = input ("Silakan masukan umur baru pasien: ")
                        pasien.umur = umur_baru
                    elif pilih == '4':
                        gender = input ("Gender pasien (L/P): ")
                        if gender == 'L' or gender == 'l':
                            pasien.gender = 1
                        elif gender == 'P' or gender == 'p':
                            pasien.gender = 0
                        else:
                            print ("Anda tidak memasukkan data dengan benar.")
                            print ("Gender pasien tidak berubah.")
                    elif pilih == '5':
                        penyakit_baru = input("Silakan masukan penyakit baru pasien: ")
                        pasien.penyakit = penyakit_baru
                    else:
                        print ("Anda tidak memasukkan pilihan dengan benar.")
                        print ("Data pasien tidak berubah.")

                    masih_edit = input ("Apakah Anda masih ingin meng-edit data pasien? (Y/T): ")
                    if masih_edit == 'T' or masih_edit == 't':
                        edit = False
                        print ("Edit data pasien selesai.")
                        pasien.print_data()
                    elif masih_edit == 'Y' or masih_edit == 'y':
                        continue
                    else:
                        edit = False
                        print ("Anda tidak memasukkan pilihan dengan benar.")
                        print ("Edit selesai")
