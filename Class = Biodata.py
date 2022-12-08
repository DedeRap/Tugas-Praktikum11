print("===== Class : Biodata =====")

class mahasiswa :
    Total = 0
    def __init__(self, nama, NIM, angkatan):
        self.nama = nama
        self.NIM = NIM
        self.angkatan = angkatan
        mahasiswa.Total += 1
        
    def tampilin(self):
        print("Total mahasiswa : %d" % mahasiswa.Total)
    
    def biodata(self):
       print("\nNama     : ", self.nama)
       print("NIM      : ", self.NIM)
       print("Angkatan : ", self.angkatan)
       

nama     = input("Masukkan nama anda : ")
NIM      = input("Masukkan NIM anda  : ")
angkatan = input("Masukkan tahun anggkatan anda : ")

data = mahasiswa(nama, NIM, angkatan)
data.biodata()
print()
data.tampilin()