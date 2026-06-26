def CliMenu():
    print("this is a task manager, see above your options")
    print("1 | Add a task")
    print("2 | Show tasks")
    print("3 | update a task")
    print("4 | Change status")
    print("5 | Delete")

TempTask = {}
TaskId = 1

CliMenu()
user_input = input("Enter your choice: ")
if user_input == "1":
    TempTask["id"] = TaskId
    TaskId += 1
    TempTask["name"] = input("Enter task name: ")
    valid_status = ["todo", "done", "in progress"]
    
    TempTask["status"] = input("Enter task status: todo, done or in progress: ")   

print(TempTask)
print(TaskId)






