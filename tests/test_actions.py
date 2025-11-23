from datetime import datetime
import pytest
import src.actions as actions

@pytest.fixture(autouse=True)
def isolated_json(tmp_path, monkeypatch):
    json_file = tmp_path / "tasks.json"
    json_file.write_text('{"tasks": []}', encoding="utf-8")
    
    monkeypatch.setattr(actions, "JSON_PATH", str(json_file))

def test_add_task_creates_new_task():
    description = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = actions.add_task(description)

    assert task["description"] == description
    assert task["status"] == "todo"
    assert task["id"] == 1

    data = actions.read_json()
    assert len(data["tasks"]) == 1
    
def test_update_task_modifies_description_when_id_exists():
    original = actions.add_task("original")
    task_id = original["id"]

    new_desc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated = actions.update_task(task_id, new_desc)

    assert updated is not None
    assert updated["description"] == new_desc

    data = actions.read_json()
    
    assert data["tasks"][0]["description"] == new_desc
    
def test_update_task_returns_none_when_id_does_not_exist():
    actions.add_task("original desc")

    result = actions.update_task(999, "new desc")

    assert result is None

    data = actions.read_json()
    
    assert data["tasks"][0]["description"] == "original desc"

def test_mark_task_updates_status_when_valid_status_is_given():
    task = actions.add_task("task")
    task_id = task["id"]

    updated = actions.mark_task(task_id, "done")

    assert updated is not None
    assert updated["status"] == "done"

def test_mark_task_returns_none_when_status_is_invalid():
    task = actions.add_task("invalid")
    task_id = task["id"]

    result = actions.mark_task(task_id, "invalid-status")
    
    assert result is None
    assert actions.read_json()["tasks"][0]["status"] == "todo"
    
def test_list_tasks_returns_all_existing_tasks():
    actions.add_task("A")
    actions.add_task("B")

    tasks = actions.list_tasks()

    assert len(tasks) == 2
    assert any(task["description"] == "A" for task in tasks)
    
def test_list_tasks_by_status_returns_only_tasks_matching_status():
    t1 = actions.add_task("A")
    t2 = actions.add_task("B")

    actions.mark_task(t1["id"], "done")

    filtered = actions.list_tasks_by_status("done")
    
    assert len(filtered) == 1
    assert filtered[0]["status"] == "done"
    
def test_list_tasks_by_status_returns_empty_list_when_status_is_invalid():
    actions.add_task("A")

    filtered = actions.list_tasks_by_status("invalid")

    assert filtered == []
    
def test_delete_task_returns_none_when_id_does_not_exist():
    actions.add_task("exists")

    result = actions.delete_task(999)

    assert result is None
    assert len(actions.read_json()["tasks"]) == 1
    
def test_delete_task_removes_task_when_id_exists():
    task = actions.add_task("to delete")
    task_id = task["id"]

    deleted = actions.delete_task(task_id)

    assert deleted is not None
    assert deleted["id"] == task_id
    assert len(actions.read_json()["tasks"]) == 0