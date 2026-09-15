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
    elif choice in ["1", "2", "3", "4"]:
        print("这个功能下一步实现。")
    else: 
        print("无效的选择。")