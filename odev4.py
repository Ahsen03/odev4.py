# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

def kelime_goster(kelime, tekrar):
    for _ in range(tekrar):
        print(kelime)



# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def dikdortgen_hesapla(uzun_kenar, kisa_kenar):
    alan = uzun_kenar * kisa_kenar
    cevre = 2 * (uzun_kenar + kisa_kenar)
    return alan, cevre





# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)

import random

def yazi_tura():
    sonuc = random.choice(["Yazı", "Tura"])
    return sonuc




# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asal_sayilar(baslangic, bitis):
    def asal_mi(sayi):
        if sayi < 2:
            return False
        for i in range(2, int(sayi**0.5) + 1):
            if sayi % i == 0:
                return False
        return True

    return [sayi for sayi in range(baslangic, bitis + 1) if asal_mi(sayi)]




# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tam_bolenler(sayi):
    return [i for i in range(1, sayi + 1) if sayi % i == 0]


