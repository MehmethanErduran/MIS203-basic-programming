"""Week 3 model answer: order validation and an inclusive member threshold."""


def decide_order(amount, stock, quantity, is_member):
    if amount <= 0 or stock < 0 or quantity <= 0:
        return False, "Invalid amount, stock or quantity.", None
    elif quantity > stock:
        return False, "Not enough stock.", None
    elif is_member and amount >= 500:
        return True, "Approved with a 10% member discount.", amount * 0.90
    else:
        return True, "Approved at the regular price.", amount


def main():
    amount = float(input("Order amount (TRY): "))
    stock = int(input("Available stock: "))
    quantity = int(input("Requested quantity: "))
    member_answer = input("Is the customer a member? (yes/no): ").strip().lower()
    is_member = member_answer in ("yes", "y")

    approved, reason, final_price = decide_order(amount, stock, quantity, is_member)
    print(reason)
    if approved:
        print(f"Final price: {final_price:.2f} TRY")


if __name__ == "__main__":
    main()
