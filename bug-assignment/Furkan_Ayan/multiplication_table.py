number = int(input("Enter a number: "))
i = 1
while i < 12:
    # BUG FIX 1: 'num' değişkeni 'number' olarak değiştirildi.
    print(f"{number} x {i} = {number * i}")

    # BUG FIX 2: Boşluk/girinti hatası (indentation) düzeltildi.
    i = i + 1
print("Done!")
