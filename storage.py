import sqlite3

DB = "runs.db"

def init_db():

    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status INTEGER,
        latency REAL
    )
    """)

    conn.commit()


def save_run(status, latency):

    conn = sqlite3.connect(DB)

    conn.execute(
        "INSERT INTO runs(status, latency) VALUES (?, ?)",
        (status, latency)
    )

    conn.commit()


def list_runs():

    conn = sqlite3.connect(DB)

    rows = conn.execute(
        "SELECT * FROM runs ORDER BY id DESC LIMIT 20"
    )

    return rows.fetchall()
