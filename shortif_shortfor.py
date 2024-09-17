
#short if kullanımı
# is_active=True
# is_active=False

# if is_active:
#     user_info="active"
# else:
#     user_info="deactive"

#!short hali
# user_info="active" if is_active else "deactive"
# print(user_info)

#for kullanımı

user_index=[]

# for item in range(1,10):
#     user_index.append(item)

# print(user_index)

#!short hali

user_index_v1= [item for item in range(1,10)]
user_index_v2= [item * 10 for item in range(1,10)]
user_index_v3= [item for item in range(1,10) if item % 2 !=0]
print(user_index_v3)