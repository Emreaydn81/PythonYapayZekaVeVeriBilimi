# Ön Tanımlı Argümanlar

?print

def carpma_yap(x, y):
    print(x*y)
    
carpma_yap(3)

#y sayı vererek işlem yaptırma

def carpma_yap(x, y = 1):
    print(x*y)
    
carpma_yap(3)

print("Merhaba")

#Argümanların Sıralaması

def carpma_yap(x, y = 1):
    print(x*y)
    
carpma_yap(y = 2,x = 3)

carpma_yap(2,3)
