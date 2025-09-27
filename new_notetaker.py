tasks = []

while True:
  
    print("\n--- To-Do List Menu ---")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
      if not tasks:
        print("Your to-do list is empty!")
      else:
        print("\nYour tasks:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i])
            
    elif choice == "2":
        task = input("Enter the task to add: ")
        if task:
           tasks.append(task)
           print("Task '" + task + "' added!")
        else:
           print("Task cannot be empty.")

    #advanced
    elif choice == "3":
      choice = input("Enter the name or number you want to remove: ")
      
      if choice.isdigit():
        #since index starts from 0
        index = int(choice) - 1
        if index >= 0 and index < len(tasks):
            removed_task = tasks.pop(index)
            print("Task '" + removed_task + "' removed!")
        else:
            print("Invalid task number.")
            
      else:
        if choice in tasks:
            tasks.remove(choice)
            print("Task '" + choice + "' removed!")
        else:
            print("Task not found.")
          
    elif choice == "4":
        print("Exiting To-Do List App. Goodbye!")
        break
      
    else:
        print("Invalid choice. Please select a valid option.")