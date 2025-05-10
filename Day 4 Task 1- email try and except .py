count = 0

def mailvalidation(email):
    try:
        
        try:
            username, domain = email.split('@')
        except ValueError:
            raise ValueError("Email must contain exactly one '@' symbol.")

        if not username or not domain:
            raise ValueError("Username or domain part is missing.")

        
        try:
            d1, d2 = domain.split('.')
        except ValueError:
            raise ValueError("Domain must contain exactly one '.' (e.g., 'example.com').")

        if not d1 or not d2:
            raise ValueError("Domain part is not valid (e.g., 'example.com').")

        return True

    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception:
        print("Error: Unknown email validation error.")
        return False

while True:
    try:
        usermail = input("Enter your email address: ")
        if mailvalidation(usermail):
            print("Your email address is correct")
            break
        else:
            raise ValueError("Invalid email format.")
    except ValueError:
        count += 1
        if count == 3:
            print("You entered 3 incorrect email addresses!")
            break
        else:
            print("Please try again.\n")
