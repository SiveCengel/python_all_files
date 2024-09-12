
#!ödev
#*boş list1 içerisine 4 meyve tanımla ve 3. indextekini patates ile değiştir
# list1=[]
# list1.append("elma")
# list1.append("armut")
# list1.append("kivi")
# list1.append("karpuz")  #?boş listeye atama yaptık
# list1.pop(3)            #?3.indexi sildik
# list1.insert(3,"patates") #?3. indexe patates attık
# print(list1)

#*list2 3 yazılım dili girilsin sonuna "python " ekle ve 2. indexteki listeden çıkar.

# diller=["js","php","django"]
# diller.append("python")
# diller.pop(2)
# print(diller)

#! IF ELSE (KARŞILAŞTIRMA OPERATÖRLERİ)
#? == (eşittir)
#? > (büyüktür)
#? < (küçüktür)
#? >= (büyük eşit)
#? <= (küçük eşit)
#? != (eşit değil)

#?py kullanım
# if koşul:
#     print(test)
# else:
#     print("test else")  
  
# yas=23
# if yas<30:
#     print("test")
# else:
#     print("test else")

#*yaşın 18 den büyük olduğunda "reşitsiniz yazan program" değilse "reşit değilsiniz"

# yas=18
# if yas>=18:
#     print("Reşitsiniz")
# else:
#     print("Reşit değilsiniz")

#*kullanıcı yaşını ve adını alınız
#*18 yaşından büyükse"mehmet 23 yaşındasın reşitsin
#*18 den küçükse "mehmet 18 yaşındasın reşit değilsin"

# isim=input("Adınızı Giriniz :")
# yas=int(input("Yaşınızı Giriniz :"))

# if yas>=18:
#     print(f"{isim},{yas} yaşındasın ve reşitsin")
# else:
#     print(f"{isim},{yas} yaşındasın ve reşit değilsin")

#*kullanıcıdan alınan 2 sayısının eşit olup olmadığı kontrol edilsin

# sayi1=int(input("1. sayıyı giriniz :"))
# sayi2=int(input("2. sayiyi giriniz :"))
# if sayi1==sayi2:
#     print("sayılar eşit")
# else:
#     print("sayilar eşit değil")

#*ortalamasını giren öğrencinin geçip geçmediği kontrol ediilsin

# sinav1=int(input("1.sınavı giriniz :"))
# sinav2=int(input("2. sinav giriniz :"))
# ortalama= (sinav1+sinav2)/2
# if ortalama>=50:
#     print("geçtiniz!")
# else:
#     print("Kaldınız")

#*girilen iki sayının hangisinin büyük olduğnu bulunuz

# sayi1=int(input("bir sayı giriniz :"))
# sayi2=int(input("ikinci bir sayı daha :"))
# if sayi1>sayi2:
#     print(f"{sayi1},{sayi2} den büyüktür.")
# else:
#     print(f"{sayi1},{sayi2} den küçüktür.")

#*girilen sayının tek mi çift mi oldğ. bul

# sayi=int(input("1 sayı giriniz:"))
# sonuc=sayi%2
# if sonuc==0:
#     print("sayı çifttir.")
# else:
#     print("sayi tektir")

#*kullanıcıdan yaptığı alışveriş fiyatını alınız.
#*alışveriş fiyatı 100 lira altındaysa 15 tl kargo icreti fiyata dahil edilsin
#*100 lira üstündeyse kargo ücreti alınmasın

# tutar=int(input("Alışveriş tutarınızı giriniz:"))
# total=tutar+15
# if tutar>=100:
#     print(f"kargo ücretsiz!")
# else:
#     print(f"kargo dahil tutarınız,{total}")

#*kullanıcı girdiği vize ve final  notlarının ortalamasını alın
#*vize=40% final=60%
#*vize ve final ortalaması sonucu kalan öğrencilerden büt noyu istensin
#*büt notu sonucu yeniden ortalama alıp geçti kaldı mesajı verilsin
#* vize=40% büt=60%

# vize=int(input("vize notunuzu giriniz :"))
# final=int(input("final notunuzu giriniz :"))
# ortalama=(vize*0.4)+(final*0.6)
# if ortalama>=50:
#     print("tebrikler. geçtiniz! ortalamanız",ortalama)
# else:
#     print("maalesef kaldınız! ortalamanız :",ortalama)
#     but=int(input("bütünleme notunuzu giriniz :"))
#     ortalama=(vize*0.4)+(but*0.6)
#     if ortalama>=50:
#         print(f"büt ile geçtiniz! : {ortalama}")
#     else:
#         print("kaldınız")

#!elif() 
#*else if ()anlamına gelmektedir.
#*birden fazla şartım var ise elif şartını kullanabilirsiniz.

"""
if şart:
    işlenecek kodlar
elif şart:
    işlenecek kodlar
elif şart:
    işlenecek kodlar
elif şart:
    işlenecek kodlar
else:
    işlenecek kodlar
"""

# #*örnek
# renk="djdje"
# if renk=="mavi":
#     print("girilen renk mavi")
# elif renk=="yeşil":
#     print("girilen renk yeşil")
# elif renk=="kırmızı":
#     print(f"girilen renk {renk}")
# else:
#     print("yanlış bir tuşlama yaptınız")




#!ödevler
#*girilen iki sayının hangisinin büyük olduğunu bulunuz
#*girilen sayının kaç basamaklı olduğunu bulun
#*100lük sistemde girilen notu 5lik sisteme çevirin(87=>5)
#*alınan iki sayının girilen harfe göre dört işlem yapan uygulamayı yazınız.
#*örn: toplama=t 

#*kullanıcıya sinema yada tiyatro tercihi sorulsun 
#*sinema izlemek için 50tl
#*tiyatro için 100tl ödemesi gerekmektedir.
#*öğrencilere %50 indirim yapıldığı düşünülerek
#*öğrenci ise indirim yapılsın
#*öğrenci değilse indirimsiz tutatı hesaplayarak ekrana yazdıran kodu yazınız