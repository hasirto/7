while True:
    tr_karakter = ["ben","a","o","r"]
    parola = input("parolayı giriniz: ")

    for i in parola:
        if i in tr_karakter:
            print("parolada {} harfi olamaz".format(tr_karakter[0]))
        else:
            pass
    print("parola kabul edildi")
