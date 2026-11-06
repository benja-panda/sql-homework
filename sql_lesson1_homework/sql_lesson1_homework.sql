-- SQL Lesson 1 (08.10.2026) - Homework: STUDENTS
-- DB Browser for SQLite: Execute SQL -> paste -> F5. To see one query's result, select it and press Ctrl+Return.

DROP TABLE IF EXISTS STUDENTS;  -- so the script can be run again from the top

-- 1) the table and its rules
CREATE TABLE STUDENTS (
  ID INT PRIMARY KEY,        -- each student's number: unique
  NAME TEXT NOT NULL,        -- required
  AGE INT,
  CITY TEXT,
  GRADE REAL NOT NULL        -- required, can have decimals (92.5)
);

-- 2) exactly the 4 students from the table
INSERT INTO STUDENTS (ID, NAME, AGE, CITY, GRADE) VALUES
  (1, 'Noa', 15, 'Tel Aviv', 92.5),
  (2, 'Liam', 16, 'Haifa', 88.0),
  (3, 'Maya', 15, 'Netanya', 95.0),
  (4, 'Omer', 17, 'Jerusalem', 81.5);

-- 3.1) all students, all details -> 4 rows
SELECT * FROM STUDENTS;

-- 3.2) every student's name and grade
SELECT NAME, GRADE FROM STUDENTS;

-- 3.3) students who got a grade above 90 -> Noa (92.5), Maya (95.0)
SELECT * FROM STUDENTS WHERE GRADE > 90;

-- 3.4) students whose name starts with M -> Maya
SELECT * FROM STUDENTS WHERE NAME LIKE 'M%';

-- 4) finally remove the table
DROP TABLE STUDENTS;
