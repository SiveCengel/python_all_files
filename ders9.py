
#?liste içerisindeki elemanları yazdırmak

# meyveler=["elma","armut","karpuz","kivi"]

# for i in meyveler:
#     print(i)

  
#*bir sayısal loto oyunu yapınız!
#*rastgele 3 adet rakam oluşturunuz ve kullanıcıdanda 3 adet tahmin rakamı isteyiniz
#*kullanıcıdan bahis miktarınıda giriniz
#*sıraya bakmaksızın rastgele oluşturulan 3 rakam ile girilen rakamları karşılaştırınız
#*3 rakamıda bilen kullanıcın bahisini 3e katlayınız
#*2 rakam bilen kullanıcın bahisini 2ye katlayınız
#*1 rakam bilen kullanıcının bahisini amorti olarak geri iade ediniz!
#*örnek olarak 
#*rasgelesayılar = 1,4,7 kulllanıcınTahmini 3,9,1
#*                 1,4,6 => 1,4,6 
#*bu durumda amorti kazanılır ve bahis iade edilir
# import random
# tutulanSayilar=[]

# for i in range(3):
#     rastgeleSayi=random.randint(1,10)
#     tutulanSayilar.append(rastgeleSayi)
#     print(tutulanSayilar)

# girilenBakiye=int(input("Ne kadarlık oynamak istersiniz : "))

# sayi1=int(input("Lütfen 1. sayıyı giriniz : "))
# sayi2=int(input("Lütfen 2. sayıyı giriniz : "))
# sayi3=int(input("Lütfen 3. sayıyı giriniz : "))

# sayac=0
# if sayi1==tutulanSayilar[0]:
#   sayac+=1
# if sayi2==tutulanSayilar[1]:
#   sayac+=1
# if sayi3==tutulanSayilar[2]:
#   sayac+=1
  
# print(sayac)

#?alternatif
# import random

# tutulanSayilar = []

# for i in range(3):
#   rastgeleSayi = random.randint(1,10)
#   tutulanSayilar.append(rastgeleSayi)
  
# print(tutulanSayilar)

# girilenBakiye = int(input("Ne kadarlık oynamak isterseniz : "))

# say1 = int(input("Lütfen 1. Sayıyı Giriniz : "))
# say2 = int(input("Lütfen 2. Sayıyı Giriniz : "))
# say3 = int(input("Lütfen 3. Sayıyı Giriniz : "))

# sayac=0
# if say1 in tutulanSayilar:
#   sayac+=1
#   tutulanSayilar.remove(say1)
# if say2 in tutulanSayilar:
#   sayac+=1
#   tutulanSayilar.remove(say2)
# if say3 in tutulanSayilar:
#   sayac+=1
#   tutulanSayilar.remove(say3)
  
# print(sayac)

#?break komutu

# meyveler=["elma","armut","kivi","karpuz","kavun"]

# for i in meyveler:
#     if i=="armut":
#         print(i)
#         break


#?continue ile döngüyü başa almak

# for i in range(10):
#     if i==3:
#         continue   #*continue gördüğünde alt satırı okumadan başa döner
#     print(i)


#?else ile for kullanımı
#*else döngü bittiğinde devreye girer ve gelende döngünün bittiğini gösterir.

# for i in range(5):
#     print(i)
# else:
#     print("döngü bitti")

#?örnekler
#*1'den 100e kadar olan tek sayıları yazınız

# for i in range(1,100,2):
#   print(i)

#?alternatif
# for i in range(1,100):
#   if i%2!=0:
#     print(i)


#*0'den 100e kadar olan çift sayıları yazını
# for i in range(0,100+1,2):
#   print(i)

#?alternatif
# for i in range(0,100+1):
#   if i%2==0:
#     print(i)

#* 0'dan 100 yanlızca 5'e bölünebilen rakamları yazdırınız!

# for i in range(0,100):
#   if i%5==0:
#     print(i)


#* 1'dan 100 e kadar 3 ve 7 ye tam bölünenler

# for i in range(1,100):
#   if i%3==0 and i%7==0:
#     print(i)


#*1den 100e kadar olan tek ve çift sayıları ayrı ayrı
#*arraylere append ile ekleyiniz daha sonra bu iki arrayi
#*ekrana yazıdırınız

# tek =[]
# cift=[]

# for i in range(1,20+1):
#   if i%2==0:
#     cift.append(i)
#   else:
#     tek.append(i)
    
# print(tek,cift)

#*meyveler listesinde her eleman sırasıyla gelsin ve karşılığında fiyatları yazılsın
 
# meyveler = ["elma","armut","karpuz","kavun"]

# for i in meyveler:
#   if i=="elma":
#     print(f"{i} 10TL")
#   elif i=="armut":
#     print(f"{i} 20TL")
#   elif i=="karpuz":
#     print(f"{i} 30TL")
#   elif i=="kavun":
#     print(f"{i} 40TL")
 
 

