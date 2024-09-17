
#?aralık belirterek for döngüsünü çalıştırmak ->range

# for item in range(1,10):
#     print(item)

# for item in range(1,101):
#     if item %5==0:
#         print(item)



#?liste içindeki verileri tek tek işlemek
# users=["Aysen","Fatma","Cigdem","Hasan","Ahmet","Mehmet"]

# for user in users:
#     print(user)



#?item ve index bilgisi ile listeleri döngüde kullanmak ->enumerate

# for obj in enumerate(users):
#     print(users[obj[0]])

#!list unpacking 
#151. video

# user_info=["admin","1234dfvsxdcfv"]
# user,password=user_info

# user_detail=["admin","1234432222345","admin@admin.com","mail-master@admin.com"]

# user_name,user_password,*mail_list=user_detail
# print(user_name,user_password,mail_list)

products=[
    ["laptop","mouse","keyboard"],
    ["monitor","printer"],
    "Sony XYZ",
    "Beats Fit Pro",
    "Apple Magic Keyboard",
    "Logitech MX Master 3",
    12,
    33,
    34,
]

for item in products:
    if type(item) == list:
        for pr in item:
            print(pr)
    elif type(item)==str:
        print(item)
