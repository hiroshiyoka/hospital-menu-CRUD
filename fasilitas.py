class Fasilitas:
    def __init__ (self, barang: str, jenis: str):
        self.barang = barang
        self.jenis = jenis
        
    def print_data_fasilitas(self):
        print("===== Barang =====")
        print("Nama Barang\t:", self.barang)
        print("Jenis Barang\t:", self.jenis)
