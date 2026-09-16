import json
from pathlib import Path

# 定义数据文件的路径，存储任务数据
# __file__ 是当前文件的路径，parent 是当前文件所在的目录，"tasks.json" 是数据文件名
DATA_FILE = Path(__file__).parent / "tasks.json"

# 函数：保存当前程序中的任务到json文件
def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

# 函数：读取json文件中的任务
def load_tasks():
    # 尝试读取文件，如果文件不存在则返回空列表
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        # 如果文件不存在，则返回空列表
        return [] 
    except json.JSONDecodeError:
        # 如果文件内容不是有效的JSON格式，则返回空列表
        return []