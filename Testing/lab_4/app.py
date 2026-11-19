import json
from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = "tasks.db"


def init_db(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def export_tasks(filepath, db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT id, title FROM tasks")
    tasks = [{"id": row[0], "title": row[1]} for row in cursor.fetchall()]
    conn.close()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT id, title FROM tasks")
    tasks = [{"id": row[0], "title": row[1]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO tasks (title) VALUES (?)", (data["title"],))
    conn.commit()
    conn.close()
    return jsonify({"message": "created"}), 201


if __name__ == "__main__":
    init_db()
    app.run(debug=True)