#Hatalar / istisnalar (exceptions)

a = 10

b = 0

a/b


try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sıfır olmaz")


#Tip Hatası

a = 10
b  = "2"

a / b

try:
    print(a/b)
except TypeError:
    print("Sayı Ve String Problemi")

#
a = 10
b  = 2

a / b

try:
    print(a/b)
except TypeError:
    print("Sayı Ve String Problemi")
