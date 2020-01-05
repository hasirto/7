birinci_sayi=input("1.sayıyı gir: ")
ikinci_sayi=input("2.sayıyı gir:  ")

try:
    say1=int(birinci_sayi)
    say2=int(ikinci_sayi)
    print(say1/say2)
except ValueError:
    print("lüften onluk tabanlı bir sayı giriniz")
except ZeroDivisionError:
    print("0 a bölünemez")
