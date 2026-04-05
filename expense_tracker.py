expenses = []

while True:
    print("\n1.Add Expense 2.View Expenses 3.Total 4.Exit")
    choice = input("Choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        expenses.append(amount)

    elif choice == "2":
        print("Expenses:", expenses)

    elif choice == "3":
        print("Total Expense:", sum(expenses))

    elif choice == "4":
        break
