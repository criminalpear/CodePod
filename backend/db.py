import sqlite3

conn = sqlite3.connect("snippets.db", check_same_thread=False)

def init():
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS snippets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            language TEXT,
            code TEXT
        )
        """)

def get_all_snippets():
    return conn.execute("SELECT * FROM snippets").fetchall()

def add_snippet(title, language, code):
    with conn:
        conn.execute("INSERT INTO snippets (title, language, code) VALUES (?, ?, ?)",
                     (title, language, code))
