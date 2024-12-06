class Gempa:
    # konstruktor insisialisasi atribut lokasi dan skala
    def __init__(self, lokasi, skala):
        
        # atribut
        self.lokasi = lokasi
        self.skala = skala

    # method menentukan dampak skala gempa
    def dampak(self):

        # statement/logika
        if self.skala < 2:
            print('dampak gempa tidak berasa')
            print()
        elif self.skala >=2 and self.skala <= 4:
            print('dampak gempa bangunan retak-retak')
            print()
        elif self.skala > 4 and self.skala <= 6:
            print('dampak gempa berpotensi tsunami')
            print()

        #menampilkan lokasi dan skala
        print (f'lokasi gempa: {self.lokasi}')
        print(f'skala gempa: {self.skala}')