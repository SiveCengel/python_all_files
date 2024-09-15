
#!ileri seviye if sorguları
#?ileri seviye if sorguları for şeklinde de çalışabilir.

# meyveler=["elma","armut","kavun","karpuz","kivi"]

# if "elma" in meyveler:
#     print("Bu listede elma var")
# else:
#     print("Bu listede elma yok")

#*örnek
# meyveler=["elma","armut","kavun","karpuz","kivi"]
# renkler=["kırmızı","mavi","pembe","yeşil"]

# if "elma" in meyveler and "yeşil" in renkler:
#     print("Her iki arrayde de mevcut")

#*bir metin içerisinde kullanıcının girdiği kelimeyi metinde arayan kod satırlarını yazınız.

#*yanlış ama olsun dursun.
# metin=input("metin girin :")

# if "cümle" in metin:
#     print("evet o kelime var")

#*doğru bence
# metin="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# kelime=input("Aranacak kelimeyi girin :")

# if (kelime) in metin:
#     print("Evet o kelime mevcut")
#*bir cümle içinde kullanıcının girdiği kelimeyi aratın
#*bu kelimenin kaç defa kullanıldığını da yazınız.

# metin="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# kelime=input("Aranacak kelimeyi girin :")
# kelimeSay=metin.count(kelime)

# if kelime in metin:
#     print(f"Aranan kelime cümle içerisinde mevcut {kelimeSay} tane vardır.")
# else:
#     print(f"Aranan kelime yok")

#*kullanıcıdan bir harf alınız.
#*sesli harf girildiğinde sesli harf girildi şeklinde mesak veriniz.
# harf=input("Lütfen bir harf giriniz :")
# sesliHarfler="aeıioöuüAEIİOÖUÜ"

# if harf in sesliHarfler:
#     print("Sesli bir harf girdiniz")
# else:
#     print("Sessiz harf girdiniz.")

#*bir dict yapısı oluşturunuz if sorgusu ile dict içerisinde

#?key sorgulama
# kisiler={
#     "isim":"sive",
#     "yas":"32",
#     "maas":234556,
#     "sifre":123
# }
# if "maas" in kisiler:
#     print(f"Maaş değeri var. Value:{kisiler['maas']}")
# else:
#     print("yok")

#?value sorgulama()
# kisiler={
#     "isim":"sive",
#     "yas":"32",
#     "maas":234556,
#     "sifre":123
# }
# if "sive" in kisiler.values():
#     print("sive var")
# else:
#     print("sive yok")

#?alternatif
# kisiler={
#     "isim":"sive",
#     "yas":"32",
#     "maas":234556,
#     "sifre":123
# }
# bosArray=[]
# for i in kisiler.values():
#     bosArray.append(i)
# print(bosArray)

#*meyveler içerisinde girilen key karşılığında value yazdır

# meyveler={
#     "kiraz":10,
#     "elma":20,
#     "kivi":30
# }
# deger=input("değeri giriniz")
# if deger in meyveler:
#     print(meyveler[deger])


#!while 
#?bir döngü çeşitidir.
#*sonsuz döngülerde kullanılabilir

# for i in range(5):
#     print(i)

# i=0
# while i<=5:
#     i+=1
#     print(i)

#*döngü sayısı 3 e ulaştığında döngüden çık
# i=1
# while i<10:
#     print(i)
#     if i==3:
#         break
#     i+=1

#*1 den 10 a kadar olan sayıları yazınız 3 rakamı hariç.
# i=1
# while i<=10:
#     if i!=3:
#         print(i)
#     i+=1

#?alternatif
# i=0
# while i<=10:
#     i+=1
#     if i==3:
#         continue
#     print(i)


# i=0
# while i<5:
#     i+=1
#     print(i)
# else:
#     print("döngü bitti")

#?while ile sonsuz döngü

# i=0
# while True:
#     print(i)
#     i+=1


# i=0
# while True:
#     i+=1
#     if i==100:
#         break
#     print(i)

# i=0
# kadi="sive"
# while True:
#     i+=1
#     girilenKadi=input("Kullanıcı adınızı giriniz :")
#     if girilenKadi==kadi:
#         print("Sisteme hoşgelndiniz")
#     else:
#         print("Kullanıcı adı yanlış tekrar deneyin")

