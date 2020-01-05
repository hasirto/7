while True:
    x = input("Bir sayı girin: ")
    if not x:
        break
    try:
        y = float(x)
    except ValueError:
        print("Geçersiz sayı")
        continue
    print(y**2)