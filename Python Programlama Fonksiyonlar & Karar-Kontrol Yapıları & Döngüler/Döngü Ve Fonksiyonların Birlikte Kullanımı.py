#Döngü Ve Fonksiyonların Beraber Kullanımı

def kare_al(x):
    print(x**2)
    
kare_al(2)

maaslar = [1000,2000,3000,4000,5000]

for i in maaslar:
    print(i)
    
#maaslara yüzde 20 zam yapılacak kodları

maaslar[0]*20/100 + maaslar[0]
maaslar[1]*20/100 + maaslar[1]

#Döngü yazılcak.
#fonksiyon yazılcak.

def yeni_maas(x):
    print(x)
    
yeni_maas(4)

def yeni_maas(x):
    print(x*20/100 + x)
    

for i in maaslar:
    yeni_maas(i)