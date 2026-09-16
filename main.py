from storage import load_tasks, save_tasks

# 获取用户输入的任务编号，判断是否合规，并转换为列表索引
def get_task_index(tasks, action):
    # 处理无效字符
    try:
        task_number = int(input(f"请输入要{action}的任务编号："))
    except ValueError:
        print("请输入有效的任务数字编号!!!")
        return None
    # 处理无效数字
    if task_number < 1 or task_number > len(tasks):
        print("没有这个任务编号!!!")
        return None

    return task_number - 1

# 查看任务
def show_tasks(tasks):
    if not tasks:
        print("目前没有任务。")
    else:
        print("\n当前任务：")
        for index, task in enumerate(tasks, start=1):
            status = "[√]" if task["done"] else "[ ]"
            print(f"{index}. {status} {task['title']}")

def main():
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
            # .strip() 方法用于去除输入字符串的首尾空白字符，确保用户输入的任务不为空
            task = input("请输入任务：").strip()
            if not task:
                print("任务不能为空。")
                continue
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
            show_tasks(tasks)

        # 完成任务
        elif choice == "3":
            index = get_task_index(tasks, "完成")
            if index is None:
                continue
            # 标记任务为已完成
            tasks[index]["done"] = True
        
            # 保存更新后的任务状态
            save_tasks(tasks)
                
            print("任务已完成。")

        # 删除任务
        elif choice == "4":
            index = get_task_index(tasks, "删除")
            if index is None:
                continue
            # 删除任务
            removed_task = tasks.pop(index)
            
            # 保存删除过后的任务列表
            save_tasks(tasks)
            
            print(f"已删除任务：{removed_task['title']}")
        else: 
            print("无效的选择。")
            
# 如果当前文件是被直接运行的，就执行 main()
if __name__ == "__main__":
    main()
