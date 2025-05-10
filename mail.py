import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def get_user_info():
    while True:
        name = input("Enter your name: ").strip()
        if name and not name.isdigit():
            break
        print("Invalid input. Please enter a valid name (not empty or numbers).")

    while True:
        email = input("Enter your email: ").strip()
        if is_valid_email(email):
            break
        print("Invalid email format. Please try again.")

    return name, email
