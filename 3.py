ilk_sayi=input("birinci sayiyi gir :")
ikinci_sayi=input("ikinci sayiyi gir :")
try:
    sayi1=int(ilk_sayi)
    sayi2=int(ikinci_sayi)
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)

except ValueError as aciklama :#value error hatasını aciklama değişkenine atama
    print(aciklama)#hatanın gerçek açıklamasını yazdır
    print("sayı dışında bişi girdin")
