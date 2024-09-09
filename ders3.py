#*kullanıcının girdiği sayının karesini alan program

# sayi=int(input("Bir sayı giriniz :"))
# sayi =sayi*sayi
# print(sayi)

#?girilen 3 sınavın ortalamasını alan prog.
# sinav1=int(input("1. Sınav notunuzu giriniz :"))
# sinav2=int(input("2. Sınav notunuzu giriniz :"))
# sinav3=int(input("3.sınavı giriniz :"))
# ortalama=(sinav1+sinav2+sinav3)/3
# print(f"Ortalamanız:{ortalama}")

#?kullanıcıdan alınan kullanıcı adının karakter uzunluğunu bulunuz

# girilenKullaniciAdi =input("Lütfen kullanıcı adınızı giriniz :")
# kadiLen= len(girilenKullaniciAdi)
# print(f"Kullanıcı adı uzunluğu : {kadiLen}")

#?kenar uzunluğu yüksekliği girilen üçgenin alanını hesaplayan programı yazınız((k*h)/2)

# kenarUzunlugu= int(input("Kenar Uzunluğu Giriniz : "))
# yukseklik=int(input("yukseklik giriniz : "))
# alan=(kenarUzunlugu*yukseklik)/2
# print(int(alan))

#?kısa kenarın ve uzun kenarın girildiği dikdörtgenin çevresini hesaplayan program

# kisaKenar= int(input("Kısa Kenar Uzunluğu giriniz :"))
# UzunKenar=int(input("Uzun kenar uzunluğu giriniz :"))
# cevre=(kisaKenar+UzunKenar)*2
# print(f"dikdörtgenin çevresi :{cevre}")

#?vizenin %40 finalin %60 alınarak ortalamayı ekrana yazdıran program
# vize=int(input("Vize notunuzu giriniz : "))
# final=int(input("Final notunuzu giriniz :"))
# ortalama=(vize*0.4) + (final*0.6)
# print(f"Ortalamanız :{ortalama}")

#?kullanıcıdan alınan kilo ve boy ile vucut kitle endeksini hesaplayın
# kilo =int(input("kilonuzu giriniz:"))
# boy=float(input("boyunuzu giriniz"))
# i= kilo/(boy*boy)
# print(f"vücut kitle endeksiniz :{i}")


#!stringlerde eleman ayırma işlemi

# mesaj="selam ben sive!"
# print(mesaj)

# mesaj="selam ben sive!"
# print(mesaj[:5]) #?selam kelimesini alır

# mesaj="selam ben sive!"
# print(mesaj[:-3])  #?sondan kaç harfin silineceğini - ile belirtiyoruz.

# mesaj="selam ben sive!"
# print(mesaj[6:9]) #? numaralarına göre sınırlandırma çizip o aralığı alabiliriz.

# mesaj="selam ben sive"
# print(mesaj[-6:]) #?tersten ayırma işlemi

#!string method
#?Lower() (girilen metni küçük harflere dönüştürür)
# text = "SELAM BEN SİVE"
# text = text.lower()
# print(text)

#*örnek
# girilenMetin =input("Kullanıcı adını giriniz(küçük harf) :")
# girilenMetin=girilenMetin.lower()
# if girilenMetin=="sive":
#     print("Hoşgeldin sive")

#?casefold() (girilen metni küçük harflere dönüştürür)
#*casefold lower ile aynı işlemi yapar fakat casefold daha güçlüdür.
# text ="SİVE KANMAZ"
# print(text.casefold())

#? upper() (girilen metini büyük harfe dönüştürme)
# text="sive kanmaz"
# text=text.upper()
# print(text)

#?strip() başındaki ve sonundaki boşlukları siler cümle arasındakilere dokunmaz

# text= "     sive kanmaz           "
# text=text.strip()
# print(text)

#*silinmesini istediğimiz karakterleri belirtip ayıklamasını sağlayabiliriz.
# text="....,,,,,sive kanmaz,,,....***"
# print(text.strip(",.*"))

#?istitle() (bütün kelimelerin baş harfine bakıyor.Büyük harf değilse hepsi false basıyor.)

# text="Sive Kanmaz"
# print(text.istitle())

#*örnek
# kullaniciAdi=(input("Kullanıcı adı giriniz(baş harf büyük olmalı) : "))
# kullaniciAdiKontrol =kullaniciAdi.istitle()
# if kullaniciAdiKontrol==True:
#     print(f"Teşekkürler! {kullaniciAdi}")
# else :
#     print("Lütfen Adınızın Baş harfini büyük giriniz!")

#?count() (metin içerisinde belirttiğimiz kelimenin kaç tane olduğunu döndürür)
# text="Selam ben yazılım çok seviyorum!Çünkü benim işim yazılım"
# text=text.count("yazılım")
# print(text)


#*count la belirli aralıklar arasında arama yapmak mümkün
# text="Selam ben yazılım çok seviyorum!Çünkü benim işim yazılım"
# text=text.count("yazılım".1.25)
# print(text)

#?index()
# text="selam ben sive kanmaz"
# text=text.index("a")
# print(text)

#*indexte belirtilen aralıkta sorgulamak
# text="selam ben sive kanmaz"
# text=text.index("e",5,10)
# print(text)

#?center()
#*yazılan metinin karakter sayısından daha küçük bir ortalama girilemez
# metin="sive kanmaz"
# metin=metin.center(40)
# print(metin)

#*metin karakterlerinde boşlukların içerileri de doldurulabilir.

# metin="sive kanmaz"
# metin =metin.center(23,"*")
# print(metin)

#?split() yazılan metnin
# metin="selam ben sive kanmaz"
# print(metin.split())

# metin="selam ben sive kanmaz"
# metin=metin.split()
# print(metin[0])

#*girilen metni belirli bir karaktere göre parçalama
# aylar="ocak,şubat,mart,nisan,mayıs"
# aylar=aylar.split(",")
# print(aylar)

#*split ile parçalanan arrayin bütün elemanlarını for ile döndürebiliriz

# aylar="ocak,şubat,mart,nisan,mayıs"
# aylar=aylar.split(",")
# for i in aylar:
#     print(i)





#*örnek kullanıcının virgüllerle girdiği kullanıcı adlarını
#*çekiliş uygulaması yazınız!
# isimler=input("Lütfen Kullanıcı İsimlerini virgülle ayırarak giriniz!\n")
# isimler=isimler.split(",")
# import random
# rndIsim=random.choice(isimler)
# print(f"çekilişin kazananı {rndIsim}")


# metin="murat,sive,ümran,yakup,imge"
# metin=metin.split(",")
# import random
# rndIsim=random.choice(metin)
# print(rndIsim)

#?endswith() 
#*cümle sonunun ne ile bittiğini kontrol eder
#*doğru ise true
#*yanlış ise false döndürür.
# text="merhaba ben sive kanmaz"
# text=text.endswith("!")
# print(text)

#?startswith()

# text="merhaba ben sive kanmaz"
# text=text.startswith("m")    #?true
# print(text)

#!birden fazla methodu aynı anda kullanmak

# text= "     sive kanmaz           "
# text=text.strip().upper()
# print(text)

#?replace()
#*metnin içinde değiştirmek istediğimiz karakterlerin yerine
#*başka birşey yazmamıza yarar.

# text="selam ben neos yazılım"
# x=text.replace("selam","merhaba")
# print(x)

#!ödev
#*telefon numarasının başında 0 girildiğinde silmesini saplayan yapı?

