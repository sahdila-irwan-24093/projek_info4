class Hewan:
    def makan(self):
        print("Hewan makan ikan")

class Bangau(Hewan):
    def suara(self):
        print("Kruk-kruk")

k = Bangau()
k.makan()
k.suara()
print("="*25)
# ==================================
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Mobil(Kendaraan):
    def jalan(self):
        print("Mobil berjalan")

m = Mobil("Suzuki")
m.info()
m.jalan()

print("="*25)
# ==================================
class Hewan: 
    def suara(self):
        print("suara hewan")

class LumbaLumba(Hewan):
    def suara(self):
        print("wiiiuuu—wiiiuu—piiip—piiip")  

a = LumbaLumba()
a.suara()    

