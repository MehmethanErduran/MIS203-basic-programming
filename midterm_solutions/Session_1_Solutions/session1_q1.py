"""Session 1, Question 1."""

quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: "))
subtotal = quantity * unit_price
if quantity >= 100:
    discount = subtotal * 0.10
else:
    discount = 0.0
fee = 12.0
total = subtotal - discount + fee

print(f"Subtotal: {subtotal:.2f} TRY")
print(f"Discount: {discount:.2f} TRY")
print(f"Service Fee: {fee:.2f} TRY")
print(f"Total: {total:.2f} TRY")
