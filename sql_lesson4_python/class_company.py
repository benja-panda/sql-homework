"""Lesson 29 class exercises (22.10), with the class db.py.
1) The COMPANY table from the SQLite booklet (p.26 CREATE, p.29 INSERTs) + 3 SELECTs.
2) Rename a row and delete a row by id, both taken from input().
   Bonus: delete only if the id exists.
Spec: the messages Itay sent to the class group (22.10)."""
from db import run_query_select, run_update_query

# start clean: the ids are fixed, so a second run would fail with "UNIQUE constraint failed: COMPANY.ID"
run_update_query("DROP TABLE IF EXISTS COMPANY")
run_update_query("""CREATE TABLE IF NOT EXISTS COMPANY (
    ID      INT PRIMARY KEY NOT NULL,
    NAME    TEXT NOT NULL,
    AGE     INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY  REAL)""")

insert_query = "INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?, ?)"  # 5 columns = 5 ?
run_update_query(insert_query, (1, "Paul", 32, "California", 20000.00))
run_update_query(insert_query, (2, "Allen", 25, "Texas", 15000.00))
run_update_query(insert_query, (3, "Teddy", 23, "Norway", 20000.00))
run_update_query(insert_query, (4, "Mark", 25, "Rich-Mond", 65000.00))
run_update_query(insert_query, (5, "David", 27, "Texas", 85000.00))
run_update_query(insert_query, (6, "Kim", 22, "South-Hall", 45000.00))
run_update_query(insert_query, (7, "James", 24, "Houston", 10000.00))


def show(title, rows):
    print(title)
    for row in rows:  # one dict per line, like the class example
        print("  ", row)


show("All rows:", run_query_select("SELECT * FROM COMPANY"))
show("SALARY > 30000:", run_query_select("SELECT * FROM COMPANY WHERE SALARY > ?", (30000,)))
show("NAME starts with D:", run_query_select("SELECT * FROM COMPANY WHERE NAME LIKE ?", ("D%",)))

# 2) update: the id and the new name come from the user -> they go in params, never inside the SQL text
company_id = int(input("ID to rename: "))  # input() returns text; int() fails on a word (ValueError)
new_name = input("New name: ")
run_update_query("UPDATE COMPANY SET NAME = ? WHERE ID = ?", (new_name, company_id))

# Bonus: DELETE of a missing id is not an error, it just deletes nothing - so look first
delete_id = int(input("ID to delete: "))
if run_query_select("SELECT ID FROM COMPANY WHERE ID = ?", (delete_id,)):  # no row -> [] -> False
    run_update_query("DELETE FROM COMPANY WHERE ID = ?", (delete_id,))
    print(f"ID {delete_id} deleted")
else:
    print("user not exist")

show("After update and delete:", run_query_select("SELECT * FROM COMPANY"))
