# hw17 חלק 1 סעיף 2: תוכנית פייתון שמריצה את השאילתות ומציגה את התשובות - Benjamin Anzel
# הקובץ ecommerce1.db צריך להיות באותה תיקייה כמו התוכנית.
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("ecommerce1.db")

QUESTIONS = [
    ("כמה לקוחות יש בטבלה?",
     "SELECT COUNT(*) FROM ecomm"),
    ("מהו גיל הלקוח הממוצע?",
     "SELECT ROUND(AVG(Age), 2) FROM ecomm"),
    ("כמה לקוחות גברים ונשים יש?",
     "SELECT Gender, COUNT(*) FROM ecomm GROUP BY Gender"),
    ("כמה מוצרים בממוצע רוכשים הגברים והנשים?",
     'SELECT Gender, ROUND(AVG("Items Purchased"), 2) FROM ecomm GROUP BY Gender'),
    ("כמה סוגי membership קיימים?",
     'SELECT COUNT(DISTINCT "Membership Type") FROM ecomm'),
    ("כמה חברים יש בכל סוג membership?",
     'SELECT "Membership Type", COUNT(*) FROM ecomm GROUP BY "Membership Type"'),
    ("כמה לקוחות גרים ב-New York?",
     "SELECT COUNT(*) FROM ecomm WHERE City = ?", ("New York",)),
    ("כמה לקוחות יש בכל עיר (מהגדול לקטן)?",
     "SELECT City, COUNT(*) AS n FROM ecomm GROUP BY City ORDER BY n DESC"),
    ("כמה שילמו בסך הכול הגברים והנשים (Total Spend)?",
     'SELECT Gender, ROUND(SUM("Total Spend"), 2) FROM ecomm GROUP BY Gender'),
    ("מי קנה הכי הרבה מוצרים?",
     'SELECT "Customer ID", Gender, City, "Items Purchased" FROM ecomm '
     'WHERE "Items Purchased" = (SELECT MAX("Items Purchased") FROM ecomm)'),
    ("מי קנה הכי פחות מוצרים?",
     'SELECT "Customer ID", Gender, City, "Items Purchased" FROM ecomm '
     'WHERE "Items Purchased" = (SELECT MIN("Items Purchased") FROM ecomm)'),
]


def run_query(conn, sql, params=()):
    cursor = conn.execute(sql, params)
    return cursor.fetchall()


def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        for number, question in enumerate(QUESTIONS, start=1):
            text, sql = question[0], question[1]
            params = question[2] if len(question) > 2 else ()
            rows = run_query(conn, sql, params)
            print(f"{number}. {text}")
            if len(rows) == 1 and len(rows[0]) == 1:
                print(f"   {rows[0][0]}")
            else:
                for row in rows:
                    print("   " + " | ".join(str(value) for value in row))
            if len(rows) > 1 and "Customer ID" in sql:
                print(f"   (תיקו: {len(rows)} לקוחות)")
            print()
    finally:
        conn.close()


if __name__ == "__main__":
    main()
