import json
import os
from datetime import datetime

TASK_FILE = "advanced_tasks.json"

PRIORITY_COLORS = {
    "High": "\033[91m",    # Red
    "Medium": "\033[93m",  # Yellow
    "Low": "\033[92m",     # Green
    "Done": "\033[90m"     # Gray
}
RESET = "\033[0m"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks, show_done=True):
    print("\n📋 Your Tasks:\n")
    for idx, task in enumerate(tasks):
        if not show_done and task["status"] == "Done":
            continue

        color = PRIORITY_COLORS.get(task["status"], PRIORITY_COLORS.get(task["priority"], ""))
        print(f"{color}{idx+1}. [{task['priority']}] {task['title']} (Due: {task['due']}) - {task['status']}{RESET}")

def add_task(tasks):
    title = input("✏️ Task title: ").strip()
    due = input("📅 Due date (YYYY-MM-DD): ").strip()
    priority = input("🔺 Priority (High/Medium/Low): ").capitalize().strip()
    
    if not title:
        print("⚠️ Task title cannot be empty.")
        return
    
    if not due:
        due = "No date"

    if priority not in ["High", "Medium", "Low"]:
        priority = "Low"

    tasks.append({
        "title": title,
        "due": due,
        "priority": priority,
        "status": "Pending"
    })

    save_tasks(tasks)  # 🔥 Save immediately
    print("✅ Task added and saved!")

def mark_done(tasks):
    display_tasks(tasks, show_done=False)
    try:
        index = int(input("✔️ Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks) and tasks[index]["status"] != "Done":
            tasks[index]["status"] = "Done"
            print("🎉 Task marked as done!")
        else:
            print("❌ Invalid or already done.")
    except:
        print("❗ Invalid input.")

def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("❌ Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            print(f"🗑️ Deleted: {tasks[index]['title']}")
            del tasks[index]
        else:
            print("❗ Invalid number.")
    except:
        print("❗ Invalid input.")

def filter_tasks(tasks):
    print("\n🔍 Filter Options:\n1. All\n2. Pending Only\n3. Done Only")
    choice = input("Select filter: ")
    if choice == "1":
        display_tasks(tasks, show_done=True)
    elif choice == "2":
        display_tasks(tasks, show_done=False)
    elif choice == "3":
        done = [t for t in tasks if t["status"] == "Done"]
        display_tasks(done, show_done=True)
    else:
        print("❌ Invalid option.")

def main():
    tasks = load_tasks()
    while True:
        print("\n🛠️ ADVANCED TO-DO LIST")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark as Done")
        print("4. Delete Task")
        print("5. Filter Tasks")
        print("6. Exit")

        choice = input("👉 Choose (1-6): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            filter_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("👋 Bye! Tasks saved.")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
