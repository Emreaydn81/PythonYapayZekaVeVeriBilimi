#Fonksıyonlara Gırıs ve Fonksiyon Okur Yazarlığı

print("a","b",sep = "_")

#Fonksiyon Dokümasyontonları
?print

len("a")

#Fonksiyon Nasıl Yazılır
#Ekrana Yazdırma
def kare_al(x):
    print(x**2)
    
kare_al(3)

#Hesaplar Ama Ekrana Yazdırmaz
    def kare_al(x):
        x**2
        
    kare_al(5)
