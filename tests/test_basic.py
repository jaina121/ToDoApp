from app import create_app


def test_home_route():
    app = create_app()

    with app.test_client() as client:
        response = client.get("/")

    assert response.status_code == 200
    assert b"AI Vibe Todo App" in response.data


def test_add_task_requires_text():
    app = create_app()

    with app.test_client() as client:
        response = client.post("/add", json={"text": "   "})

    assert response.status_code == 400
    assert response.get_json()["status"] == "error"


def test_add_task_accepts_deadline():
    app = create_app()

    with app.test_client() as client:
        response = client.post("/add", json={"text": "Study", "deadline": "2026-05-01"})
        tasks = client.get("/tasks").get_json()

    assert response.status_code == 200
    assert tasks[-1]["deadline"] == "2026-05-01"


def test_suggest_endpoint_returns_subtasks():
    app = create_app()

    with app.test_client() as client:
        response = client.post("/suggest", json={"text": "study math"})

    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "ok"
    assert len(data["suggestions"]) >= 3
