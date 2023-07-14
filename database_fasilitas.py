import os
from fasilitas import Fasilitas

class MenuFasilitas:
    def __init__(self):
        self.menu_fasilitas = [
            '1. Lihat fasilitas',
            '2. Tambah fasilitas',
            '3. Keluar'
        ]
        
        self.run_menu_fasilitas()
        
    def run_menu_fasilitas(self):
        self.db_fasilitas = DbFasilitas()
        while True:
            os.system('cls')
            print("Selamat datang di menu fasilitas.")
            print("---------------------------------")
            for menu in self.menu_fasilitas:
                print(menu)
            pilihan = input("Silakan pilih menu: ")
            if pilihan == '1':
                self.db_fasilitas.print_semua_fasilitas()
            elif pilihan == '2':
                barang = ''
                while self.db_fasilitas.barang_ada(barang) or barang == '':
                    barang = input("Masukkan nama barang: ")
                    if self.db_fasilitas.barang_ada(barang):
                        print("Nama barang sudah terdaftar.")
                        
                jenis = input("Jenis barang: ")
                self.db_fasilitas.tambah_fasilitas(barang=barang, jenis=jenis)
            elif pilihan == '3':
                return
            else:
                print("Anda tidak memasukkan pilihan dengan benar")
            input("Tekan enter untuk melanjutkan")

class DbFasilitas:
    def __init__(self):
        self.db_fasilitas = []
        
    def print_semua_fasilitas(self):
        for fasilitas in self.db_fasilitas:
            fasilitas.print_data_fasilitas()
            
    def print_semua_nama_barang(self):
        print("== Daftar nama barang ==")
        for fasilitas in self.db_fasilitas:
            print(fasilitas.barang)
        print("")
                
    def tambah_fasilitas(self, barang, jenis):
        daftar_barang_fasilitas = [fasilitas.barang for fasilitas in self.db_fasilitas]
        if barang in daftar_barang_fasilitas:
            print("Data barang sudah ada dalam database.")
        else:
            fasilitas = Fasilitas(barang, jenis)
            self.db_fasilitas.append(fasilitas)
            print("Fasilitas dengan nama barang", fasilitas.barang, "berhasil disimpan.")
        
    def barang_ada(self, barang: str):
        daftar_fasilitas = [fasilitas.barang for fasilitas in self.db_fasilitas]
        if barang in daftar_fasilitas:
            return True
        return False
            