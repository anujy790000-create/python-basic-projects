text = input("Enter message: ")
shift = 3

result = ""

for ch in text:
    if ch.isalpha():
        result += chr(ord(ch) + shift)
    else:
        result += ch

print("Encrypted:", result)
