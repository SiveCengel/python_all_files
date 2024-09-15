
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

# say1=input("1.sayı : ")
# say2=input("2.sayı : ")

# if say1.isnumeric() and say2.isnumeric():
#     say1,say2=int(say1),int(say2)
#     print(say1+say2)
# else:
#     print("Lütfen rakam giriniz!")


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
# islemler=["para çek","para yatır"]
# sifre="1234"
# bakiye=1000
# girilensifre=input("Bankamıza Hoşgeldiniz\n Şifrenizi giriniz : ")

# if girilensifre==sifre:
#     print(f"Girilen Şifre Doğru!\n Bakiyeniz : {bakiye}")
#     secilenislem=input("Lütfen yapılacak işlemi seçiniz : ")

#     if secilenislem==islemler[0]:
#         cekilentutar=int(input("Ne kadar çekmek istersiniz ?"))
#         if cekilentutar<=bakiye:
#             bakiye-=cekilentutar
#             print(f"para çekme işleminiz tamamlandı! Kalan tutar :{bakiye}")
#         else:
#             print("yetersiz bakiye")
#     elif secilenislem==islemler[1]:
#         yatirilantutar=int(input("yatırmak istediğiniz tutar : "))
#         bakiye+=yatirilantutar
#         print(f"para yatırma işlemi tamamlanmıştır! toplam tutar : {bakiye}")
#     else:
#         print("hatalı bir işlem yaptınız!")
# else:
#     print("Hatalı Şifre.Lütfen tekrar deneyiniz!")

#! date time 
#*zaman dilimi olarak kullanılır

# import datetime

# zaman=datetime.datetime.now()  #?şuanki zaman
# print(zaman)

# x=datetime.datetime.now()
# print(x.year)       #?yıl
# print(x.month)     #?ay
# print(x.day)       #?gün
# print(x.hour)     #?saat
# print(x.minute)   #?dakika
# print(x.second)   #?saniye
# print(x.timestamp()*1000) #?milisaniye

#!random()
#*ratgele amlamına gelir (sayı,değişken vs. atamak için kullanılır)

# import random

# print(random.randrange(1,10))  #*aralık belirterek ramdom sayı oluşturulur.


# meyveler=["elma","armut","kavun","kivi","ananas"]
# secileneleman=random.choice(meyveler)   #*rastgele dizi içinden bir değişkeni bize döncürür
# print(secileneleman)

#*basit bir sayı tahmini oyunu yapınız 1 ile 50 arasında 
#*kullanıcı sayıyı bildiğinde bildiniz bilemediğinde bilemediniz mesajı göndersin

# import random

# rnddeger=random.randrange(1,50)
# print(rnddeger)
# girilendeger=int(input("Lütfen tahmininizi giriniz : "))

# if rnddeger==girilendeger:
#     print(f"makinenin tuttuğu değer {rnddeger}! Tebrikler Bildiniz")
# else:
#     print("maalesef bilemediniz!")


#*hava durumlarının olduğu bir liste tutunuz
#*örnek= havadurumu[yağışlı,karlı,güneşli]
#*rastgele değer alıp değer karşılığında if else kullanarak mesajlar bastırınız

# import random
# havaDurumu=["yağışlı","karlı","güneşli"]
# rndHavaDurumu=random.choice(havaDurumu)

# if rndHavaDurumu=="yağışlı":
#     print("Bugun hava yağışlı!Şemsiyeni yanına al")
# elif rndHavaDurumu=="karlı":
#     print("Bugun hava karlı!Sıkı giyin!")
# elif rndHavaDurumu=="güneşli":
#     print("bugun hava güneşli! günün tadını çıkar.")
# else:
#     print("hatalı değer")

#*instagram çekiliş uygulaması
#*uygulamada kullanıcı isimlerini klavyeden alınız
#*kazanan sayısı ve yedek sayısı sorulsun
#*kazananlar ve yedekler listelensin

# kazananListesi = []
# yedekListesi = []

# girilenIsimler = input("Kullanıcı Adlarını Aralarında Virgül İle Ayırarak Yazınız")
# girilenIsimler = girilenIsimler.split()

# kazananSayisi = int(input("Lütfen Kazanan Sayısını Giriniz :"))
# yedekSayisi = int(input("Lütfen Yedek Sayısını Giriniz :"))

# for i in range(kazananSayisi): #*
#   kazanan = random.choice(girilenIsimler) #*random kazanan seçtim
#   kazananListesi.append(kazanan) #*kazananı kazanan listesine ekledim
#   girilenIsimler.remove(kazanan) #*kazananı isimlerden sildim
  
# for i in range(yedekSayisi):
#     yedek = random.choice(girilenIsimler)
#     yedekListesi.append(yedek)
#     girilenIsimler.remove(yedek)
    
# print(kazananListesi,yedekListesi)




#!loop (döngü)

#?for yapısı

# for i in range(10+1):  #?0 ile 10 arasındaki rakamları yazar
#     print(i)

#*ekrana 10 kez adınız yazınız
# for i in range(10+1):
#     print("şive")

#? başlangıç ve bitiş değeri vererek

# for i in range(5,10):
#     print(i)

#? artış değeri verilerek

# for i in range(0,22,2):
#     print(i)


#!ödev
#*bilgisayarın saatine ulaşarak saat aralığına göre "günaydın","iyi günler" veya "iyi akşamlar " yazdırınız

# import datetime

# currentTime=datetime.datetime.now().time()
# if currentTime>=datetime.time(06) and currentTime<datetime.time(12):
#     print("Günaydın")
# elif currentTime>=datetime.time(12) and currentTime<datetime.time(17):
#     print("İyi Günler!")
# elif currentTime>=datetime.time(18) and currentTime<datetime.time(06):
#     print("İyi Geceler!")
# else:
#     print("hatalı")

# import datetime

# current_time = datetime.datetime.now().time()

# if current_time >= datetime.time(6) and current_time < datetime.time(12):
#     print("Good morning")
# elif current_time >= datetime.time(12) and current_time < datetime.time(17):
#     print("Good afternoon")
# elif current_time >= datetime.time(17) and current_time < datetime.time(06):
#     print("Good evening")


# from datetime import datetime

# now = datetime.now()
# current_time = now.time()

# if current_time > datetime.strptime("09:00", "%H:%M").time() and current_time < datetime.strptime("17:00", "%H:%M").time():
#     print("Ofis açık")
# else:
#     print("Ofis kapalı")
