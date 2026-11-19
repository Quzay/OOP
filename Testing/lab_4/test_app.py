import json
import sqlite3
import pytest
from app import app, init_db, export_tasks


@pytest.fixture
def db_path(tmp_path):
    path = str(tmp_path / "test.db")
    init_db(path)
    return path


@pytest.fixture
def client(db_path, monkeypatch):
    monkeypatch.setattr("app.DB_PATH", db_path)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# --- HTTP тести ---

def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = client.post("/tasks", json={"title": "Вивчити Flask"})
    assert response.status_code == 201
    assert response.get_json()["message"] == "created"


def test_create_task_no_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_get_tasks_after_create(client):
    client.post("/tasks", json={"title": "Завдання 1"})
    response = client.get("/tasks")
    assert response.status_code == 200
    tasks = response.get_json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Завдання 1"


# --- SQLite тести ---

def test_task_saved_in_db(client, db_path):
    client.post("/tasks", json={"title": "Перевірка БД"})
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT title FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    assert len(rows) == 1
    assert rows[0][0] == "Перевірка БД"


def test_two_tasks_order_in_db(client, db_path):
    client.post("/tasks", json={"title": "Перше"})
    client.post("/tasks", json={"title": "Друге"})
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT title FROM tasks")
    rows = [row[0] for row in cursor.fetchall()]
    conn.close()
    assert rows == ["Перше", "Друге"]


# --- JSON експорт тести ---

def test_export_tasks(client, db_path, tmp_path):
    client.post("/tasks", json={"title": "Експорт"})
    filepath = str(tmp_path / "tasks.json")
    export_tasks(filepath, db_path)
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["title"] == "Експорт"


def test_export_empty_tasks(db_path, tmp_path):
    filepath = str(tmp_path / "empty.json")
    export_tasks(filepath, db_path)
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)
    assert data == []