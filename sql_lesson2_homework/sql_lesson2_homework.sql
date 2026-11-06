-- SQL Lesson 2 (12.10.2026) - Homework: PETS
-- DB Browser for SQLite: Execute SQL -> paste -> F5. To see one query's result, select it and press Ctrl+Return.
-- Table name in lowercase: Itay said lowercase names are the common style (SQLite treats PETS and pets as the same).

DROP TABLE IF EXISTS pets;  -- so the script can be run again from the top

-- 1) the table
CREATE TABLE pets (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  type TEXT,
  age INTEGER
);

-- 2) the 4 pets
INSERT INTO pets (id, name, type, age) VALUES
  (1, 'Rex', 'Dog', 3),
  (2, 'Milo', 'Cat', 5),
  (3, 'Coco', 'Parrot', 1),
  (4, 'Luna', 'Cat', 2);

-- 3) every pet, all columns -> 4 rows
SELECT * FROM pets;

-- 4) Rex had a birthday: he is 4 now
UPDATE pets SET age = 4 WHERE name = 'Rex';

-- 5) only the cats -> Milo (5), Luna (2)
SELECT * FROM pets WHERE type = 'Cat';

-- 6) Coco was given away
DELETE FROM pets WHERE name = 'Coco';

-- 7) every pet that is left had a birthday: +1 for all, so no WHERE
UPDATE pets SET age = age + 1;

-- check: Rex 5, Milo 6, Luna 3
SELECT * FROM pets;
