import sys
import src.actions as actions

def main():
    match sys.argv[1]:
        case "list":
            if len(sys.argv) > 2:
                actions.list_tasks_by_status(sys.argv[2])
            else:
                actions.list_tasks()
        case "add":
            actions.add_task(sys.argv[2])
        case "mark-todo":
            actions.mark_task(int(sys.argv[2]), "todo")
        case "mark-done":
            actions.mark_task(int(sys.argv[2]), "done")
        case "mark-in-progress":
            actions.mark_task(int(sys.argv[2]), "in-progress")
        case "update":
            actions.update_task(int(sys.argv[2]), sys.argv[3])
        case "delete":
            actions.delete_task(int(sys.argv[2]))