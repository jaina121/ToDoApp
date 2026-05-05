import json
from pathlib import Path


FILE = Path("data/tasks.json")


def load_tasks():
    if not FILE.exists():
        return []

    try:
        with FILE.open("r", encoding="utf-8") as file_handle:
            tasks = json.load(file_handle)
    except json.JSONDecodeError:
        return []

    if not isinstance(tasks, list):
        return []

    cleaned_tasks = []
    for task in tasks:
        if not isinstance(task, dict):
            continue

        text = str(task.get("text", "")).strip()
        if not text:
            continue

        deadline_value = task.get("deadline")
        deadline = str(deadline_value).strip() if deadline_value not in (None, "") else ""
        if deadline in {"None", "null", "undefined"}:
            deadline = ""

        cleaned_tasks.append({
            "text": text,
            "done": bool(task.get("done", False)),
            "deadline": deadline or None,
        })

    return cleaned_tasks


def save_tasks(tasks):
    FILE.parent.mkdir(parents=True, exist_ok=True)
    with FILE.open("w", encoding="utf-8") as file_handle:
        json.dump(tasks, file_handle, indent=2, ensure_ascii=False)