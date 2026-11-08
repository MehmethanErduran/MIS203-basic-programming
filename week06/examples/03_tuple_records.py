product = ("P-101", "Notebook", 75.0)

code, name, price = product

print(f"{code}: {name}, {price:.2f} TRY")
# A tuple is useful for a small record we do not plan to change.


# Paketleme (Packing)
ogrenci = ("Ali", 22, "MIS")

# Açma (Unpacking)
isim, yas, bolum = ogrenci

print(f"İsim: {isim}, Yaş: {yas}, Bölüm: {bolum}")

my_savings = (1000, 500, 310, 4000, 5000, 670, 888)

sorted_savings = sorted(my_savings)
print(sorted_savings)

max_saving = max(my_savings)
print(max_saving)

min_saving = min(my_savings)
print(min_saving)

print(my_savings.count(500))
print(my_savings.index(4000))


new_my_savings = my_savings.sort()  # This will raise an AttributeError because tuples do not have a sort method.
