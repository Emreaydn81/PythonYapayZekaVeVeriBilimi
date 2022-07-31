#Pythonda Fonksiyonel Prıgramlama
#Fonksiyonlar dilin bastacidir.
#(Birinci Sınıf Nesnelerdir.)
#Yan Etkisiz Fonksiyonlar. (stateless, girdi-çıktı)
#Yuksek Seviye Fonksiyonlar
#Vektorel Operasyonlar


#Yan Etkisiz Fonksiyonlar Örnek1

#Ornek1: Yan Etki

A = 9

def impure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3,4)