#*renkler listesinden yeşil olaan değerlere kadar değerleri yazdırınız

# renkler = ["mavi","turuncu","beyaz","kırmızı","yeşil","siyah","gri"]

# for i in renkler:
#   print(i)
#   if i=="yeşil":
#     break
  


#*renkler listesinde mavi hariç bütün elemanları yazdırınız
# renkler = ["mavi","turuncu","beyaz","kırmızı","yeşil","siyah","gri"]

# for i in renkler:
#   if i=="mavi":
#     continue
#   print(i)


#!ÖDEVLER
#*bir dict içerisinde ürünler olsun ve karşılığında fiyat listesi olsun
#*dict içerisindeki ürünlerin fiyatlarını toplamını ekrana yazınız
# urunler = {
#     "kitap": 10,
#     "kalem": 5,
#     "defter": 15,
#     "silgi": 3
# }
# toplamFiyat = sum(urunler.values())
# print(toplamFiyat)

# urunler = {
#     "kitap": 10,
#     "kalem": 5,
#     "defter": 15,
#     "silgi": 3
# }
# toplamFiyat = 0
# for urunlerfiyati in urunler.values():
#     toplamFiyat += urunlerfiyati

# print(toplamFiyat)


#?alternatif
# urunFiyat=[]

# urunler={
#   "çokonat":10,
#   "biskevit":5,
#   "dondurma":20,
#   "cips":20
# }
# for k,v in urunler.items():
#   urunFiyat.append(v)

# urunlerinToplami=sum(urunFiyat)  #?sum dizi içindeki değerlerin toplamını döndürür
# print(f"ürünlerin toplamı :{urunlerinToplami}")


#*kullanıcıdan 0'ın üstünde bir sayı isteyiniz!
#* 0'dan girilen sayıya kadar olan sayıların toplamını ekrana yazınız

# sayi= int(input("Lütfen 0'dan büyük bir sayı giriniz: "))

# if sayi> 0:
#     toplam= sum(range(1, sayi+1))
#     print(toplam)
# else:
#     print("Lütfen geçerli bir sayı giriniz.")

#?alternatif
# girilensayi=int(input("Lütfen 0 dan büyük bir sayı girin : "))

# toplam=0
# for i in range(girilensayi+1):
#   toplam +=i

# print(toplam)



#*kullanıcıdan 0'ın üstünde bir sayı isteyiniz!
#* 0'dan girilen sayıya kadar olan tek sayıların toplamını bir değişkene
#* çift sayıların toplamını bir değişkene atınız

# sayi= int(input("Lütfen 0'dan büyük bir sayı giriniz: "))

# tekSayi=0
# ciftSayi=0
# if sayi>0:
#     for i in range(1,sayi+1):
#         if i%2==0:
#             ciftSayi+=i     
#         else:
#             tekSayi+= i
#     print("çift sayıların toplamı",ciftSayi)
#     print("tek sayıların toplamı : ",tekSayi)
# else:
#     print("geçersiz sayı")

#?alternatif


# tekToplam=0
# ciftToplam=0
# girilensayi=int(input("sayıyı giriniz: "))
# for i in range(girilensayi):
#   if i%2==0:
#     ciftToplam=ciftToplam+i
#   else:
#     tekToplam=tekToplam+i

# print(f"çift toplam: {ciftToplam}\nTek toplam: {tekToplam}"
#*rastgele üretilen 1-50 arası bir sayıyı kullanıcı 5 hakta bulmaya çalışacak
#*kaçıncı defada sayıyı tahmin ettiği hakkında veri tutulacak
#*örnek "tebrikler 3. tahmininde sayıyı bildin!"

# import random

# sayi = random.randint(1, 50)
# denemeler = 0

# for i in range(5):
#     tahmin = int(input("Lütfen 1-50 arasında bir sayı tahmin edin: "))
#     denemeler += 1
#     if tahmin == sayi:
#         print("Tebrikler, {}. deneme de sayıyı buldunuz!".format(denemeler))
#         break
#     elif tahmin < sayi:
#         print("Daha yüksek bir sayı deneyin.")
#     else:
#         print("Daha düşük bir sayı deneyin.")
# else:
#     print("Tahmin hakkınız bitti. Sayı: {}".format(sayi))

#?alternatif

# import random
# rndSayi=random.randint(1,50)
# print(rndSayi)
# bilinmeSayisi=1

# for i in range(5):
#   girilenSayi=int(input("Tahmin sayısını giriniz : "))
#   if girilenSayi==rndSayi:
#     print(f"Tebrikler {bilinmeSayisi}. defada bildiniz!")
#     break
#   else:
#     bilinmeSayisi+=1
#     if i==4:
#       print("Hakkınız doldu! bilemediniz :(")

#*kullanıcıdan şifresiniz isteyiniz
#*3 kere yanlış girme hakkı olsun
#* her yanlış girdiğinde kaç hakkı olduğunu mesaj olarak versin
#* "şiferyi yanlış girdiniz kalan hakkınız 2" gibi
#*şifre doğru girildiğinde "sisteme hoşgeldiniz" mesajı veriniz

