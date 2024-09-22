first_item,second_item,third_item="first","second","third"

items =[
    first_item,
    second_item,
    third_item
]
print(items)
print(items[0])

#list içine yeni bir öge ekleme

fourth_item='fourth'
items.append(fourth_item)
print(items)


#list içindeki ögenin içindeki bilgiyi değiştirmek
print(len(items))
items[len(items) -1]='sonuncu oge'
items[-1]='en en son'
print(items)

#list içinde belli bir yere öge eklemek
items.insert(0,'en basa eklenen oge')
items.insert(3,'yeni öge')

#en sona insert ile ekleme
items.insert(len(items),'sive')
print(items)

#list içindeki belli bir bölümü listelemek
print(items[2:5])
print(items[2:])

#listin ilk 3 ögesi
print(items[:3])
#listin son 3 ögesi
print(items[len(items) -3 :])

#listeyi terse çevir

print(items[::-1])
print(items) #değişmemiş eper değişmesini istersen eşitlemeyi unutma items=items[::-1]

#step belirleyerek bilgileri al 1,3,5
print(items)
step_items=items[::2]
print(step_items)


