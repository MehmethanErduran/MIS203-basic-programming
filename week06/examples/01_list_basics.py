products = ["Notebook", "Pen", "Folder"]
print(products[0])

products.append("Marker")
products[1] = "Blue pen"

print(products)
print("Count:", len(products))

alisveris_listesi = ["Elma", "Armut", "Muz", "Portakal"]

print(alisveris_listesi[0])
print(alisveris_listesi[2])

alisveris_listesi.append("Çilek")

print(alisveris_listesi)

alisveris_listesi.insert(2, "Kivi")

print(alisveris_listesi)

alisveris_listesi.remove("Elma")
print(alisveris_listesi)

silinen = alisveris_listesi.remove("Armut")
print("Silinen eleman:", silinen)
print(alisveris_listesi)

alisveris_listesi.pop(1)
print(alisveris_listesi)

silinen = alisveris_listesi.pop(1)
print("Silinen eleman:", silinen)
print(alisveris_listesi)

# Özellik	                                     pop()	                                                        remove()
# Neye Göre Siler?	                İndeks (Sıra) numarasına göre siler.	                    Değerin (Elemanın) kendisine göre siler.
# Varsayılan Davranış	            İndeks yazmazsanız en sondaki elemanı siler.	            Değer yazmak zorunludur, boş bırakılamaz.
# Elemanı Geri Döndürür mü?	        Evet. Sildiği elemanı koparıp size verir.               	Hayır. Elemanı tamamen yok eder, geriye bir şey dönmez.
# Eleman Bulunamazsa?	            Olmayan bir indeks girilirse IndexError verir.	            Olmayan bir değer girilirse ValueError verir.

sayilar = [5, 2, 9, 1, 7, 3, 8, 4, 6]

sayilar.sort()
print(sayilar)

yeni_sayilar = sorted(sayilar)
print(yeni_sayilar)

sayilar.sort(reverse=True)
print(sayilar)

sayilar.reverse()
print(sayilar)

print(sayilar.count(5))

# sayilar.clear()
# print(sayilar)

sayilar2 = [1, 2, 3]
sayilar2.extend([4, 5, 6])
print(sayilar2)

sayilar.append(sayilar2)
print(sayilar)  

sayilar.extend(sayilar2)
print(sayilar)

notlar = [
          [50, 60],
          [55, 65]
          ]

notlar_names = ["Ali", "Veli"]

print(notlar_names[0])
print(notlar[0][0])