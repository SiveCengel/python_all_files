items=[
    "cable",
    "keyboard",
    "pc"
]

digital_products=["laptop","monitor","mouse"]
other_products=["lorem","ipsum","dolor"]

# new_items=items.copy()  #?1yöntem
new_items=[*items]        #?2yöntem
new_items[0]="mic"

print("items",items)
print("new_items",new_items)

#?bu şekilde liste içine yeni bir liste eklemiş oluruz
# items.append(digital_products)
# print(items)

#?eğer liste içine yeni liste ÖĞELERİNİ eklemek istersek o zaman 
#?bu yöntem daha doğru

# items.extend(digital_products)
# print(items)

#? ya da 

items += digital_products
print(items)

#? birden fazla liste ögesi,belki başka ögeler ekleme

# items=items+digital_products+other_products
items=[
    *items,
    *digital_products,
    *other_products,
    1,
    2,
    3
]

print(items)