TASKS_FILE = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")


tasks = load_tasks()
while True:
    print("\n我的待办")
    print("1.添加任务")
    print("2.查看任务")
    print("3.完成任务")
    print("4.删除任务")
    print("0.退出")
    
    choice = input("请选择: ")
    
    if choice == "0":
        print("程序已退出")
        break
    elif choice == "1":
        task = input("请输入任务：")
        tasks.append(task)
        save_tasks(tasks)
        print("任务已添加。")
    elif choice == "2":
        if not tasks:
            print("目前没有任务。")
        else:
            print("当前任务：")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
    elif choice in ["3", "4"]:
        print("这个功能下一步实现")
    else: 
        print("无效的选择。")
