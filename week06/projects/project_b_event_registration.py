"""Week 6 project B: use tuples and sets in an event registration desk."""

def normalize_email(email):
    return email.strip().lower()


def register(registrations, email_set, name, email, session):
    email = normalize_email(email)
    if not name.strip() or "@" not in email:
        return False, "Name and valid-looking email are required."
    if email in email_set:
        return False, "This email is already registered."
    if session not in {"Python", "Data", "GitHub"}:
        return False, "Choose Python, Data, or GitHub."
    record = (name.strip(), email, session)
    registrations.append(record)
    email_set.add(email)
    return True, "Registration saved."


def print_report(registrations):
    print("=" * 55)
    print(f"REGISTERED PARTICIPANTS: {len(registrations)}")
    print("=" * 55)
    python_count = 0
    data_count = 0
    github_count = 0
    for number, (name, email, session) in enumerate(registrations, 1):
        print(f"{number:2d}. {name:20} {session:8} {email}")
        if session == "Python":
            python_count += 1
        elif session == "Data":
            data_count += 1
        else:
            github_count += 1
    print("-" * 55)
    print(f"Python: {python_count}")
    print(f"Data: {data_count}")
    print(f"GitHub: {github_count}")


def main():
    registrations = []
    email_set = set()
    print("Event Registration Desk")
    while True:
        command = input("Register, report, or quit? ").strip().lower()
        if command == "quit":
            break
        if command == "report":
            print_report(registrations)
            continue
        if command != "register":
            print("Unknown command.")
            continue
        name = input("Name: ")
        email = input("Email: ")
        session = input("Session (Python/Data/GitHub): ").strip().title()
        _, message = register(registrations, email_set, name, email, session)
        print(message)
    print_report(registrations)


if __name__ == "__main__":
    main()
