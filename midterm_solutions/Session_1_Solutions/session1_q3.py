"""Session 1, Question 3."""

def calculate_charge(quantity, unit_price):
    return quantity * unit_price


remaining = 18
unit_price = 40.0
approved_requests = 0
total_charges = 0.0

for request in range(1, 5):
    quantity = int(input(f"Request {request} quantity: "))
    if quantity <= 0 or quantity > remaining:
        print("Rejected")
    else:
        charge = calculate_charge(quantity, unit_price)
        remaining -= quantity
        approved_requests += 1
        total_charges += charge
        print(f"Approved: {charge:.2f} TRY")
        
print(f"Remaining Stock: {remaining}")
print(f"Approved Requests: {approved_requests}")
print(f"Total Charges: {total_charges:.2f} TRY")
