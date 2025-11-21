import os
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table

full_path = os.path.join(os.path.dirname(__file__), "../tasks.json")
console = Console()

def read_json():
    with open(full_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    return data

def write_json(data):
    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
def display_table(data):
    property_table = Table(show_lines=True)
    property_table.add_column("ID")
    property_table.add_column("Task")
    property_table.add_column("Status")
    
    for task in data:
        property_table.add_row(str(task['id']), task['description'], task['status'])
        
    return property_table

def list_tasks():
    data = read_json()
        
    property_table = display_table(data["tasks"])
    
    console.print(property_table)
    
def list_tasks_by_status(status):
    data = read_json()
    
    if(status not in ["todo", "in-progress", "done"]):
        console.print("INVALID STATUS!", style="red on white")
        
        return
    
    property_table = display_table(filter(lambda task: task["status"] == status, data["tasks"]))
    
    console.print(property_table)

def add_task(description):
    data = read_json()
    
    id = data["tasks"][-1]["id"] + 1 if len(data["tasks"]) > 0 else 1

    data["tasks"].append({
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    write_json(data)
    
    print(f"Task added successfully (ID: {id})")
        
def update_task(id, description):
    data = read_json()
        
    index = next((i for i, item in enumerate(data["tasks"]) if item["id"] == id), None)
    
    if index is not None:
        data["tasks"][index]["description"] = description
        data["tasks"][index]["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        write_json(data)
    else:
        console.print("TASK NOT FOUND!", style="red on white")
        
        return
        
def mark_task(id, status):
    data = read_json()
    
    if(status not in ["todo", "in-progress", "done"]):
        console.print("INVALID STATUS!", style="red on white")
        
        return
    
    index = next((i for i, item in enumerate(data["tasks"]) if item["id"] == id), None)
    
    if index is not None:
        data["tasks"][index]["status"] = status
    else:
        console.print("TASK NOT FOUND!", style="red on white")
        
        return
    
    write_json(data)  
        
def delete_task(id):
    data = read_json()
    
    index = next((i for i, item in enumerate(data["tasks"]) if item["id"] == id), None)
    
    if index is not None:
        data["tasks"].pop(index)
        
        write_json(data)
    else:
        console.print("TASK NOT FOUND!", style="red on white")
        
        return
        
    write_json(data)