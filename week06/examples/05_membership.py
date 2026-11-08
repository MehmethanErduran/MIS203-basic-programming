approved_codes = ("P-101", "P-102", "P-103")

code = input("Product code: ").strip().upper()

if code in approved_codes:
    print("Known product")
else:
    print("Unknown product")
