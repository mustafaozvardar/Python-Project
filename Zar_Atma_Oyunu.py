import random
hak=3
print("***Zar Atma Uygulamasına Hoşgeldiniz***")
print("--> 1 ile 6 arasında bir sayı tahmin edin..")
while True:
    gelen_sayi=int(input("Tahmin giriniz: "))
    rastgele_sayi=random.randint(1,6)
    if (gelen_sayi==rastgele_sayi):
        print("-->**TEBRİKLER..! DOĞRU TAHMİN..")
        break
    elif (gelen_sayi!=rastgele_sayi):
        print("Yanlış tahmin..")
        hak-=1
        print("Kalan tahmin hakkı: ",hak)
    else:
        print("Zarda böyle bir sayı yok..!")
        print("Rastgele sayımız: ",rastgele_sayi)
        break
    if hak==0:
        print("Hakkınız Kalmadı..")
        print("Rastgele sayımız: ",rastgele_sayi)
        break


