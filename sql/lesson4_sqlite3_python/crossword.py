"""Lesson 29 crossword (course site: 99_games/sql_02_co) - one query per clue, checked against the grid's answer.
Builds crossword.db with the site's 'sales' table (open it in DB Browser / the PyCharm plugin to try the queries yourself).
Topics: COUNT(*) vs COUNT(column), SUM/AVG/MIN/MAX, GROUP BY, HAVING, ORDER BY ... LIMIT."""
import os
import sqlite3

import db
from db import run_query_select

# copied from the site page: 100 sales, 4 reps, 4 regions, 3 products, 2 NULL amounts (rows 12 and 33)
INIT_SQL = """
CREATE TABLE sales (
  id        INTEGER PRIMARY KEY,
  rep_name  TEXT    NOT NULL,
  region    TEXT    NOT NULL,
  product   TEXT    NOT NULL,
  amount    REAL,
  sale_date TEXT    NOT NULL
);
WITH RECURSIVE seq(n) AS (SELECT 1 UNION ALL SELECT n + 1 FROM seq WHERE n < 100)
INSERT INTO sales (id, rep_name, region, product, amount, sale_date)
SELECT
  n,
  CASE WHEN n <= 52 THEN 'Dana' WHEN n <= 62 THEN 'Omar' WHEN n <= 92 THEN 'Noa' ELSE 'Liam' END,
  CASE WHEN n <= 52 THEN 'North' WHEN n <= 62 THEN 'South' WHEN n <= 92 THEN 'East' ELSE 'West' END,
  CASE
    WHEN n <= 52 THEN CASE WHEN n <= 5 THEN 'Laptop' WHEN n <= 47 THEN 'Tablet' ELSE 'Phone' END
    WHEN n <= 62 THEN CASE WHEN n <= 56 THEN 'Laptop' WHEN n <= 59 THEN 'Phone' ELSE 'Tablet' END
    WHEN n <= 92 THEN CASE WHEN n <= 72 THEN 'Laptop' WHEN n <= 82 THEN 'Phone' ELSE 'Tablet' END
    ELSE CASE WHEN n <= 94 THEN 'Laptop' WHEN n <= 98 THEN 'Phone' ELSE 'Tablet' END
  END,
  CASE
    WHEN n <= 52 THEN CASE WHEN n IN (12, 33) THEN NULL WHEN n <= 5 THEN 1400 + (n * 20)
                           WHEN n <= 47 THEN 320 + ((n * 7) % 180) ELSE 360 + ((n * 11) % 120) END
    WHEN n <= 62 THEN CASE WHEN n <= 56 THEN 1150 + ((n * 13) % 120) WHEN n <= 59 THEN 390 + ((n * 9) % 80)
                           ELSE 470 + ((n * 5) % 70) END
    WHEN n <= 92 THEN CASE WHEN n = 63 THEN 2200 WHEN n <= 72 THEN 1250 + ((n * 17) % 220)
                           WHEN n <= 82 THEN 420 + ((n * 7) % 110) ELSE 500 + ((n * 3) % 140) END
    ELSE CASE WHEN n = 93 THEN 250 WHEN n <= 94 THEN 980 + ((n * 5) % 60) WHEN n <= 98 THEN 380 + ((n * 4) % 70)
              ELSE 430 + ((n * 6) % 90) END
  END,
  date('2026-01-01', '+' || (n - 1) || ' day')
FROM seq;
"""

