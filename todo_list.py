tasks = []

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Delete Task")
    print("4.Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == '3':
        num = int(input("Task number to delete: "))
        tasks.pop(num-1)

    elif choice == '4':
        break
