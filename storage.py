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
