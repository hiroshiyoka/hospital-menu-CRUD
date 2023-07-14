class Pasien:
    def __init__ (self, nomor: int, nama: str, alamat: str, umur: int, gender: bool, penyakit: str):
        self.nomor = nomor
        self.nama = nama
        self.alamat = alamat
        self.umur = umur
        self.gender = gender
        self.penyakit = penyakit

    def print_data (self):
        print ("===== No. Pasien:", self.nomor, " =====")
        print ("Nama\t:", self.nama)
        print ("Alamat\t:", self.alamat)
        print ("Umur\t:", self.umur)
        if self.gender == 1:
            print ("Gender\t: Laki-laki")
        elif self.gender == 0:
            print ("Gender\t: Perempuan")
        else:
            print ("Gender\t: tidak tersedia")
        print("Penyakit\t:", self.penyakit)
