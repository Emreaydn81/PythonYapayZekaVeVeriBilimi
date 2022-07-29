#set sorgu işlemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

#İki kumenin kesisimini boş olup olmadıgını sorgulama

set1.isdisjoint(set2)


#bir kümenin butun elemanlarının baska bir kume 
#içerisinde yer alıp almadıgı

set1.issubset(set2)

#Bir kumenin bir diger kumeyi kapsayıp kapsamadıgı

set2.issuperset(set1)
