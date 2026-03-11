import sqlite3

DB = "runs.db"

def save_run(status, latency):

    conn = sqlite3.connect(DB)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs(
        id INTEGER PRIMARY KEY,
        status INTEGER,
        latency REAL
    )
    """)

    conn.execute(
        "INSERT INTO runs(status,latency) VALUES (?,?)",
        (status, latency)
    )

    conn.commit()

def list_runs():

    conn = sqlite3.connect(DB)

    rows = conn.execute(
        "SELECT * FROM runs ORDER BY id DESC LIMIT 20"
    )

    return rows.fetchall()