# sifre = "1234"
# denemeler = 3

# for i in range(3):
#     kullanicisifre = input("Lütfen şifrenizi giriniz: ")
#     if kullanicisifre == sifre:
#         print("Sisteme hoşgeldiniz.")
#         break
#     else:
#         denemeler -= 1
#         print("Şifreniz yanlış. Kalan hakkınız: %d" % denemeler)
# else:
#     print("Şifre deneme hakkınız doldu.")

#?alternatif
# sifre="123"
# hak=3
# for i in range(3):
#   girilensifre=input("Şifrenizi giriniz : ")
#   if girilensifre==sifre:
#     print("Hoşgelndiniz.")
#     break
#   else:
#     hak-=1
#     print(f"Yanlış şifre kalan hakkınız : {hak}")
#     if hak==0:
#       print("Hakkınız bitti 1 dakika sonra deneyin!")

#*boş bir dizi oluşturun
#*kullanıcıdan kaç adet user eklemek istediğini sorun
#*kullanıcı adı ve şifrenizi giriniz
#*kullanıcı adı ve şifrenizi dizi içerisinde ayrı ayrı obje olarak oluşturun

# kullanicilar = []
# girilenKsayisi = int(input("Lütfen Kaç Ader Kullanıcı Oluşturucağınızı Yazını : "))

# for i in range(girilenKsayisi):
#   girilenKadi = input("Kullanıcı Adınız : ")
#   girilenSifre = input("Şifrenizi Giriniz :")
  
#   kullanicilar.append({"kadi":girilenKadi,"sifre":girilenSifre})

# print(kullanicilar)


#*dizi içerisinde objelerle birden fazla kullanıcı oluşturunuz
#*döngü kullanarak kullanıcıların kullanıcı adi ve sifresini alıp giriş yaptırın 

# kullanicilar = [
#   {
#     "kadi":"sive",
#     "sifre":"123"
#   },
#   {
#     "kadi":"murat",
#     "sifre":"456"
#   },
#   {
#     "kadi":"imge",
#     "sifre":"789"
#   }
# ]

# girilenKadi = input("Kullanıcı Adınızı Giriniz : ")
# girilenSifre = input("Şifrenizi Giriniz : ")

# for i in range(len(kullanicilar)):
#   if girilenKadi==kullanicilar[i]["kadi"] and girilenSifre==kullanicilar[i]["sifre"]:
#      print("hoşgeldin")
#      break
  
# if girilenKadi!=kullanicilar[i]["kadi"] and girilenSifre!=kullanicilar[i]["sifre"]:
#     print("Kullanıcı Adı veya Şifre Hatalı")

#?alternatif
# for i in range(len(kullanicilar)):
#   if girilenKadi==kullanicilar[i]["kadi"] and girilenSifre==kullanicilar[i]["sifre"]:
#     kontrol = True
#     break
#   else:
#     kontrol = False     
  
# if kontrol==True:
#   print("hg")
# else:
#   print("yanlış")




"""
  *Şifre doğrulama yapan bir sistem yazınız toplamda 3 hakda bulunması gerekiyor şifrenin
  *eğer şifre yanlış girilirse parolayı unuttunmu diye sorulsun
  *hayır derse direkt olarak sistemden çıkılsın evet derse kayıt olunurken girilen mail adresi
  *ve gizli cevabı cevaplasın doğru bildiği zaman yeni şifre belirlensin ve yeni şifre ile giriş yapılsın
"""
































#?else ile for kullanımı
#*else döngü bittiğinde devreye girer ve genelde döngünün bittiği

#?örnekler
#*1 den 100 e kadar olan tek sayıları yazınız.
# for i in range(1,101):
#     if i % 2 != 0:
#         print(i)


#*0 dan 100 e kadar olan çift sayıları yazınız.
# for i in range(0,101,2):
#     print(i)


#*0 dan 100 yanlızca 5 e bölünebilen rakamları yazdırınız.

# for i in range(101):
#     if i % 5 == 0:
#         print(i)


#*1 den 100 e kadar 3 ve 7 ye tam bölünebilenler

# for i in range(1,101):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i)

#* 1 den 100 e kadar olan tek ve çift sayıları ayrı ayrı arraylere
#*append ile ekleyiniz daha sonra bu iki array i ekrana yazdırınız.

# tekSayilar=[]
# ciftSayilar=[]

# for i in range(1,101):
#     if i%2==0:
#         ciftSayilar.append(i)
#     else:
#         tekSayilar.append(i)
# print(tekSayilar,ciftSayilar)



#*meyveler listesinde her eleman sırasıyla gelsin ve karşılığında fiyatları yazılsın

#*renkler listesinden yeşil olan değerlere kadar değerleri yazdırınız

#*renkler listesinde mavi hariç bütün elemanları yazdırınız.
