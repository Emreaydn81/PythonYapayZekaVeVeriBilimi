# Uygulama

sınır = 50000

magaza_adı = input("Magaza Adı Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sınır:
    print("Tebrikler:" + "magaza_adı" + " Promosyon Kazandınız!")
elif gelir < sınır:
    print("Uyarı! Çok Düşük Gelir:" + str(gelir))
else:
    print("Takibe devam")