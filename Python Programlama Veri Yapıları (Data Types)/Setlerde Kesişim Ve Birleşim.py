#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

#intersection = kesişim
set1.intersection(set2)
set2.intersection(set1)

kesişim = set1 & set2
kesişim

#union = Birleştirme
set1.union(set2)
birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1
