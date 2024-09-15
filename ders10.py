
#!dict işlemleri
#?veri çekmek
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# print(kullanici["isim"])

#?veri güncellemek update()

# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }

# kullanici.update({"yas":30})
# print(kullanici)

#?veri eklemek 
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# kullanici["meslek"]="web dev."
# print(kullanici)

#?veri silme
#*pop()içerisine key değeri alarak o veriyi siliyor
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# kullanici.pop("yas")
# print(kullanici)

#*popitem()
#*dict içerisindeki son veriyi direct olarak siler
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# kullanici.popitem()
# print(kullanici)

#!dict işlemleri ile for
#?key ile verilere ulaşmak
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# for i in kullanici.keys():
#     print(i)

#?values ile verilere ulaşmak
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# for i in kullanici.values():
#     print(i)

#?items ile verilere ulaşmak
# kullanici={
#     "isim":"sive",
#     "yas":"32",
#     "maas":"1234"
# }
# for k,v in kullanici.items():
#     print(k,v)

#!sezar şifreleme algoritması

#?ilk şifreleme algoritması(hashing)

# plainText="sive"
# myTest=""

# for i in range(len(plainText)):
#     test=int(ord(plainText[i])) +3   #?string ascii karşılığı
#     myTest+=(chr(test))              
# print(myTest)


#*for yapısını kullanarak aşşağıdaki yapıyı ekrana çıkartınız
"""
  *
  **
  ***
  ****
  *****
  ******
  *******
  ********
  *********
"""

# for i in range(10):
#     print(i*"*")
    
#*for yapısını kullanarak aşşağıdaki yapıyı ekrana çıkartınız
"""
  *
  **
  ***
  ****
  *****
  ****
  ***
  **
  *
"""
# for i in range(5):
#     print(i*"*")
#     if i==4:
#         for j in range(5,0,-1):
#             print(j*"*")


#!iç içe for kullanımı

# for i in range(3):
#     for j in range(2):
#         print(i)

#!ödevler
#*0'dan 10a kadar olan sayıları 3 kere yazdırın

# for i in range(0,10):
#     for j in range(3):
#         print(i)


#*0'dan 10a kadar olan sayıları 2 kere yazdırın ama 5 sayısını yazdırmayın

# for i in range(0,10):
#     for j in range(2):
#         if i==5:
#             continue
#         print(i)

#*0'dan 10a kadar olan sayıları 2 kere yazdırın ama 3 ve 7 sayısını yazdırmayın

# for i in range(0,10):
#     for j in range(2):
#         if i==3:
#             continue
#         elif i==7:
#             continue
#         print(i)



#!ödev
""""
  Şifre doğrulama yapan bir sistem yazınız toplamda 3 hakda bulunması gerekiyor şifrenin
  eğer şifre yanlış girilirse parolayı unuttunmu diye sorulsun
  hayır derse direkt olarak sistemden çıkılsın evet derse kayıt olunurken girilen mail adresi
  ve gizli cevabı cevaplasın doğru bildiği zaman yeni şifre belirlensin ve yeni şifre ile giriş yapılsın
  eski oluşturulan şifre ile yenisi aynı olmamalı
"""
# sifre="1234"
# email="sive@sive.com"
# gizliSoru="En sevdiğin çizgi film karakteri nedir?"
# gizliCevap="casper"

# deneme=0
# while deneme<3:
#     girilenSifre=input("Lütfen şifrenizi giriniz : ")
#     if girilenSifre==sifre:
#         print("Sisteme Hoşgeldiniz!")
#         break
#     else:
#         print("Yanlış şifre girdiniz.Tekrar deneyin.")
#         deneme+=1
#         if deneme==3:
#             sifremiUnuttum=input("Şifrenizi mi unuttunuz? e/h " )
#             if sifremiUnuttum=="e":
#                 girilenEmail=input("Email adresinizi giriniz : ")
#                 if girilenEmail==email:
#                     girilenGizliSoru=input(f"Gizli sorunuz :{gizliSoru}")
#                     girilenGizliCevap=input("Gizli Cevabınızı giriniz : ")
#                     if girilenGizliCevap==gizliCevap:
#                         yeniSifre=input("Yeni şifrenizi giriniz : ")
#                         while yeniSifre==sifre:
#                             yeniSifre=input("Şifreniz eski şifreyle aynı olamaz.Lütfen yeni şifre girin :")
#                             if yeniSifre!=sifre:
#                                 print("Parolanız sıfırlandı. Giriş yapınız.")
            #         else:
            #             print("Gizli soruya verdiğiniz cevap yanlış.")
            #     else:
            #         print("E-posta adresi yanlış.")
            # else:
            #     print("Sistemden çıkılıyor.")




#!sezar şifrelemeyi tam tersine çeviriniz
#!kendi algoritmanızı yaratarak şifreleyinzi!