# (grid word, clue, query, expected first column of the result)
CLUES = [
    ("SALES", "What is the table name?",
     "SELECT name FROM sqlite_master WHERE type = 'table'", ["sales"]),
    ("THREE", "How many distinct products are there?",
     "SELECT COUNT(DISTINCT product) FROM sales", [3]),
    ("FOUR", "How many distinct reps are there?",
     "SELECT COUNT(DISTINCT rep_name) FROM sales", [4]),
    ("TWO", "How many rows have a NULL amount?",
     "SELECT COUNT(*) FROM sales WHERE amount IS NULL", [2]),  # = NULL never matches, use IS NULL
    ("NORTH", "Which region has the most sales overall?",
     "SELECT region, COUNT(*) AS n FROM sales GROUP BY region ORDER BY n DESC LIMIT 1", ["North"]),
    ("TEN", "How many sales are in the South region?",
     "SELECT COUNT(*) FROM sales WHERE region = 'South'", [10]),
    ("EAST", "Which region has exactly 30 sales? (HAVING)",
     "SELECT region FROM sales GROUP BY region HAVING COUNT(*) = 30", ["East"]),
    # two regions qualify (South 10, West 8) - the grid wants the 5-letter one
    ("SOUTH", "Which region has less than 11 sales?",
     "SELECT region FROM sales GROUP BY region HAVING COUNT(*) < 11 ORDER BY region", ["South", "West"]),
    # two reps qualify (Omar 10, Liam 8) - the crossing letters decide, LIAM is another clue's answer
    ("OMAR", "Which rep has less than 11 sales?",
     "SELECT rep_name FROM sales GROUP BY rep_name HAVING COUNT(*) < 11 ORDER BY rep_name", ["Liam", "Omar"]),
    ("DANA", "Which rep has the highest number of total sales (by count)?",
     "SELECT rep_name, COUNT(*) AS n FROM sales GROUP BY rep_name ORDER BY n DESC LIMIT 1", ["Dana"]),
    ("EIGHT", "How many sales did Liam make?",
     "SELECT COUNT(*) FROM sales WHERE rep_name = 'Liam'", [8]),
    ("PHONE", "Which product appears exactly 22 times?",
     "SELECT product FROM sales GROUP BY product HAVING COUNT(*) = 22", ["Phone"]),
    # COUNT(*) counts rows, COUNT(amount) skips NULLs: Tablet has 57 rows but 55 amounts
    ("TABLET", "Which product has fewer non-NULL amounts than total rows? (HAVING)",
     "SELECT product FROM sales GROUP BY product HAVING COUNT(amount) < COUNT(*)", ["Tablet"]),
    ("LAPTOP", "Which product made the most money in total?",
     "SELECT product, SUM(amount) AS total FROM sales GROUP BY product ORDER BY total DESC LIMIT 1", ["Laptop"]),
    ("NOA", "Which rep made the single biggest sale?",
     "SELECT rep_name, amount FROM sales ORDER BY amount DESC LIMIT 1", ["Noa"]),
    # ORDER BY amount ASC alone puts the NULL rows first (Dana) - skip them
    ("LIAM", "Which rep made the single smallest sale?",
     "SELECT rep_name, amount FROM sales WHERE amount IS NOT NULL ORDER BY amount LIMIT 1", ["Liam"]),
    ("WEST", "Which region has the lowest average sale amount?",
     "SELECT region, AVG(amount) AS avg_amount FROM sales GROUP BY region ORDER BY avg_amount LIMIT 1", ["West"]),
    # both conditions: region AND product (without the product filter you get 52, all North sales)
    ("FIVE", "How many Laptop sales are in the North region?",
     "SELECT COUNT(*) FROM sales WHERE region = 'North' AND product = 'Laptop'", [5]),
]

db.DB_PATH = "crossword.db"
if os.path.exists(db.DB_PATH):
    os.remove(db.DB_PATH)  # rebuilt on every run
conn = sqlite3.connect(db.DB_PATH)
conn.executescript(INIT_SQL)  # many statements in one go (run_update_query runs only one)
conn.close()

for word, clue, sql, expected in CLUES:
    rows = run_query_select(sql)
    first_column = [list(row.values())[0] for row in rows]
    print(f"{word:7} {clue}\n        {sql}\n        -> {rows}")
    assert first_column == expected, (word, first_column)

print(f"\nALL {len(CLUES)} CLUES CHECKED")
