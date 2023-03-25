class Kelvin:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def to_celsius(self):
        return self.temperature - 273.15
    
    def to_fahrenheit(self):
        return self.temperature * 9/5 - 459.67
    
    def to_reamur(self):
        return (self.temperature - 273.15) * 4/5

suhu = float(input("Masukan Nilai Suhu Kelvin:"))
k = Kelvin(suhu)

c = k.to_celsius()
print(suhu,"derajat Kelvin", round(c, 2),"derajat Celsius".format(c))

f = k.to_fahrenheit()
print(suhu,"derajat Kelvin", round(f, 2),"derajat Fahrenheit".format(f))

r = k.to_reamur()
print(suhu,"derajat Kelvin", round(r, 2),"derajat Reamur".format(k))