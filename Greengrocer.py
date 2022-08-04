print("Lütfen büyük harf ile başlayınız....")
soru = input("Hangi meyveyi alırsınız?: ")

if soru == "Muz":
    kilo= int(input("Kaç kilo?: "))
    print((kilo*5),"TL ücretiniz.")

elif soru == "Elma":
    renk = input("Hangi renk elma olsun?: ")

    if renk == "Kırmızı":
        kilo = int(input("Kaç kilo kırmızı elma olsun?: "))

    elif renk == "Sarı":
        kilo = int(input("Kaç kilo sarı elma olsun?: "))

    elif renk == "Yeşil":
        kilo = int(input("Kaç kilo yeşil elma olsun?: "))
    else:
        kilo = int(input("Lütfen geçerli bir renk giriniz...."))
    print((kilo*2),"Tl ücretiniz.")

elif soru == "Üzüm":
    renk = input("Hangi renk üzüm olsun?: ")

    if renk == "Mor":
        kilo = int(input("Kaç kilo mor üzüm olsun?: "))
        print((kilo*3),"Tl ücretiniz")

    elif renk == "Yeşil":
        kilo = int(input("Kaç kilo yeşil üzüm olsun?: "))
        print((kilo*3,5),"Tl ücretiniz.")
    else:
        print("Lütfen geçerli bir renk giriniz....")
else:
    print("Lütfen geçerli bir meyve giriniz....")
