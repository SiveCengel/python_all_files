# print("selam")
# print("merhaba","dünya","selam")
# print("selam        "+"ben sive")

# print("""merhaba ben
#         sive

#         """)

# print("selam benim adım{ad}".format(ad="sive"))

# print("selam ben {ad} , soyadım {soyad} , ve ben {yas} yaşındayım.".format(ad="sive",soyad="kanmaz",yas="32"))

# marka="bmw" 
# print("benim arabamın markası{}".format(marka))

# isim="sive"
# soyisim="knmz"
# print("selam ben {1} soyadım {0}".format(isim,soyisim)

# print("{2} {3} {0} {1}".format("ben","python","öğrenmek","istiyorum") )

# benimAdım="sive"
# print(benimAdım)

# benim_adım="murat"
# print(benim_adım)

#int
# sayi=20
# print(sayi)

#?string
# isim="sive"
# print(isim)

# sayi =20
# sayi2 =10 + sayi
# print(sayi2)

# sayi=10
# sayi =sayi+1
# print(sayi)

# sayi=30
# sayi=sayi - 20
# print(sayi)

# sayi=10
# sayi +=10 #?sayi = sayi +10

# sayi=10
# sayi-=20
# print(sayi)

#!çoklu değişken oluşturma
# x,y,z=10,20,30
# print(x,y,z)

# sinav1,sinav2,sinav3=50,55,75
# ortalama=(sinav1+sinav2+sinav3) /3
# print(ortalama)

#?birden fazla değişkene aynı değer verilebilir

# a=b=c=d="kırmızı"
# print(a)

# a=b=c=d=25
# print(a,b,c,d)

# sayi1 = str(30)
# isim2="sive"
# print(isim2 + sayi1)

#!değşşkenlerde type çeşitleri

#?int() (tam sayı)
# sayi = 20
# print(type(sayi))

#?string (metinsel ifade)
# isim="sive"
# print(isim)

# isim="sive"
# soyisim="knmz"
# print(isim- soyisim) #!hata

#?float (ondalık)
# sayi=2.45
# print(sayi)

#? tuple
# renkler="sarı","turuncu","kahve","siyah"
# print(renkler[1])

#?list (array)
# mylist =[1,2,3,"a","b","c"]
# print(mylist)

# mylist =[1,2,3,"a","b","c"]
# elemanCagir = mylist[2]
# print(elemanCagir)

#? set
# degerler = {"renk","araba",34,56}
# print(degerler)

#?dict (obje)
# calisanlar = {
#     "isim":"sive",
#     "soyisim":"knmz",
#     "yas":32
# }
# print(calisanlar)

# arabaozellik={
#     "marka":"bmw",
#     "model":"m5",
#     "yılı":2021,
#     "km":30000
# }
# print(arabaozellik["marka"])

#?dict ve list yapısının iç içe kullanımı

# calisanlar=[
#     {
#         "isim":"sive",
#         "soyisim":"cengel",
#         "yas":31
#     },
#     {
#         "isim":"murat",
#         "soyisim":"cengel",
#         "yas":29
#     },
#     {
#         "isim":"imge",
#         "soyisim":"nas",
#         "yas":39
#     }
# ]
# print(calisanlar[1]["isim"])

#!operatörler
#?toplama
# sayi =20
# sayi2 =40
# toplam= sayi +sayi2
# print(toplam)

# sayi=40
# sayi2=10
# sayi=10+sayi2
# print(sayi)

#? +=
# sayi=20
# sayi +=10
# print(sayi)

#?çıkartma
# sayi=20
# sayi2=40
# print(sayi-sayi2)

# sayi=50
# sayi= sayi-40
# print(sayi)

# sayi=40
# sayi-=10
# print(sayi)

# isim="sive"
# soyisim="cengel"
# print(isim-soyisim) #! str den str çıkartılmaz

#? çarpma 
# sayi=20
# sayi*=2  #?sayi=sayi*2
# print(sayi)

#?bölme
# sayi=10
# sayi /=2
# print(sayi)

#? mod almak
# print(10%2)

#! değişkenlerin tipini değiştirme

# sayi= int("23")
# sayi2=int("40")
# toplam=sayi +sayi2
# print(toplam)

# toplamTutar =53.44
# print(toplamTutar) #?ondalık

# toplamTutar = int(53.44)
# print(toplamTutar)


#?str()
# sayi =str(34)
# sayi2 =str(45)
# print(sayi+sayi2)

#! Len() --lenght uzunluk-
# myList=[1,2,3,4,5,6,7,8,9,0]
# print(len(myList))

# myList=[1,2,3,4,5,6,7,8,9,0]
# listeUzunlugu =len(myList)
# print(listeUzunlugu)

# mesaj ="selam ben şive.neos akademide öğrenciyim."
# mesajUzunluk=len(mesaj)
# print(mesajUzunluk)

# person = {
#     "ad":"sive",
#     "soyad":"cengel"
# }
# print(len(person))

# person= [
#     {
#        "ad":"sive",
#        "soyad":"cengel"  
#     },
#     {
#        "ad":"sive",
#        "soyad":"cengel"  
#     },
#     {
#        "ad":"sive",
#        "soyad":"cengel"  
#     }
# ]
# print(Len[person])

#!eval()
# x ="print(25)"
# eval(x)

# y="print(len('sivecengel'))"
# eval(y)

z = eval("max(1,2,3,4,5,6)")

