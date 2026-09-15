import json

# 函数：保存当前程序中的任务到json文件
def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

# 函数：读取json文件中的任务
def load_tasks():
    try:
        with open("tasks.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # 如果文件不存在，则返回空列表
        return [] 

# 尝试读取上一次保存的任务
tasks = load_tasks()

while True:
    print("\n我的待办")
    print("1.添加任务")
    print("2.查看任务")
    print("3.完成任务")
    print("4.删除任务")
    print("0.退出")
    
    choice = input("请选择: ")
    
    # 退出程序
    if choice == "0":
        print("程序已退出")
        break
    
    # 添加任务
    elif choice == "1":
        task = input("请输入任务：")
        new_task = {
            "title": task,
            "done": False
        }
        
        tasks.append(new_task)
        
        # 将当前任务保存到文件中
        save_tasks(tasks)
                
        print("任务已添加。")
    
    # 查看任务
    elif choice == "2":
        if not tasks:
            print("目前没有任务。")
        else:
            print("\n当前任务：")
            # enumerate:遍历列表的同时，顺便给每个元素配一个编号
            for index, task in enumerate(tasks, start=1):
                if task["done"]:
                    status = "[√]"
                else:
                    status = "[ ]"
                print(f"{index}. {status} {task['title']}")
    elif choice == "3":
        # 处理无效字符
        try:
            task_number = int(input("请输入要完成的任务编号："))
        except ValueError:
            print("请输入有效的任务数字编号!!!")
            continue
        
        # 处理无效数字
        if task_number < 1 or task_number > len(tasks):
            print("没有这个任务编号!!!")
            continue
        
        # 在列表内索引减一
        index = task_number - 1
        
        # 标记任务为已完成
        tasks[index]["done"] = True
    
        # 保存更新后的任务状态
        save_tasks(tasks)
            
        print("任务已完成。")
    elif choice == "4":
        # 处理无效字符
        try:
            task_number = int(input("请输入要删除的任务编号："))
        except ValueError:
            print("请输入有效的任务数字编号!!!")
            continue
        
        # 处理无效数字
        if task_number < 1 or task_number > len(tasks):
            print("没有这个任务编号!!!")
            continue
        
        index = task_number - 1
        
        # 删除任务
        removed_task = tasks.pop(index)
        
        # 保存删除过后的任务列表
        save_tasks(tasks)
        
        print(f"已删除任务：{removed_task['title']}")
    else: 
        print("无效的选择。")
