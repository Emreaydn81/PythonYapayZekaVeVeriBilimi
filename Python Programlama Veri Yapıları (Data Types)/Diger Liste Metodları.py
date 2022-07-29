#count

liste = ["ali","veli","emre","tuba"]

liste.count("ali")
liste.count("veli")
liste.count("isik")


#mevcut listeyi kopyalamak = copy()

liste_yedek = liste.copy()

#iki listeyi birleştirmek için kullanılır : extend()

liste.extend(["a","b",10])
liste

#elemanın oldugu yeri gösterir : index()

liste.index("ali")

#elemanları terse çevirme işleminde kullanılır:reverse()

liste.reverse()
liste

#sıralama yapmak için kullanılır : sort()
liste = [10,40,5,90]
liste.sort()

liste


#liste içini temizlemek için kullanılır : clear()

liste.clear()
liste
