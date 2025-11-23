import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table

JSON_PATH = os.path.join(os.path.dirname(__file__), "../tasks.json")
console = Console()

def read_json():
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"tasks": []}

def write_json(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
def display_table(data):
    table = Table(show_lines=True)
    table.add_column("ID")
    table.add_column("Task")
    table.add_column("Status")
    
    for task in data:
        table.add_row(str(task['id']), task['description'], task['status'])
        
    return table

def list_tasks():
    data = read_json()
        
    property_table = display_table(data["tasks"])
    
    console.print(property_table)
    
    return data["tasks"]
    
def list_tasks_by_status(status):
    if(status not in ["todo", "in-progress", "done"]):
        console.print("INVALID STATUS!", style="red on white")
        
        return []
    
    data = read_json()
    
    filtered = [t for t in data["tasks"] if t["status"] == status]
    
    console.print(display_table(filtered))
    
    return filtered

def add_task(description):
    data = read_json()
    
    new_id = data["tasks"][-1]["id"] + 1 if data["tasks"] else 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": now,
        "updatedAt": now,
    }

    data["tasks"].append(task)
    
    write_json(data)
    
    added_task = display_table([task])
    
    console.print(added_task)
    
    return task
        
def update_task(task_id, description):
    data = read_json()
    tasks = data["tasks"]
    
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            updated_task = display_table([task])
            
            console.print(updated_task)
            
            write_json(data)
            
            return task
    
    console.print("TASK NOT FOUND!", style="red on white")
    
    return None
        
def mark_task(task_id, status):
    if status not in ["todo", "in-progress", "done"]:
        console.print("INVALID STATUS!", style="red on white")
        return None

    data = read_json()
    
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            updated_task = display_table([task])
            
            console.print(updated_task)
            
            write_json(data)
            
            return task

    console.print("TASK NOT FOUND!", style="red on white")
    
    return None 
        
def delete_task(task_id):
    data = read_json()
    
    tasks = data["tasks"]

    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            deleted = tasks.pop(i)
            
            write_json(data)
            
            list_tasks()
            
            return deleted

    console.print("TASK NOT FOUND!", style="red on white")
    
    return None