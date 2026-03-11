import sqlite3

DB = "runs.db"

def list_runs():

    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        status INTEGER,
        latency REAL
    )
    """)

    rows = conn.execute(
        "SELECT * FROM runs ORDER BY id DESC LIMIT 20"
    )

    return rows.fetchall()
