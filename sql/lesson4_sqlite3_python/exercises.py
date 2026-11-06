"""Practice for Python + SQLite with the class db.py. Each exercise: the task (comment), the solution, a check.
Run: python exercises.py  (uses its own practice.db, rebuilt on every run)."""
import os
import sqlite3

import db
from db import run_query_select, run_update_query

db.DB_PATH = "practice.db"  # the library reads DB_PATH on every connect(): point it at a practice file
if os.path.exists(db.DB_PATH):
    os.remove(db.DB_PATH)  # start clean, so running this twice gives the same results

# 1) Create a books table (id auto, title and author required, year) and insert 4 books with ? parameters.
#    run_update_query returns the new row's id (lastrowid).
run_update_query("""CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER)""")
ids = [run_update_query("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", b) for b in (
    ("I, Robot", "Isaac Asimov", 1950),
    ("Sapiens", "Yuval Noah Harari", 2011),
    ("Homo Deus", "Yuval Noah Harari", 2015),
    ("Foundation", "Isaac Asimov", 1951))]
print("1) new ids:", ids)
assert ids == [1, 2, 3, 4]

# 2) Books published after 2000. The year comes from a variable -> pass it as a parameter, never glue it into the SQL.
after = 2000
recent = run_query_select("SELECT title, year FROM books WHERE year > ? ORDER BY year", (after,))
print("2) after 2000:", recent)
assert recent == [{"title": "Sapiens", "year": 2011}, {"title": "Homo Deus", "year": 2015}]

# 3) Search: the user typed "Found" -> titles containing it. The % wildcards go INSIDE the parameter.
word = "Found"
found = run_query_select("SELECT title FROM books WHERE title LIKE ?", (f"%{word}%",))
print("3) search:", found)
assert found == [{"title": "Foundation"}]

# 4) Update a year, delete a book, then count what is left (COUNT with an alias so the dict key is readable).
run_update_query("UPDATE books SET year = ? WHERE title = ?", (1952, "Foundation"))
run_update_query("DELETE FROM books WHERE id = ?", (3,))  # (3,) - a one-item tuple needs the comma
count = run_query_select("SELECT COUNT(*) AS n FROM books")[0]["n"]
print("4) books left:", count)
assert count == 3

# 5) Books per author (GROUP BY from Python) - the result is a list of dicts like any SELECT.
per_author = run_query_select("SELECT author, COUNT(*) AS books FROM books GROUP BY author ORDER BY books DESC")
print("5) per author:", per_author)
assert per_author == [{"author": "Isaac Asimov", "books": 2}, {"author": "Yuval Noah Harari", "books": 1}]

# 6) Why parameters: SQL injection. A "name" typed by a user that changes the meaning of the query.
evil = "x' OR '1'='1"
unsafe = run_query_select(f"SELECT title FROM books WHERE author = '{evil}'")  # NEVER do this
safe = run_query_select("SELECT title FROM books WHERE author = ?", (evil,))
print(f"6) unsafe f-string returned {len(unsafe)} rows (all of them!), safe ? returned {len(safe)}")
assert len(unsafe) == 3 and safe == []

# 7) Foreign keys from Python: PRAGMA foreign_keys is per CONNECTION, and db.py opens a new connection on every
#    call - so run_update_query("PRAGMA foreign_keys = ON") does nothing for the next call.
run_update_query("CREATE TABLE IF NOT EXISTS authors (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")
run_update_query("""CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, stars INTEGER,
    author_id INTEGER NOT NULL, FOREIGN KEY (author_id) REFERENCES authors(id))""")
run_update_query("PRAGMA foreign_keys = ON")
run_update_query("INSERT INTO reviews (stars, author_id) VALUES (?, ?)", (5, 99))  # author 99 doesn't exist...
print("7) without FK in connect(): a review of author 99 was accepted (no error)")
original_connect = db.connect


def connect_with_fk():  # the fix: switch it on inside connect(), for every connection
    conn = original_connect()
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


db.connect = connect_with_fk
try:
    run_update_query("INSERT INTO reviews (stars, author_id) VALUES (?, ?)", (4, 98))
    blocked = False
except sqlite3.IntegrityError as e:
    blocked = True
    print("   with FK in connect():", e)
assert blocked

# 8) The class main.py adds Alice, Bob, Carol again on every run (CREATE TABLE IF NOT EXISTS keeps the old rows).
#    One fix: make the name UNIQUE and use INSERT OR IGNORE, so a second run changes nothing.
run_update_query("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL UNIQUE, grade INTEGER)")
for _ in range(2):  # "run the script twice"
    run_update_query("INSERT OR IGNORE INTO students (name, grade) VALUES (?, ?)", ("Alice", 90))
n = run_query_select("SELECT COUNT(*) AS n FROM students")[0]["n"]
print("8) Alice after two runs:", n, "row")
assert n == 1

print("\nALL 8 EXERCISES PASSED")
