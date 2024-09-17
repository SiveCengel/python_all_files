
#kullanıcı ad bilgisini bildirene kadar devam et..ve en az 5 karakter olsun

user=""

# while len(user)<=5:
#     user=input("Kullanıcı adını giriniz : ")
#     print(user)


#kullanıcı ad ve soy ad bilgisini bildirene kadar sormaya devam et

# first_name,last_name="",""
# while len(first_name)<5 and len(last_name)<5:
#     print("Lütfen kullanıcı adı 5 karakter veya daha fazlası olsun")
#     first_name=input("Adınız :")
#     last_name=input("Soyadınız : ")

#kullanıcı ad veya soyad bilgisini bildirene kadar sormaya devam et
first_name,last_name="",""
while len(first_name)<5 or len(last_name)<5:
    print("Lütfen kullanıcı adı 5 karakter veya daha fazlası olsun")
    first_name=input("Adınız :")
    last_name=input("Soyadınız : ")
