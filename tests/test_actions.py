from datetime import datetime
import pytest
import src.actions as actions

def test_user_add_task_correctly():
    description = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    actions.add_task(description)
    
    added_task = actions.read_json()["tasks"][-1]
    
    assert added_task["description"] == description
    
def test_user_update_task_correctly():
    id, description = 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    actions.update_task(id, description)
    
    assert actions.read_json()["tasks"][0]["description"] == description
    
def test_user_update_task_incorrectly():
    id, description = 100, f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} 2026"
    actions.update_task(id, description)
    
    assert actions.read_json()["tasks"][0]["description"] != description

def test_user_mark_task_correctly():
    id, status = 1, "done"
    actions.mark_task(id, status)
    
    assert actions.read_json()["tasks"][0]["status"] == status

def test_user_mark_task_incorretly():
    id, status = 1, "false"
    actions.mark_task(id, status)
    
    assert actions.read_json()["tasks"][0]["status"] != status
    
def test_user_task_list_correctly():
    assert len(actions.read_json()["tasks"]) > 0
    
def test_user_task_list_by_status_correctly():
    status = "done"
    
    assert len(list(filter(lambda task: task["status"] == status, actions.read_json()["tasks"]))) > 0
    
def test_user_task_list_by_status_incorrectly():
    status = "false"
    actions.list_tasks_by_status(status)
    
    assert len(list(filter(lambda task: task["status"] == status, actions.read_json()["tasks"]))) == 0
    
def test_user_delete_task_incorrectly():
    id = 100
    actions.delete_task(id)
    
    assert len(actions.read_json()["tasks"]) > 0 
    
def test_user_delete_task_correctly():
    id = 1
    actions.delete_task(id)
    
    assert len(actions.read_json()["tasks"]) == 0