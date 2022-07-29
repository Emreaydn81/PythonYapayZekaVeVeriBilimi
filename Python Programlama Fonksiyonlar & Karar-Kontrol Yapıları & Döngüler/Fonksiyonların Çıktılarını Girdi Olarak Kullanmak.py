#Fonksiyonların Çıktılarını Girdi Olarak Kullanmak = return
#Eski
def direk_hesap(ısı, nem, sarj):
    print((ısı + nem)/sarj)
    
çıktı = direk_hesap(25, 30, 40)
çıktı
print(çıktı)

#Yeni
def direk_hesap(ısı, nem, sarj):
    return((ısı + nem)/sarj)

direk_hesap(25, 40, 70)*9
çıktı = direk_hesap(25,40,70)
print(çıktı)
