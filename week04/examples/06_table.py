price = float(input("Unit price: "))

for quantity in range(1, 6):
    print(f"{quantity} units: {quantity * price:.2f} TRY")


