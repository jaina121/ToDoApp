from datetime import date
import re

from flask import Blueprint, jsonify, render_template, request

from .storage import load_tasks, save_tasks

bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    return render_template("index.html")


@bp.route("/tasks")
def tasks():
    return jsonify(load_tasks())


@bp.route("/add", methods=["POST"])
def add():
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("text", "")).strip()
    deadline = str(payload.get("deadline", "")).strip()

    if not text:
        return jsonify({"status": "error", "message": "Task text is required"}), 400

    if deadline:
        try:
            date.fromisoformat(deadline)
        except ValueError:
            return jsonify({"status": "error", "message": "Invalid deadline"}), 400

    tasks = load_tasks()
    tasks.append({"text": text, "done": False, "deadline": deadline or None})
    save_tasks(tasks)
    return jsonify({"status": "ok"})


@bp.route("/toggle", methods=["POST"])
def toggle():
    payload = request.get_json(silent=True) or {}
    tasks = load_tasks()

    try:
        index = int(payload["index"])
        tasks[index]["done"] = not tasks[index]["done"]
    except (KeyError, TypeError, ValueError, IndexError):
        return jsonify({"status": "error", "message": "Invalid task index"}), 400

    save_tasks(tasks)
    return jsonify({"status": "ok"})


@bp.route("/update", methods=["POST"])
def update():
    payload = request.get_json(silent=True) or {}
    tasks = load_tasks()

    try:
        index = int(payload["index"])
        text = str(payload.get("text", "")).strip()
        if not text:
            return jsonify({"status": "error", "message": "Task text is required"}), 400

        tasks[index]["text"] = text
    except (KeyError, TypeError, ValueError, IndexError):
        return jsonify({"status": "error", "message": "Invalid task update"}), 400

    save_tasks(tasks)
    return jsonify({"status": "ok"})


@bp.route("/delete", methods=["POST"])
def delete():
    payload = request.get_json(silent=True) or {}
    tasks = load_tasks()

    try:
        index = int(payload["index"])
        tasks.pop(index)
    except (KeyError, TypeError, ValueError, IndexError):
        return jsonify({"status": "error", "message": "Invalid task delete"}), 400

    save_tasks(tasks)
    return jsonify({"status": "ok"})


@bp.route("/suggest", methods=["POST"])
def suggest():
    payload = request.get_json(silent=True) or {}
    task_text = str(payload.get("text", "")).strip()

    if not task_text:
        return jsonify({"status": "error", "message": "Task text is required"}), 400

    return jsonify({"status": "ok", "suggestions": build_suggestions(task_text)})


def build_suggestions(task_text):
    normalized = task_text.lower()

    template_map = [
        (r"project|app|website|site", [
            "Define the goal and scope",
            "List the main features",
            "Build the first working version",
            "Test the core flow",
        ]),
        (r"study|learn|course|exam|test", [
            "Review the topic outline",
            "Study the key concepts",
            "Practice with examples",
            "Do a quick self-check",
        ]),
        (r"buy|shop|order", [
            "Check what is already available",
            "Make a short shopping list",
            "Compare options or prices",
        ]),
        (r"email|message|call|contact", [
            "Collect the needed details",
            "Write a short draft",
            "Send or schedule the message",
        ]),
    ]

    for pattern, suggestions in template_map:
        if re.search(pattern, normalized):
            return suggestions[:5]

    words = [word for word in re.findall(r"[a-zA-Zа-яА-Я0-9]+", task_text) if len(word) > 3][:3]
    base = words[0] if words else task_text

    return [
        f"Clarify what '{base}' should include",
        f"Split '{base}' into smaller steps",
        f"Complete the first step for '{base}'",
        f"Review the result and finish '{base}'",
    ]
