tr_karakter="şçğüöıİ"
parola=input("parola gir")
for i in parola:
    if i in tr_karakter:
        raise TypeError("parolada türkçe karakter olamaz")
    else:
        pass
print("parola kabul edildi")
