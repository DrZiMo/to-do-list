def display_all_tasks(tasks):
    if len(tasks) > 0:
        print("\nAll tasks:")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
    else:
        print("There are no tasks!\n")

def add_new_task(tasks):
    print("ADD NEW TASK:")

    newTask = input("Enter the new task: ")
    tasks.append(newTask)

    print(f"\n{newTask} was added to the tasks!\n")

def delete_a_task(tasks):
    print("DELETE A TASK:")

    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]}")

    RemoveTask = int(input("Enter the number of the task: ")) - 1
    del tasks[RemoveTask]

    task_to_delete = tasks[RemoveTask - 1]
    print(f"\n{task_to_delete} was removed from the tasks!\n")

def to_list_app():
    tasks = ["one", "two"]

    while 1 == 1:
        print("\nTODO LIST APP:")
        print("1. View all tasks")
        print("2. Add a new task")
        print("3. Delete a task")
        print("4. Exit")

        choose = input("\nChoose: ")

        if(choose == '1'):
            display_all_tasks(tasks)
        elif(choose == '2'):
            add_new_task(tasks)
        elif(choose == '3'):
            delete_a_task(tasks)
        elif(choose == '4'):
            exit()
        else:
            print("Invalid number!")

to_list_app()