"""The class library (course site, Slide 08 "Python + SQLite"): one function to read, one to write."""
import sqlite3

# the database file; created next to this script the first time we connect
DB_PATH = "my_sql.db"


def connect():
    """Open a connection; row_factory lets us read a row like a dict: row["name"]."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def run_query_select(sql, params=()):
    """For SELECT: returns a list of dicts, one per row."""
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)  # the ? marks are filled from params: safe from SQL injection
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()  # always closed, even if the query fails


def run_update_query(sql, params=()):
    """For INSERT / UPDATE / DELETE / CREATE: saves (commit) and returns the id of the last inserted row."""
    conn = connect()
    try:
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()  # without commit nothing is written to the file (like Write Changes in DB Browser)
        return cursor.lastrowid
    finally:
        conn.close()
