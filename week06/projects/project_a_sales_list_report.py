"""Week 6 project A: analyze a list of sales without external libraries."""

def read_sales():
    sales = []
    print("Enter one sale at a time. Press Enter to finish.")
    while True:
        text = input("Sale amount: ").strip()
        if text == "":
            return sales
        try:
            amount = float(text)
        except ValueError:
            print("Enter a number.")
            continue
        if amount < 0:
            print("Sale cannot be negative.")
            continue
        sales.append(amount)


def summarize(sales, target):
    total = 0.0
    above_target = []
    for sale in sales:
        total += sale
        if sale >= target:
            above_target.append(sale)
    return total, above_target


def print_report(sales, target):
    if not sales:
        print("No sales entered.")
        return
    total, above = summarize(sales, target)
    print("=" * 48)
    print("SALES LIST REPORT")
    print("=" * 48)
    for number, amount in enumerate(sales, start=1):
        print(f"Sale {number:2d}: {amount:9.2f} TRY")
    print("-" * 48)
    print(f"Number of sales: {len(sales)}")
    print(f"Total: {total:.2f} TRY")
    print(f"Average: {total / len(sales):.2f} TRY")
    print(f"Minimum: {min(sales):.2f} TRY")
    print(f"Maximum: {max(sales):.2f} TRY")
    print(f"Sales at or above {target:.2f}: {len(above)}")


def main():
    print("Sales List Report")
    target = float(input("Target sale amount: "))
    sales = read_sales()
    print_report(sales, target)


if __name__ == "__main__":
    assert summarize([100, 200, 300], 200) == (600, [200, 300])
    main()
