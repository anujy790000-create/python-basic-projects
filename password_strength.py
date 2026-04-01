password = input("Enter password: ")

length = len(password) >= 8
digit = any(c.isdigit() for c in password)
upper = any(c.isupper() for c in password)

if length and digit and upper:
    print("Strong Password")
else:
    print("Weak Password")
