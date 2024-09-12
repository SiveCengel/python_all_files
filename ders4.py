
#*telefon numarasının başında 0 girildiğinde silmesini saplayan yapı?
# girilenTelefon=input("Bir telefon numarası giriniz :")
# girilenTelefonKont=girilenTelefon.startswith("0")
# if girilenTelefonKont==True:
#     girilenTelefon=girilenTelefon.replace("0","",1) #?değiştirilecek eleman,yerine ne yazılacağı,kaç adet 0 silinecek
#     print(girilenTelefon)

# else:
#         print(girilenTelefon)

#?isnumeric()

# text="495940302"
# text=text.isnumeric()
# print(text)

#*örnek
#*girilen telefon numarasında harf bulunmaması gerekmekte

# tel =input("Lütfen telefon numaranızı giriniz :")
# tel=tel.isnumeric()

# if tel==True:
#     print("Teşekkürler")
# else:
#     print("Hatalı Giriş Yapıldı!")


#?find() (metinsel ifadenin sıra numarasını verir.)
#*index ile arasındaki fark:
#*index eğer arama yapıp bulamazsa program duruyor ve hata veriyor.
#*fakat find fonk. değer bulamazsa -1 veriyor.

# text="selam ben sive"
# text=text.find("e")
# print(text)

#!listeleri toplama
# list1=["a","b","c","d","e","f"]
# list2=[1,2,3,4,5,34,3456,677]
# sonliste=list1+list2
# print(sonliste)

#!Liste metotları

#?append() (listeye eleman gönderme)

# renkler=["kırmızı","mavi","turuncu","yeşil"]
# renkler.append("sarı")
# print(renkler)

#*hazır bir araba listesi içerisine kullanıcıdan alınan en sevdiği arabayı ekleyiniz
# arabalar=["bmw","mercd","wv","porche"]
# sevilenArac=input("en sevdiğiniz araç nedir? :")
# arabalar.append(sevilenArac)
# print(arabalar)

#* var olan bir diziye kullanıcıdan alınan farklı diziyi ekleyiniz.
#?split()
# yazilimDilleri=["html","css","js","react","py","django"]
# alinanYazilimDili=input("En sevdiğiniz Yazılım Dilleri : ")
# alinanYazilimDili=alinanYazilimDili.split()
# yazilimDilleri.append(alinanYazilimDili)
# print(yazilimDilleri)

#*örnek
# test=input("Test içeriği giriniz(virgüllerle ayırınız) : ")
# degertest=test.split(",")
# print(degertest)

#?insert() (diziye eklenen elemanın nereye ekleneceği belirtilebilir)

# mylist=["html","css","js","py"]
# mylist.insert(0,"react")
# print(mylist)

#*var olan bir 5 elamanlı diziye manuel olarak 4.indexine bir veri ekleyerek ekrana yazdırın.

# liste=["a","b","c","d","e"]
# liste.insert(4,"ş")
# print(liste)

#?remove() (listedeki elemanı siler)
# mylist=["a","b","c","d","e","f"]
# mylist.remove("a")  #*listeden seçilen eleman remove komutu içerisinde belirtilmeli
# print(mylist)

#?count() (liste içerisinde kaç tane aynı eleman olduğunu verir)
# mylist=["a","b","c","a","d","e","f","a"]
# x=mylist.count("a")
# print(x)

#?reverse() (listeyi tersine çevirir)
# mylist=["a","b","c","d","e","f"]
# mylist.reverse()
# print(mylist)

#?extend() (bir dizideki bütün elemanları başka bir diziye gönderir)
# front=["html","css","js"]
# back=["django","c#","php"]
# front.extend(back)
# print(front)

#*örn:dizi içerisinde hem int hem string ifadeler bulunabilir
# sayilar=[1,2,3,4,5,6]
# harfler=["a","b","c","d","e"]
# sayilar.extend(harfler)
# print(sayilar)

#?clear()  (diziyi sıfırlar(bütün elemanları siler))
# mylist=["a","b","c","d","e","f"]
# mylist.clear()
# print(mylist)

#?pop() (içerisinde değer olmadığında dizideki son elemanı siler)
# mylist=["a","b","c","d","e","f"]
# mylist.pop()
# print(mylist)

#*pop metodu içine değer girildiğinde o liste içindeki index numaralı elemanı siler
# mylist=["a","b","c","d","e","f"]
# mylist.pop(1)
# print(mylist)

#?sort() (dizinin içindeki elemanları sıralar)
# mylist=[45,23,77,12,85,23,1,67,88,32,12,11]
# mylist.sort()
# print(mylist)

#*örn:
# mylist=["bmw","audi","merc","wv","ford"]
# mylist.sort()
# print(mylist)

#!ödev
#*boş list1 içerisine 4 meyve tanımla ve 3. indextekini patates ile değiştir
#*list2 3 yazılım dili girilsin sonuna "python " ekle ve 2. indexteki listeden çıkar.
