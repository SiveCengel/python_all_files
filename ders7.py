
#*kullanici adında bir dict oluşturunuz
#*dict(obje) içerisinde kullanıcıadı ve şifre adında keyler oluşturup value karşılığında değerleri oluşturunuz
#*klavyeden girilen kullanıcıadı ve şifreyi dict içerisindeki verilerle karşılaştırın
#*"hoşgeldiniz kullanici" veya "hatalı kullanıcı adı veya şifre yazdırınız"


# kullanicilar=[{
#         "kadi":"sive",
#         "sifre":"123"
#     },
#     {
#         "kadi":"murat",
#         "sifre":"321"
#     },
#     {
#         "kadi":"eylul",
#         "sifre":"0101"
#     }
# ]
# girilenKadi=input("Kullanıcı adını giriniz : ")
# girilenSifre=input("Şifrenizi giriniz :")

# if girilenKadi==kullanicilar[0]["kadi"] and girilenSifre==kullanicilar[0]["sifre"]:
#     print(f"Hoşgeldiniz! {kullanicilar[0]['kadi']}")
# elif  girilenKadi==kullanicilar[1]["kadi"] and girilenSifre==kullanicilar[1]["sifre"]:
#     print(f"Hoşgeldiniz! {kullanicilar[1]['kadi']}")
# elif girilenKadi==kullanicilar[2]["kadi"] and girilenSifre==kullanicilar[2]["sifre"]:
#     print(f"Hoşgeldiniz! {kullanicilar[2]['kadi']}")
# else:
#     print("Kullanıcı adı veya şifre yanlış")



#*şifresini unutmuş bir kullanıcı olduğunu varsayalım
#*dışarıdan gizlisoru,mailadres adında değişkenler oluşturunuz
#*kullanıcıya gizisorunun cevabını ve mail adresini sorunuz
#*bu iki veriyi karşılaştırınız ve yeni şifre oluşturması için yeni şifrenizi giriniz yazınız
#*kullanıcı yeni şifresini doğrulamak için 2 defa girilmesini isteyin
#*girilen bu iki yeni şifreleri karşılaştırıp eğer aynı şifreler girildiyse "şifreniz değiştirildi yazınız"
#*değilse hatalı giriş yazınız

# gizliSoru="neos"
# mailAdres="neos@neos.com.tr"

# girilenCevap=input("Gizli sorunun cevabı nedir?")
# girilenMail=input("Mail adresinizi giriniz : ")

# if girilenCevap==gizliSoru and girilenMail==mailAdres:
#     print("Cevaplar doğru!")
#     yeniSifre=input("Yeni şifrenizi giriniz : ")
#     yeniSifre2=input("Yeni şifrenizi tekrar giriniz : ")

#     if yeniSifre==yeniSifre2:
#         print("Tebrikler!Şifreniz değiştirildi")
#     else:
#         print("Şifreler uyuşmuyor.Tekrar deneyin")
# else:
#     print("Gizli soru veya mail adresi yanlış")
    

#*bilet satış uygulaması
#*kullanıcıya tiyatro / sinema / gezi mi diye sorulursun
#*kaç adet bilet istediklerinizi sorunuz
#*öğrenci olup olmadığı sorulsun
#*öğrencilere 50% indirim yapınız
#* tam biletler için fiyat listesi::::
    #*sinema:5TL
    #*tiyatro:10TL
    #*gezi:20TL

# # Bilet fiyatlarını tanımla
# sinema_fiyat = 5
# tiyatro_fiyat = 10
# gezi_fiyat = 20

# # Kullanıcıdan bilet türünü seçmesini iste
# bilet_turu = input("Tiyatro, gezi veya sinema bileti seçin: ")

# # Kullanıcıdan bilet adetini iste
# bilet_adet = int(input("Kaç adet bilet istiyorsunuz? "))

# # Kullanıcının öğrenci olup olmadığını sor
# ogrenci_mi = input("Öğrenci misiniz? (evet/hayır) ")

# # Bilet fiyatını hesapla
# if bilet_turu == "sinema":
#     fiyat = sinema_fiyat
# elif bilet_turu == "tiyatro":
#     fiyat = tiyatro_fiyat
# elif bilet_turu == "gezi":
#     fiyat = gezi_fiyat
# else:
#     print("Geçersiz bilet türü seçildi.")
#     exit()

# # Eğer kullanıcı öğrenci ise indirim yap
# if ogrenci_mi == "evet":
#     fiyat = fiyat * 0.5

# # Toplam fiyatı hesapla ve ekrana yazdır
# toplam_fiyat = fiyat * bilet_adet
# print("Toplam fiyat: " + str(toplam_fiyat) + " TL")


#?ikinci çözüm
# sinema,tiyatro,gezi=5,10,20

# print("sinema/tiyatro,gezi")
# secim=input("Lütfen seçiminizi yapınız : ")
# biletadet=int(input("Kaç adet bilet almak istersiniz? : "))
# ogrenciKontrol=input("Öğrenci misiniz? : e/h")

# if (secim=="sinema" or secim=="tiyatro" or secim=="gezi") and ogrenciKontrol=="e":
#     if secim=="sinema":
#         sinema*=biletadet
#         sinema*=0.5
#         print(f"Öğrenci indirimi uygulandı.Ödenecek tutar : {sinema}")
#     elif secim=="tiyatro":
#         tiyatro*=biletadet
#         tiyatro*=0.5
#         print(f"Öğrenci indirimi uygulandı.Ödenecek tutar : {tiyatro}")
#     elif secim=="gezi":
#         gezi*=biletadet
#         gezi*=0.5
#         print(f"Öğrenci indirimi uygulandı.Ödenecek tutar : {gezi}")
#     else:
#         print("hatalı giriş")
# elif (secim=="sinema" or secim=="tiyatro" or secim=="gezi") and ogrenciKontrol=="h":
#     if secim=="sinema":
#         sinema*=biletadet
#         print(f"Öğrenci indirimi uygulanmadı.Ödenecek tutar : {sinema}")
#     elif secim=="tiyatro":
#         tiyatro*=biletadet
#         print(f"Öğrenci indirimi uygulanmadı.Ödenecek tutar : {tiyatro}")
#     elif secim=="gezi":
#         gezi*=biletadet
#         print(f"Öğrenci indirimi uygulanmadı.Ödenecek tutar : {gezi}")
#     else:
#         print("hatalı giriş")
# else:
#     print("tekrar deneyin!")

#*kullanıcıdan girilen 2 veri alıyruz eğer sayılardan oluşuyorsa ikisini
#*toplasın değilse ekrana "yalnızca sayı girilsin"








#!ödev
#*basit bir bankamatik uygulaması oluşturunuz.
#*kullanıcıdan bir şifre alınız şifre doğru olduğuu takdirdeişlemler
#*alanlarına yönlendirilsin
#*para çekme ve para yatırma işlemleri yapılsın

# sifre = input("Lütfen şifrenizi girin: ")
# if sifre == "1234":
#     print("Giriş başarılı. İşlemler için seçim yapın.")
#     print("1. Para Çekme")
#     print("2. Para Yatırma")
#     islem = int(input("Seçiminizi girin (1 veya 2): "))

#     if islem == 1:
#         miktar = int(input("Çekmek istediğiniz miktarı girin: "))
#         print(str(miktar) + " TL çekildi.")
#     elif islem == 2:
#         miktar = int(input("Yatırmak istediğiniz miktarı girin: "))
#         print(str(miktar) + " TL yatırıldı.")
#     else:
#         print("Geçersiz seçim.")
# else:
#     print("Hatalı şifre.")

#?ikinci çözüm

