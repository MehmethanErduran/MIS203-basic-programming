sales = [120.0, 95.5, 180.0, 75.0]

total = 0.0

print(len(sales))

for amount in sales:
    total += amount
    
print(f"Total: {total:.2f} TRY")

print(f"Average: {total / len(sales):.2f} TRY")