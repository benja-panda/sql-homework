-- SQL Lesson 3 (15.10.2026) - Homework: Constraints, Auto Increment, Foreign Key
-- DB Browser for SQLite: New Database -> Execute SQL -> paste this file -> Execute all (F5) -> Write Changes (Ctrl+S).
-- DB Browser shows only the LAST result: to see one query's result, select just that query and press Ctrl+Return.

PRAGMA foreign_keys = ON;  -- SQLite enforces FOREIGN KEY rules only when this is on

-- so the script can be run again from the top (child table before its parent)
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS help_requests;
DROP TABLE IF EXISTS class_signups;


-- ===================== Homework 1: Constraints - class_signups =====================
CREATE TABLE class_signups (
  id INTEGER PRIMARY KEY,                       -- main ID: unique and not empty
  contact_email TEXT NOT NULL UNIQUE,           -- required, no two rows with the same email
  participant_name TEXT NOT NULL,               -- required
  fitness_score INTEGER CHECK (fitness_score >= 0 AND fitness_score <= 50),
  payment_status TEXT DEFAULT 'unpaid'          -- no value given -> 'unpaid'
);

INSERT INTO class_signups (id, contact_email, participant_name, fitness_score, payment_status) VALUES
  (1, 'maya@mail.com', 'Maya', 44, 'paid'),
  (2, 'tomer@mail.com', 'Tomer', 29, 'unpaid'),
  (3, 'noa2@mail.com', 'Noa', 38, 'paid'),
  (4, 'liam@mail.com', 'Liam', 47, 'unpaid');

-- Participants who already paid -> Maya (1), Noa (3)
SELECT * FROM class_signups WHERE payment_status = 'paid';

-- Participants whose name ends with the letter "m" -> Liam (4)
SELECT * FROM class_signups WHERE participant_name LIKE '%m';


-- ===================== Homework 2: Auto Increment - help_requests =====================
CREATE TABLE help_requests (
  id INTEGER PRIMARY KEY AUTOINCREMENT,         -- generated automatically, always moves forward
  visitor_name TEXT NOT NULL,                   -- required
  urgency_level TEXT,                           -- urgent / normal / low
  wait_minutes INTEGER
);

-- no id values typed: SQLite gives 1, 2, 3, 4
INSERT INTO help_requests (visitor_name, urgency_level, wait_minutes) VALUES ('Yael', 'urgent', 12);
INSERT INTO help_requests (visitor_name, urgency_level, wait_minutes) VALUES ('Avi', 'normal', 45);
INSERT INTO help_requests (visitor_name, urgency_level, wait_minutes) VALUES ('Roni', 'urgent', 8);
INSERT INTO help_requests (visitor_name, urgency_level, wait_minutes) VALUES ('Tal', 'low', 60);

-- Urgent requests -> Yael (1), Roni (3)
SELECT * FROM help_requests WHERE urgency_level = 'urgent';

-- Delete the last row (Tal, id 4), add one more visitor, and check the id
DELETE FROM help_requests WHERE id = 4;
INSERT INTO help_requests (visitor_name, urgency_level, wait_minutes) VALUES ('Shira', 'normal', 20);

-- Shira got id 5, not 4: with AUTOINCREMENT a deleted id is never reused
SELECT * FROM help_requests;


-- ===================== Homework 3: Foreign Key - authors and books =====================
CREATE TABLE authors (                          -- parent table
  id INTEGER PRIMARY KEY,
  author_name TEXT NOT NULL
);

CREATE TABLE books (                            -- child table: every book points to an existing author
  id INTEGER PRIMARY KEY,
  book_title TEXT NOT NULL,
  author_id INTEGER NOT NULL,
  FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- parents first: a book can only point to an author that already exists
INSERT INTO authors (id, author_name) VALUES (1, 'Agatha Christie');
INSERT INTO authors (id, author_name) VALUES (2, 'Isaac Asimov');
INSERT INTO authors (id, author_name) VALUES (3, 'Yuval Noah Harari');

INSERT INTO books (id, book_title, author_id) VALUES (1, 'Murder on the Orient Express', 1);
INSERT INTO books (id, book_title, author_id) VALUES (2, 'I, Robot', 2);
INSERT INTO books (id, book_title, author_id) VALUES (3, 'Foundation', 2);
INSERT INTO books (id, book_title, author_id) VALUES (4, 'Sapiens', 3);
INSERT INTO books (id, book_title, author_id) VALUES (5, 'And Then There Were None', 1);

-- Books by author 2 (Isaac Asimov) -> I, Robot (2), Foundation (3)
SELECT * FROM books WHERE author_id = 2;

-- Challenge: Agatha Christie's books, found by the author's name with a JOIN
-- -> Murder on the Orient Express (1), And Then There Were None (5)
SELECT b.id, b.book_title, b.author_id
FROM books b
JOIN authors a ON b.author_id = a.id
WHERE a.author_name = 'Agatha Christie';
