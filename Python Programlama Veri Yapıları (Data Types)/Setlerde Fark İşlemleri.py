#Setler - Klasik Kume İşlemleri

#difference() = ile iki kumenin farkini ya da "_" ifadesi
#intersection() = iki kume kesisimi ya da "&" ifadesi
#union() = iki kumenin birleşimi
#symmetric_difference() ikisinde de olmayanlar

#difference
set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

#ikisinde olmayanlar
set1.symmetric_difference(set2)

set1-set2
set2-set1
