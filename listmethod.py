# items=[
#     "html",
#     "html",
#     "html",
#     "python",
#     "python",
#     "django",
#     "css",
#     "css",
#     "css",
#     "bootstrap",
# ]

#?liste içinde kaç öge var -> len
# print(len(items))

#?liste içinde bir öge var mı -> in

# print("python" in items)
# item=input("Bu eğitimde hangi yazılım dili var mı diye sor : ")
# if item in items:
#     print(f"{item} bilgi var")
# else:
#     print("yok")

#?liste içinde bir öge kaç kez var -> count
# print("Kaç adet python var",items.count("python"))


#?liste iindeki ögenin yeri(index) nedir? ->index

# print("python index : ",items.index("python"))

#?liste içindeki öge adlarını sil ->remove

# items.remove("python")
# print(items)

#?liste içindeki son ögeyi çıkar ->pop
# last_item=items.pop()
# print(items)
# print(last_item)

#?liste içindeki x indexli ögeyi çıkar -> pop

# first_item =items.pop(0)
# print(items)
# print(first_item)

#?listeyi boşalt -> clear

# items.clear()
# print(items)

#?liste içindeki ögeleri topla  ->sum

# numbers=[
#     1,
#     2,
#     3,
#     4,
#     5,
#     6
# ]
# print(sum(numbers))

#?liste içindeki en küçük fiyat

# print(min(numbers))

#?liste içindeki en büyük fiyat

# print(max(numbers))

#!iç içe list

#örn:
# users=[]
# user_1=["Ayse",1234]
# user_2=["Ali",9876]

# users.append(user_1)
# users.append(user_2)

# print(users)

#?liste içindeki list e erişmek

# products=[
#     ["laptop","mouse","keyboard"],
#     ["monitor","printer"],
#     "headphone",
# ]

# print(products)

# print(products[2])

#?lis içindeki listi silmek

# first_user=users.pop()

# print(first_user)
# print(users)