# kadi="sive"
# i=0
# while True:
#     girilenKadi=input("lütfen kullanıcı adı giriniz :")
#     if girilenKadi==kadi:
#         print("Hoşgeldiniz")
#         break
#     else:
#         print("Yanlş giriş")
#         break

 #*while döngüsü ile 1-100 arasındaki sayıların tek ve çiflerini yazdırınız

# tekSayilar=[]
# ciftSayilar=[]
# i=1
# while i<=100:
#     if i%2==0:
#         ciftSayilar.append(i)  
#     else:
#         tekSayilar.append(i)
#     i+=1
# print("Çift Sayılar :",ciftSayilar)
# print("Tek sayılar :",tekSayilar)


#*1- 100 e kadar tek sayıları üzerine ekleyerek toplamını hesaplayalım.
# toplam=0
# i=1
# while i<=100:
#     if i%2==1:    
#         toplam=toplam+i
#     i+=1 
# print("Tek sayıların toplamı :",toplam)


#*varolan bir listedeki elemanları ekrana yazdırınız

# liste=["kalem","kağıt","defter","kitap","silgi"]
# i=0
# while i<len(liste):
#     print(liste[i])
#     i+=1

#*başlangıcı , bitiş ve artış değerlerini kullanıcının belirlediği bir döngü oluşturun

# baslangicdegeri=int(input("Başlangıç değerini giriniz : "))
# artisdegeri=int(input("Artış değerini giriniz : "))
# bitisdegeri=int(input("Bitiş değeri giriniz :"))

# i=baslangicdegeri
# while i<bitisdegeri:
#     print(i)
#     i+=artisdegeri

#*girilen metinsel ifadeyi harf harf alt alta yazdırınız 

# metin=input("Bir metin giriniz : ")
# i=0
# while i<len(metin):
#     print(metin[i])
#     i+=1


#*başlangıcı , bitiş kullanıcının belirlediği bir döngü oluşturun
#* 3e ve 5e bölünen sayıları ekrana yazdırınız

# baslangicdegeri=int(input("Başlangıç değeri giriniz : "))
# bitisdegeri=int(input("Bitiş değeri giriniz : "))

# i=baslangicdegeri
# while i<bitisdegeri:
#     if i%3==0 and i%5==0:
#         print(i)
#     i+=1

#* 100'den 1e kadar olan sayıları azalan şekilde yazınız

# i=100
# while i>1:
#     print(i)
#     i-=1

#*Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.

# sayilar=[]
# i=0
# while i<5:
#     alinansayilar=int(input("Sayı giriniz :"))
#     sayilar.append(alinansayilar)
#     i+=1
# sayilar.sort() 
# print(sayilar)


#*kullanıcıya kaç ürün ekleyeceğinizi sorunuz
#*eklenecek ürünlerim adını ve fiyatını isteyiniz (obje olarak verileri tutunuz)
#*ürünler eklendikten sonra ürünleri döngü ile listeleyiniz

# urunler={}
# urunAdet=int(input("Kaç adet ürün eklemek istersiniz? : "))

# i=0
# while i<urunAdet:
#     urunAdi=input("Ürün adı giriniz : ")
#     urunFiyat=int(input("Ürün fiyatı giriniz : "))
#     urunler[urunAdi]=urunFiyat
#     i+=1
# for urunAdi,urunFiyat in urunler.items():
#   print(f"{urunAdi}:{urunFiyat}")


#*zor ödev sorusu
"""
  *bir obje içerisinde ürünler ve karşılığında fiyatları bulunan bir liste yapısı hazırlayınız
  * sonsuz bir döngüde sürekli olarak almak istediği ürünü sorunuz
  * bir sonraki sorusu ise alışverişe devam etmek istermisiniz gibi soru yöneltin
  * evet dediği sürece alışveriş yapmaya devam edecek müşteri
  * hayır dediğinde seçtiği ürünleri bir liste içerisine gönderip toplamlarını alınız!
"""

# urunler={
#   "karpuz":10,
#   "kavun":20,
#   "kivi":30,
#   "gofret":5,
#   "elma":10,

# }

#* ne almak istersin => karpuz (10)
# * alışverişe devam e/h
#* ne almak istersin



#? erdinç algortima
# olusturulansifre = input("yeni şifrenizi oluşturun : \n")
# cıktı = ""

# for i in range(len(olusturulansifre)):
  
#   test = int(ord(olusturulansifre[i])) + olusturulansifre[::-1].index(olusturulansifre[i]) + 3
#   cıktı += (chr(test))
#   print(olusturulansifre[::-1].index(olusturulansifre[i]))

# print(cıktı)