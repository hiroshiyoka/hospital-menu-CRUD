import os
from dokter import Dokter

class MenuDokter:
    def __init__(self):
        self.menu_dokter = [
            '1. Print data dokter',
            '2. Tambah data dokter',
            '3. Cari data dokter',
            '4. Hapus data dokter',
            '5. Edit data dokter',
            '6. Keluar'
        ]
        
        self.menu_cari_dokter = [
            '1. Cari berdasarkan nama',
            '2. Cari berdasarkan spesialisasi',
            '3. Keluar'
        ]
        
        self.db_dokter = DbDokter()
        self.run_menu_dokter()
        
    def run_menu_dokter(self):
        while True:
            os.system('cls')
            print("Selamat datang di menu data dokter.")
            print("-----------------------------------")
            for menu in self.menu_dokter:
                print(menu)
                
            pilihan = input("Silakan pilih menu: ")
            if pilihan == '1':
                self.db_dokter.print_semua_dokter()
            elif pilihan == '2':
                nama = ''
                while self.db_dokter.dokter_ada(nama) or nama == '':
                    nama = input("Masukkan nama dokter : ")
                    if self.db_dokter.dokter_ada(nama):
                        print("Nama dokter sudah terdaftar.")
                        
                spesialisasi = input("Spesialisasi: ")
                self.db_dokter.tambah_data_dokter(nama=nama, spesialisasi=spesialisasi)
            elif pilihan == '3':
                self.run_menu_cari_dokter()
            elif pilihan == '4':
                self.db_dokter.print_semua_nama_dokter()
                nama = input("Silakan masukkan nama dokter yang akan dihapus datanya: ")
                self.db_dokter.hapus_data_dokter_by_nama(nama)
            elif pilihan == '5':
                nama = input("Silakan masukkan nama dokter yang akan diedit: ")
                self.db_dokter.edit_data_dokter_by_nama(nama)
            elif pilihan == '6':
                return
            else:
                print("Anda tidak memasukkan pilihan dengan benar")
            input("Tekan enter untuk melanjutkan")    
            
    def run_menu_cari_dokter(self):
        while True:
            os.system('cls')
            print("Selamat datang di menu cari data dokter")
            print("---------------------------------------")
            for menu_cari in self.menu_cari_dokter:
                print(menu_cari)
            pilih = input("Pilih menu cari data dokter yang anda inginkan: ")
            if pilih == '1':
                nama = input("Masukkan nama dokter yang ingin dicari: ")
                dokter = self.db_dokter.cari_data_dokter_by_nama(nama)
                if dokter is None:
                    print("Data dokter dengan nama", nama, "tidak ditemukan.")
                else:
                    dokter.print_data_dokter()
            elif pilih == '2':
                spesialisasi = input("Masukkan spesialisasi dokter yang ingin dicari: ")
                dokter_list = self.db_dokter.cari_data_dokter_by_spesialisasi(spesialisasi)
                if not dokter_list:
                    print("Data dokter dengan spesialisasi", spesialisasi, "tidak ditemukan.")
                else:
                    print("Dokter dengan spesialisasi", spesialisasi, ":")
                    for dokter in dokter_list:
                        dokter.print_data_dokter()
            elif pilih == '3':
                break
            else:
                print("Anda tidak memasukkan pilihan dengan benar")
            input("Tekan enter untuk melanjutkan")

class DbDokter:
    def __init__(self):
        self.db_dokter = []
        
    def print_semua_dokter(self):
        for dokter in self.db_dokter:
            dokter.print_data_dokter()
    
    def print_semua_nama_dokter(self):
        print("== Daftar nama dokter ==")
        for dokter in self.db_dokter:
            print(dokter.nama)
        print("")
        
    def cari_data_dokter_by_nama(self, nama: str):
        for dokter in self.db_dokter:
            if dokter.nama == nama:
                return dokter
        return None
            
    def cari_data_dokter_by_spesialisasi(self, spesialisasi: str):
        dokter_ditemukan = []
        for dokter in self.db_dokter:
            if dokter.spesialisasi == spesialisasi:
                dokter_ditemukan.append(dokter)
        return dokter_ditemukan
            
    def tambah_data_dokter(self, nama, spesialisasi):
        daftar_nama_dokter = [dokter.nama for dokter in self.db_dokter]
        if nama in daftar_nama_dokter:
            print("Data dokter sudah ada dalam database.")
        else:
            nomor = len(self.db_dokter) + 1
            dokter = Dokter(nomor, nama, spesialisasi)
            self.db_dokter.append(dokter)
            print("Dokter dengan nama", dokter.nama, "berhasil disimpan.")
            
    def dokter_ada(self, nama: str):
        daftar_nama_dokter = [dokter.nama for dokter in self.db_dokter]
        if nama in daftar_nama_dokter:
            return True
        return False
    
    def hapus_data_dokter_by_nama(self, nama: str):
        for dokter in self.db_dokter:
            if dokter.nama == nama:
                self.db_dokter.remove(dokter)
                print("Data dokter dengan nama", dokter.nama, "berhasil dihapus.")
                return
        print("Dokter dengan nama", nama, "tidak terdaftar dalam database.")
            
    def edit_data_dokter_by_nama(self, nama: str):
        for dokter in self.db_dokter:
            if dokter.nama == nama:
                print("Dokter dengan nama", nama, "ditemukan.")
                edit_dokter = True
                while edit_dokter:
                    print("Pilih data dokter yang akan diedit:")
                    print("1. Nama")
                    print("2. Spesialisasi")
                    pilih = input("Silakan pilih (1/2): ")
                    if pilih == '1':
                        nama_baru_dokter = input("Silakan masukan nama baru dokter: ")
                        dokter.nama = nama_baru_dokter
                    elif pilih == '2':
                        spesialisasi_baru_dokter = input("Silakan masukan spesialisasi baru dokter: ")
                        dokter.spesialisasi = spesialisasi_baru_dokter
                    else:
                        print("Anda tidak memasukkan pilihan yang benar.")
                        print("Data dokter tidak berubah.")
                        
                    still_edit = input("Apakah Anda masih ingin meng-edit data dokter? (Y/N): ")
                    if still_edit.lower() == 'n':
                        edit_dokter = False
                        print("Edit data dokter selesai.")
                        dokter.print_data_dokter()
                    elif still_edit.lower() == 'y':
                        continue
                    else:
                        edit_dokter = False
                        print("Anda tidak memasukkan pilihan yang benar.")
                        print("Edit selesai.")
