print("===== Program OOP Getter dan Setter =====")

class Data:
    
    def __init__(self, nama, nilai):
        self.nama  = nama
        self.__nilai = nilai
    
    @property
    def Tampilkan(self):
        return "\nNama  : {} \nNilai : {}".format(self.nama, self.__nilai)
    
    @property 
    def nilai(self):
        pass
    
    @nilai.getter
    def nilai(self):
        return self.__nilai
    
    @nilai.setter
    def nilai(self, input):
        self.__nilai = input
    
    @nilai.deleter
    def nilai(self):
        self.__nilai = None
    
data = Data(None, None) 
u = True
while (u != False):
    print("\n1. Mendeklarasikan Objek")
    print("2. Menampilkan Objek")
    print("3. Merubah Objek")
    print("4. Menghapus Nilai Objek")
    print("5. Keluar dari Program")
    Pilihan = int(input("Masukkan Pilihan Berupa Angka (1/2/3/4/5): "))
    
    if (Pilihan == 1):
        nama  = input("Masukkan Nama Anda  = ")
        nilai = input("Masukkan Nilai Anda = ")
        
        data = Data(nama, nilai)
        print("Data Berhasil Dibuat")
    
    elif (Pilihan == 2):
        print(data.Tampilkan)
        
    elif (Pilihan == 3):
        Ganti = input("Apa yang Ingin Diubah (Nama/Nilai): ")
        if (Ganti == 'Nama' or Ganti == 'nama'):
            nama = input("Masukkan Nama Anda = ")
            data.nama = nama
            print("Data nama berhasil diubah.")
            
        elif (Ganti == 'Nilai' or Ganti == 'nilai'):
            nilai = input("Masukkan Nilai Anda = ")
            data.nilai = nilai
            print("Data nilai berhasil diubah.")
            
        else :
            print("Maaf, pilihan tidak tersedia.")
            
    elif (Pilihan == 4):
        del data.nilai
        print("Nilai Telah Dihapus.")
            
    elif (Pilihan == 5):
        u = False

print("\nTerima kasih, telah menggunakan program ini.")