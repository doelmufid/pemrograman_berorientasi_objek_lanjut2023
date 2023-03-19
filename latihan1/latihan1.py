#contoh 1
class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} berwarna {self.warna}")

mobilA = Mobil("Toyota", "Hitam")
mobilA.info() # Output: Mobil Toyota berwarna Hitam

#Contoh 2:
class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")

mahasiswaB = Mahasiswa("Ahmad", "123456789")
mahasiswaB.info()

#Contoh 3:
class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return 3.14 * (self.jari_jari ** 2)
    
lingkaranA = Lingkaran(7)
print(f"Luas lingkaran: {lingkaranA.luas()}")

#Contoh 4:
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def info(self):
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}")

bukuA = Buku("Harry Potter and the Philosopher's Stone", "J.K. Rowling")
bukuA.info()

#Contoh 5:
class PesawatTerbang:
    def __init__(self, maskapai, tujuan):
        self.maskapai = maskapai
        self.tujuan = tujuan

def info(self):
    print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")

pesawatA = PesawatTerbang("Garuda Indonesia", "Jakarta - Bali")
pesawatA.info()

#Contoh 6:
class Kalkulator:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def subtract(x, y):
        return x - y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    @staticmethod
    def divide(x, y):
        if y == 0:
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y
    
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(3, 5)) # Output: 8
print(Kalkulator.subtract(10, 7)) # Output: 3
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4, 6)) # Output: 24
print(Kalkulator.divide(12, 4)) # Output: 3.0

#Contoh 7:
class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5
    
mycelcius = 80
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit)

class Celcius:
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5

C = 75
F = Celcius.to_fahrenheit(C)
print("konversi",C,"derajat celcius adalah",F,"derajat fahrenheit")

C = 60
R = Celcius.to_reamur(C)
print("konversi",C,"derajat celcius adalah",R,"derajat reamur")

C = 90
K = Celcius.to_kelvin(C)
print("konversi",C,"derajat celcius adalah",K,"derajat kelvin")