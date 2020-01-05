while True:
    try:
        bölünen=int(input("bölünecek sayiyi giriniz :"))
        bölen=int(input("bölen sayiyi giriniz :"))
    except ValueError:#int yerine harf girilirse
        print("bir sayi giriniz :")
    else:
        try:
            print(bölünen/bölen)
        except ZeroDivisionError:
            print("girilen sayı 0 a bölünemüyor")