class Reamur:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def to_celsius(self):
        return self.temperature * 5/4
    
    def to_fahrenheit(self):
        return self.temperature * 9/4 + 32
    
    def to_kelvin(self):
        return self.temperature * 5/4 + 273.15

suhu = float(input("Masukan Nilai Suhu Reamur:"))
r = Reamur(suhu)

c = r.to_celsius()
print(suhu,"derajat Reamur", round(c, 2),"derajat Celsius".format(c))

f = r.to_fahrenheit()
print(suhu,"derajat Reamur", round(f, 2),"derajat Fahrenheit".format(r))

k = r.to_kelvin()
print(suhu,"derajat Reamur", round(k, 2),"derajat Kelvin".format(k))