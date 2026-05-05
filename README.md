# AI Vibe Todo App

An AI-assisted Todo web application built with Flask.

This project is designed to demonstrate a structured vibe-coding workflow: AI tools are used for planning, coding, refactoring, and iterative improvement, not only for one-time code generation.

## Project Goal

Build a practical and testable task manager while showing how AI can be integrated into a real development process with clear instructions and traceable iterations.

## Features

### Core Todo Functions
- Add tasks
- Edit tasks
- Mark tasks as complete or active
- Delete tasks
- Filter by All, Active, and Done

### Deadline and Reminder Support
- Optional deadline per task
- Visual labels for Today and Tomorrow
- Overdue tasks highlighted in red
- Browser notification on task creation

### Mini Analytics
- Completed tasks count
- Remaining tasks count
- Progress percentage

### AI Suggestion Workflow
- Input a task idea
- Generate 3-5 suggested subtasks
- Display suggestions in the UI
- Add all suggested subtasks into the main task list

## Why This Is an AI Vibe-Coding Project

This project was developed iteratively with AI support:
- Started from a simple scaffold
- Improved structure and user experience step by step
- Added new features through guided AI prompts
- Kept the codebase organized with explicit agent instructions

It demonstrates an AI-assisted workflow with continuous refinement, not just a one-shot generated app.

## AI Project Files

- [AGENTS.md](AGENTS.md): root-level agent instructions
- [ai/AGENT.md](ai/AGENT.md): project-specific AI behavior
- [ai/.cursorrules](ai/.cursorrules): coding guidance for Cursor-style agents
- [ai/PROMPTS.md](ai/PROMPTS.md): prompt history and context

## Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- JSON file storage
- Pytest for basic validation

## Run Locally

1. Activate virtual environment.
2. Start the app:

```bash
python app.py
```

3. Open in browser:

```text
http://127.0.0.1:5000
```

## Quick Presentation Version

This is an AI-assisted Flask Todo app built with a vibe-coding approach. It includes task CRUD, deadlines, overdue highlighting, mini analytics, browser notifications, and an AI subtask generator. The repository also contains dedicated AI instruction files and prompt history, showing how AI tools were used throughout the development workflow.