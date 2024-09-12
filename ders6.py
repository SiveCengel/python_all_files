
#!ödevler çözümü
#*girilen iki sayının hangisinin büyük olduğunu bulunuz.
# sayi1=int(input("bir sayı giriniz : "))
# sayi2=int(input("bir sayı daha giriniz : "))
# if sayi1>sayi2:
#     print(f"{sayi1} büyüktür {sayi2}'den")
# elif:
#     print(f"{sayi2} büyüktür {sayi1}")
# else:
#     print(f"{sayi1} sayısı ile {sayi2} sayısı eşittir.")

#*girilen sayının kaç basamaklı olduğunu bulun
# sayi=int(input("bir sayı giriniz : "))
# if sayi<10:
#     print("sayı 1 basamaklıdır!")
# elif sayi<100:
#     print("sayı 2 basamaklıdır.")
# elif sayi<1000:
#     print("sayı 3 basamaklıdır.")
# elif sayi<10000:
#     print("sayı 4 basamaklıdır.")
# else:
#     print("sayı çok basamaklıdır.")


# yas=int(input("Yasinizi giriniz:"))
# if yas>0 and yas<18:
#     print("küçüksünüz")
# elif yas<18 and yas<35:
#     print("gençsiniz")
# elif yas<35 and yas<55:
#     print("yetişkinsiniz")
# elif yas<55 and yas<75:
#     print("yaslisiniz")
# else:
#     print("lütfen geçerli bir değer giriniz")

#?alternatif len()
# girilensayi=input("sayı giriniz : ")
# girilensayi=len(girilensayi)
# print(f"girilen sayının basamak sayısı : {girilensayi}")


#*100lük sistemde girilen notu 5lik sisteme çevirin(87=>5)
# girilenNot=int(input("ortalamanızı giriniz : "))

# if girilenNot<45:
#     print("karnenize 1 olarak düştü")
# elif girilenNot<55:
#     print("karnenize 2 olarak düştü")
# elif girilenNot<69:
#     print("karnenize 3 olarak düştü")
# elif girilenNot<84:
#     print("karnenize 4 olarak düştü")
# elif girilenNot<=100:
#     print("karnenize 5 olarak düştü")

#*alınan iki sayının girilen harfe göre dört işlem yapan uygulamayı yazınız.
#*örn: toplama=t 

# sayi1=int(input("1.sayıyı girin : "))
# sayi2=int(input("2.sayıyı giriniz : "))
# islem=input("yapmak istediğiniz işlemi seçiniz!\n Toplama=t\nÇıkartma=ç\nÇarpma=x\nBölme=b")

# if islem=="t":
#     sonuc=sayi1+sayi2
#     print(f"Toplamların sonuc : {sonuc}")
# elif islem=="ç":
#     sonuc=sayi1-sayi2
#     print(f"çıkartma sonucu : {sonuc}")
# elif islem=="x":
#     sonuc=sayi1*sayi2
#     print(f"çarpma sonucu : {sonuc}")
# elif islem=="b":
#     sonuc=sayi1/sayi2
#     print(f"çıkartma sonucu : {sonuc}")
# else:
#     print("yanlış bir tuşlama yaptınız!")

#*kullanıcıya sinema yada tiyatro tercihi sorulsun 
#*sinema izlemek için 50tl
#*tiyatro için 100tl ödemesi gerekmektedir.
#*öğrencilere %50 indirim yapıldığı düşünülerek
#*öğrenci ise indirim yapılsın
#*öğrenci değilse indirimsiz tutatı hesaplayarak ekrana yazdıran kodu yazınız

