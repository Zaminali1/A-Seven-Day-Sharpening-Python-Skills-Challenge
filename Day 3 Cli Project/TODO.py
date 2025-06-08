# ✅ 1. TODO LIST – Instructions (Text-Based Agent Tool)

# 1. Create an empty list to store tasks:

# todo_list = []


# 2. Start a loop to continuously ask the user what they want to do:

# while True:
#     command = input("Add/View/Quit: ").lower()


# 3. If the user types "add":

# Ask them for the task name.

# Add it to the list.


# if command == "add":
#     task = input("Enter task: ")
#     todo_list.append(task)
#     print("Task added.")


# 4. If the user types "view":

# Show all tasks in the list.


# elif command == "view":
#     for i, task in enumerate(todo_list, 1):
#         print(f"{i}. {task}")


# 5. If the user types "quit", exit the loop:

# elif command == "quit":
#     break







todo_list=[]
while True :
 command=input("Add/View/Quit: ").lower()
 if command == "add":
  task=input("Enter Task: ")
  todo_list.append(task)
  print("Task Added...")
 elif command== "view":
     if not todo_list:
      print("No Task Available")
     else:
         for i, task in enumerate(todo_list, 1):
          print(f"{i} {task}")
 elif command == "quit":
   break 
 else:
     print("Invalid command Try add view quit") 