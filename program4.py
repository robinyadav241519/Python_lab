# Interactive Command-Line Task Scheduler

tasks = []

while True:
    print("\n--- Task Scheduler ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Check Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        priority = input("Enter priority (high/low): ")
        done = input("Is the task completed? (yes/no): ")

        tasks.append([task, priority, done])
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(i, ".", task[0], "-", task[1], "-", task[2])

    elif choice == "3":
        print("\nTasks ready to execute:")

        for task in tasks:
            name = task[0]
            priority = task[1]
            done = task[2]

            # Boolean logic and short-circuit evaluation
            if (priority == "high" and done == "no") or not done == "yes":
                print("Execute:", name)
            else:
                print("Skip:", name)

    elif choice == "4":
        print("Exiting Task Scheduler...")
        break

    else:
        print("Invalid choice! Please try again.")