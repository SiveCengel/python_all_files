#fonksiyonlar def ile tanımlanır
#fonksiyonlar bir veya birden daha fazla değer/parametre alabilir veya almayabilir
#fonksiyonlara gönderilen parametreler default değer içerebilir
#fonksiyonlar bir tip veri dönebilir
#fonksiyonlar tekrar kendilerini çağırabilirler
#fonksiyonlara gönderilen bilgilerin sayısı belli olmadan da kullanılabilir

def hello():
    print("Merhaba")

hello() #çalıştırmış olduk

name="Derya"

def greetings():
    #global değişken kullanabiliriz ama çoooook riskli
    print(f"Merhaba {name}")

greetings()