# sinema,tiyatro=50,100
# tercih=input("sinema mı? tiyatro mu?")
# if tercih=="sinema":
#     ogrenci=input("öğrenci misin?")
#     if ogrenci=="e":
#        sinemaIndırım=sinema*0.5
#        print("öğrenci indirimi uygulandı.tutar: ",sinemaIndırım)
#     else:
#         print("ödenecek tutar :",sinema)
# elif tercih=="tiyatro":
#     ogrenci=input("öğrenci misin?")
#     if ogrenci=="e":
#        tiyatroIndırım=tiyatro*0.5
#        print("ögrenci indirimi uygulandı.Tutar :",tiyatroIndırım)
#     else:
#         print("ödenecek tutar :",tiyatro)
# else:
#     print("hatalı seçim")

#*kullanıcının girdiği 2 sayıyı bölünüz. bölüm ve kalanı ekrana yazdır

# bolunen=int(input("bir sayı giriniz : "))
# bolen=int(input("bir sayı daha : "))
# bolum=bolunen/bolen
# kalan=bolunen%bolen
# print(f"Bölüm : {int(bolum)}\n Kalan : {kalan}")

#!and /or (&& -||) (ve -veya)
#?ve veya anlamına gelmektedir.

#*sisteme giriş örneği
# kadi="sive"
# sifre="1234"
# if kadi=="sive" and sifre=="1234":
#     print("sisteme hoşgeldiniz!")
# else:
#     print("hatalı giriş!")


#*kullanıcıdan kadi ve şifre alınız karşılaştırma yapıp girişi sağlayın
# kadi="sive"
# sifre="1234"
# girilenKadi=input("Kullanıcı adı giriniz : ")
# girilenSifre=input("Bir şifre giriniz : ")
# if kadi==girilenKadi and sifre==girilenSifre:
#     print("Hoşgeldin",kadi)
# elif girilenKadi!=kadi or girilenSifre!=sifre:
#     print("Kullanıcı Adı veya Şifre Yanlış")
# else:
#     print("Lütfen Bilgilerinizi Giriniz")

#*Kullanıcının girdiği 3 sayının en büyüğünü bulun

# sayi1=int(input("1. sayıyı giriniz : "))
# sayi2=int(input("2. sayıyı giriniz : "))
# sayi3=int(input("3. sayıyı giriniz : "))

# if sayi1>sayi2 and sayi1>sayi3:
#     print("En büyük sayı",sayi1)
# elif sayi2>sayi1 and sayi2>sayi3:
#     print("En büyük sayı",sayi2)
# else:
#     print("En büyük sayi",sayi3)

#*kullanıcıdan bir şifre ve kullanıcı adı oluşturmasını isteyin
#*eğer kullanıcı adı veya şifre en az 8 karakterden oluşuyorsa 
#*uyarı mesaı olarak 8 karakteerden az yazsın

# kadi=input("Bir kullanıcı adı giriniz : ")
# sifre=input("Bir şifre giriniz : ")
# kadilen,sifrelen=len(kadi),len(sifre)
# if kadilen<8 or sifrelen<8:
#     print("Kullanıcı adı veya sifre 8 karakterden az olamaz!")
# else:
#     print("kayıt başarıyla oluşturuldu",kadi)

#*bir kişi mağazadan 100tl ve üzeri alışveriş yaparsa %10
#*200tl ise %15,300 tl ve üzeri alışverişe %20 indirim kazandığını ve
#*ödeyeceği miktarı ekrana yazınız

# fiyat=int(input("fiyat giriniz : "))

# if fiyat>=100 and fiyat<200:
#     fiyat-=fiyat*0.10
#     print(f"%10 indirim kazandırınız!Ödenecek tutar {fiyat}")
# elif fiyat>=200 and fiyat<300:
#     fiyat-=fiyat*0.15
#     print(f"%15 İndirim Kazandınız! Ödenecek tutar : {fiyat}")
# elif fiyat>=300:
#     fiyat-=fiyat *0.20
#     print(f"%20 İndirim Kazandınız! Ödenecek  Tutar : {fiyat}")
# else:
#     print("Ödenecek Tutar :",fiyat)
 
