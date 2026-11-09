sales = [120, 500, 75, 820, 300]

large_sales = []

for sale in sales:
    if sale >= 500:
        large_sales.append(sale)
        
print("Large sales:", large_sales)

