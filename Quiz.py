score = 0

questions = {
    "Capital of India? ": "delhi",
    "2 + 2 = ? ": "4",
    "Python is a language? (yes/no) ": "yes"
}

for q, ans in questions.items():
    user = input(q).lower()
    if user == ans:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("Score:", score)
