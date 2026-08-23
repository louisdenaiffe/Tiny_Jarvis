import sqlite3
import time
from pathlib import Path


con = sqlite3.connect(Path(__file__).parent / "tiny_jarvis.db")
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        content TEXT,
        created_at REAL
    )
""")


def new_entry(content):
    created_at = time.time()
    try:
        cur.execute("""
            INSERT INTO memory
            VALUES (?, ?)
        """, (content, created_at))
        con.commit()
    except Exception as e:
        return f"Error while committing to memory : {e}"


def get_recent_memories():
    try:
        cur.execute("""
            SELECT content, created_at
            FROM memory
            ORDER BY created_at DESC
            LIMIT 5
        """)
        return cur.fetchall()
    except Exception as e:
        return f"Error while retrieving memories: {e}"


def delete_all():
    try:
        cur.execute("DELETE FROM memory")
        con.commit()
    except Exception as e:
        return f"Error while deleting memories: {e}"