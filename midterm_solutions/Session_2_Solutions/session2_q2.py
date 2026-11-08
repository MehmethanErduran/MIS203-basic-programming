"""Session 2, Question 2."""

days = int(input("Number of days: "))
while days <= 0:
    print("Enter a positive number of days.")
    days = int(input("Number of days: "))
total = 0.0
target_days = 0
for day in range(1, days + 1):
    value = float(input(f"Day {day}: "))
    while value < 0:
        print("Enter zero or more for this day.")
        value = float(input(f"Day {day}: "))
    total += value
    if value >= 80:
        target_days += 1
average = total / days
print(f"Total: {total:.2f} km")
print(f"Average: {average:.2f} km")
print(f"Days Meeting Target: {target_days}")
