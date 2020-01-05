ilk_sayi=input("birinci sayiyi gir :")
try:
    sayi1=int(ilk_sayi)
except ZeroDivisionError:
    print("1. sayıya 0 girdin!")
except ValueError:
    print("birinci sayıya harf girdin")


ikinci_sayi=input("ikinci sayiyi gir :")
try:
    sayi2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)

except (ValueError,ZeroDivisionError):
    print("ikinci sayıya harf ya da 0 girdin")

