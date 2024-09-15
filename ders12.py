
#!TRY EXCEPT (TRY-CATCH)
#? hata ayıklama modeli

# try:
#     print(x)
# except:
#     print("Bu veriyi basamıyorum")

# try:
#     print(x)
# except NameError:
#     print("değişken bulunamadı hatası")
# except:
#     print("Birşeyler ters gitti")


#?else herhangi bir hata olmadığında devreye girer.try ile beraber çalışır
#?her zaman kullanmak zorunda değiliz
# try:
#     print("Selam!")
# except:
#     print("Hatalı işlem!")
# else:
#     print("hata yok devam et!") 

#*open ile bir .txt dosyası açmaya çalışınız
#*dosyanın dizinde var olup olmadığını kontrol ediniz.

# try:
#    dosya=open("test.txt","r")
# except:
#     print("böyle bir dosya yok")

#!txt belgesi veri okuma/yazma

#? w mod
# dosya=open("fatura.txt","w")
# dosya.write("Fatura toplam tutar :800tl")

#*örnek
# dosya=open("fatura.bat","w")
# for i in range(20):
#     dosya.write("start\n")

#? a mod
# dosya=open("test.txt","a")
# dosya.write("Selam Naber\n")

# dosya=open("test.py","a")

# dosya=open("test.html","a")

#!matematiksel işlemler 
#?min() ,max()

# degeribul=max(2,5,78,2,6,88,85,32,26)
# print(degeribul)

# degeribul=min(2,5,78,2,6,88,85,32,26)
# print(degeribul)


#* kullanıcıdan kaç adet değer gireceğini sorunuz
#* mesela 3 değeri girilirse 3 kere lütfen sayı belirleyiniz deyiniz
#* belirlenen her sayıyı bir array içerisinde toplayınız
#* min ve max kullanarak dizi içerisine alınan değerlerin en büyüğünü bulunuz

# girilendegerkat=int(input("Kaç adet değer gireceksiniz? : "))

# test=[]
# for i in range(girilendegerkat):
#     girilendeger=int(input("Lütfen değer giriniz : "))
#     test.append(girilendeger)

# enBuyuk=max(test)
# print(f"En büyük değer={enBuyuk}")

#? abs()
#*negatifi pozitife çevirir.

# sayi=abs(-20)
# print(sayi)

#? pow()
# sayi=pow(2,3)
# print(sayi)

#*örnek
# deger1=int(input("alt değer giriniz : "))
# deger2=int(input("Üst değer giriniz : "))
# sayi=pow(deger1,deger2)
# print(sayi)

#!math modulü
#?math kullanmak için math modulünü import etmemiz gerekir.

import math

#? math.sqrt()

# karekok=math.sqrt(16)
# print(karekok)

#? math.ceil()
#*yukarıya yuvarlama
# sayi=math.ceil(2.4)
# print(sayi)

#? math.floor()
#*aşağı yuvarlama

# sayi=math.floor(2.6)
# print(sayi)

#!fonksiyonlar

# def yazdir():
#     print("Selam ben sive")

# yazdir()

# def carpma(say1,say2,say3):
#     sonuc=say1*say2*say3
#     return sonuc

# print(carpma(2,2,2))

#*ortalama alan bir fonksiyon yazınız
# def sorgula(sin1,sin2):
#     sonuc=(sin1+sin2)/2
#     return sonuc

# print(sorgula(50,75))

#*kullanıcııdan alınan 3 sınavın ortalamasınıalan fonk.  yazın

# def hesapla():
#     sin1=int(input("1.sınavı giriniz : "))
#     sin2=int(input("2.sınavı giriniz : "))
#     sin3=int(input("3.sınavı giriniz : "))
#     sonuc=(sin1+sin2+sin3)/3
#     print(f"{sonuc}")
# hesapla()


#?fonksiyonlar arasında değerler gönderme

#*bir  adet çarpma fon oluşturunuz.
#* bir adet çıkarma fonk. oluştur
#* bu iki fonksiyon arasında haberleşmeyi sağlayın.

# def carpma(say1,say2):
#     carpim=say1*say2
#     return carpim
# def cikarma():
#     x1=carpma(2,2)
#     x2=carpma(3,3)
#     cikarma=x1-x2
#     return cikarma

# print(cikarma())

#! class yapısı (nesne tabanlı programlama)
# class ClassOlustur:
#     x=5
# print(ClassOlustur)

#*classı ayakta tutan nesnelerdir
# class ClassOlustur:
#     x=5
# test=ClassOlustur()
# print(test.x)

#*nesneyi tek başına oluşturmak mantıklı işlemler değildir
#*init ile nesneler oluşturulur

# class Kullanici:
#     def __init__(self,ad,soyad):
#         self.ad=ad
#         self.soyad=soyad

# elemanYaz=Kullanici("sive","kanmaz")
# print(elemanYaz.ad)

#?örnek
# class Kisi:
#     def __init__(self,isim,yas):
#         self.isim=isim
#         self.yas=yas
#     def yazdir(self):
#         print("Selam benim adım : ",self.isim, "benim yaşım " ,self.yas)
# k1=Kisi("sive",32)
# k1.yazdir()

