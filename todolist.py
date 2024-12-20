def AddTasks():
    number_tasks=int(input("Enter Number of Tasks Want to Add:"))
    for i in range(number_tasks):
        tasks=input("Enter the Task:")
        print("Task is Added!")
        Task_dic[tasks]='Not Done'

def ViewTask():
    print("Tasks:")
    sno = 1
    for i,j in Task_dic.items():
        print(f'{sno}.{i} - {j}')
        sno+=1
def RemoveTask():
    delete_task=input("Enter the Task to be Removed:")
    if delete_task in Task_dic:
        Task_dic.pop(delete_task)
        print("Task is Deleted Successfully")
    else:
        print("Task is not found")
def Mark_task_completed():
    task_done=input("Enter The task to be  mark as done:")
    Task_dic[task_done]='Done'
    print("Task Marked as Done!")
def InvalidTask():
    print("You entered Invalid Task")
n=True
Task_dic={}
while n:
    print("===***===To-Do-List===***===")
    print('1.Add Task','2.View Task','3.Delete Task','4.Mark Task As Completed','5.Exit',sep='\n')
    user_choice=int(input("Enter Your Choice:"))
    if user_choice==1:
        AddTasks()
    elif user_choice==2:
        ViewTask()
    elif user_choice==3:
        RemoveTask()
    elif user_choice==4:
        Mark_task_completed()
    elif user_choice==5:
        break
    else:
        InvalidTask()
