print("***Giris Uygulaması***")
print("1-Giriş Yap\t2-Çıkış Yap")
#Kullanici ve Sifre değişkenlere verilerimizi atadık.
kullanici="random"
sifre="1234"
hak=3
sec=int(input("Secim: "))
while True:
    
    if sec==1:
        #Kullanıcıdan Sifre ve Kullanıcı Adı girmesini istedik.
        userkullanici=input("Kullanıcı adı giriniz: ")
        usersifre=input("Sifre giriniz: ")
        if userkullanici==kullanici and usersifre!=sifre:
            #Eğer şifre hatalı ise hakkını 1 azalttık.
            print("Sifre hatali..")
            hak-=1
            print("Kalan Hak: ",hak)
        elif userkullanici!=kullanici and usersifre==sifre:
            #Eğer Kullanıcı Adı hatalı ise hakkını 1 azalttık.
            print("Kullanıcı adı hatalı..")
            hak-=1
            print("Kalan Hak: ",hak)
        elif userkullanici!=kullanici and usersifre!=sifre:
            #Eğer Kullanıcı Adı ve Sifre hatalı ise hakkını 1 azalttık.
            print("Kullanıcı adı ve Sifre hatali..")
            hak-=1
            print("Kalan Hak: ",hak)
        else:
            #Başta atamış olduğumuz değerle ile kullanıcan almış olduğumuz eşleştirildiğinde sisteme giriş yapıldı.
            print("-->Sisteme HOŞGELDİNİZ..")
            break
        if hak==0:
            #Hakkı bittiğinde sisteme girmesini break(dur) komutu ile engelledik.
            print("Hakkınız Kalmadı..! Girişiniz Engellendi.")
            break
    elif sec==2:
        print("Çıkıs yapıldı...")
        break
    else:
        print("Hatali secim..!")
