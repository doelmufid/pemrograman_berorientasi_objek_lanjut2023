class Fahrenheit:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def to_celsius(self):
        return (self.temperature - 32) * 5/9
    
    def to_reamur(self):
        return (self.temperature - 32) * 4/9
    
    def to_kelvin(self):
        return (self.temperature + 459.67) * 5/9

suhu = float(input("Masukan Nilai Suhu Fahrenheit:"))
f = Fahrenheit(suhu)

c = f.to_celsius()
print(suhu,"derajat Fahrenheit", round(c, 2),"derajat Celsius".format(c))

r = f.to_reamur()
print(suhu,"derajat Fahrenheit", round(r, 2),"derajat Reamur".format(r))

k = f.to_kelvin()
print(suhu,"derajat Fahrenheit", round(k, 2),"derajat Kelvin".format(k))