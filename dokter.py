class Dokter:
    def __init__ (self, nomor: int, nama: str, spesialisasi: str):
        self.nomor = nomor
        self.nama = nama
        self.spesialisasi = spesialisasi
        
    def print_data_dokter(self):
        print("===== No. Dokter:", self.nomor, " =====")
        print("Nama Dokter\t:", self.nama)
        print("Spesialisasi\t:", self.spesialisasi)
