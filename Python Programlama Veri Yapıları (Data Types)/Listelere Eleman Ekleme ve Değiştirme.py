#Listeler - Eleman Degiştirme

liste = ["ali", "veli","berkcan","ayse"]

#listede 1 numaralı kişiinin ismini değiştirme
liste[1] = "velinin_babası"


liste

liste[1] = "veli"

#listede 0 dan 3 çe kadar kişilerin isimleri değiştirme
liste[0:3] = "alinin_babası","velinin_babası","berkcanın_babası"

liste

#listeye ekleme

liste = liste + ["kemal"]

liste


del liste[2]
liste


