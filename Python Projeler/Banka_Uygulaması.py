print("*** Banka Uygulamasına Hoşgeldiniz ***")
print("Aşağıdaki işlemlerden birini seçiniz")
print("1-Para Yatır\t2-Para Çek\t3-Bakiye Bilgisi Göster\t4-Çıkış Yap")
bakiye = 0
while True:
    sec=int(input("Secim: "))
    if sec==1:
        #Kullanıcıdan yatırmak istediği miktarı alıyoruz.
        miktar=int(input("Yatırılacak miktarı giriniz: "))
        bakiye += miktar
        print("Para başarıyla yatırıldı..")
    elif sec==2:
        #Kullanıcıdan çekmek istediği miktarı alıyoruz.
        miktar=(int(input("Çekilecek miktar giriniz: ")))
        if (bakiye-miktar<0):
            print("Bakiyenizde bu kadar miktar bulunmamaktadır..")
            print("Böyle bir miktar çekemezsiniz..")
        else:
            bakiye -= miktar
            print("Paranız başarıyla çekildi..")
    elif sec==3:
        #Kullanıcıya güncel bakiyesini gösteriyoruz.
        print("Güncel bakiye: ",bakiye)
    elif sec==4:
        #Sistemden çıkış yapıldı.
        print("Çıkış yapıldı..")
        break
    else:
        print("Hatali secim..!")

       