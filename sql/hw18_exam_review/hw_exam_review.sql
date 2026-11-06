-- חזרה למבחן - שאילתות (hw18, 2.11.2026) - Benjamin Anzel
-- להריץ הכול ב-DB Browser: New Database -> Execute SQL -> F5 -> Ctrl+S.
-- התשובות שהתקבלו כתובות בהערה מתחת לכל שאילתה.

-- @a. יצירת הטבלאות והקשרים
CREATE TABLE category (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL UNIQUE
);
CREATE TABLE products (
    product_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    price       REAL NOT NULL CHECK (price >= 0),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);
CREATE TABLE nutritions (
    nutrition_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id   INTEGER UNIQUE,          -- UNIQUE = לכל מוצר שורה תזונתית אחת לכל היותר (יחיד ליחיד)
    name         TEXT,
    calories     REAL,
    fats         REAL,
    sugar        REAL,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE TABLE orders (
    order_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time     TEXT NOT NULL,          -- ל-SQLite אין טיפוס DATETIME אמיתי: שומרים טקסט 'YYYY-MM-DD HH:MM'
    address       TEXT,
    customer_name TEXT NOT NULL,
    customer_ph   TEXT,
    total_price   REAL
);
CREATE TABLE products_orders (
    order_id   INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    amount     INTEGER NOT NULL CHECK (amount > 0),
    PRIMARY KEY (order_id, product_id),   -- מפתח ראשי מורכב: אותו מוצר לא יופיע פעמיים באותה הזמנה
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- @b. הקשרים (תשובה מילולית)
-- category -> products        : יחיד לרבים (קטגוריה אחת, הרבה מוצרים, FK בצד של products)
-- products -> nutritions      : יחיד ליחיד (product_id ב-nutritions הוא FK + UNIQUE)
-- orders  <-> products        : רבים לרבים, דרך טבלת הקישור products_orders
--   (orders -> products_orders ו-products -> products_orders הם כל אחד יחיד לרבים)

-- @c. אכלוס (הקובץ inserts.sql מהלינק בתרגיל)
INSERT INTO category (name) VALUES
('Beverages'),
('Snacks'),
('Dairy'),
('Fruits'),
('Vegetables');

INSERT INTO products (name, price, category_id) VALUES
('Orange Juice', 5.99, 1),
('Chocolate Bar', 2.50, 2),
('Milk', 3.20, 3),
('Apple', 1.50, 4),
('Carrot', 0.99, 5),
('Coca Cola', 1.50, 1),    -- Beverages
('Pepsi', 1.40, 1),        -- Beverages
('Water Bottle', 0.99, 1), -- Beverages
('Orange Soda', 1.70, 1),  -- Beverages
('Iced Tea', 2.00, 1),     -- Beverages
('Potato Chips', 1.80, 2),   -- Snacks
('Pretzels', 2.20, 2),       -- Snacks
('Popcorn', 1.99, 2),        -- Snacks
('Granola Bar', 1.50, 2),    -- Snacks
('Cookies', 3.00, 2),        -- Snacks
('Cheese', 4.50, 3),      -- Dairy
('Yogurt', 1.25, 3),      -- Dairy
('Butter', 3.75, 3),      -- Dairy
('Cream Cheese', 2.50, 3),-- Dairy
('Ice Cream', 5.00, 3),   -- Dairy
('Banana', 1.20, 4),      -- Fruits
('Grapes', 2.99, 4),      -- Fruits
('Mango', 1.75, 4),       -- Fruits
('Pineapple', 3.00, 4),   -- Fruits
('Strawberries', 2.80, 4);-- Fruits


INSERT INTO nutritions (product_id, name, calories, fats, sugar) VALUES
(1, 'Orange Juice', 120, 0.2, 20),
(2, 'Chocolate Bar', 220, 12, 18),
(3, 'Milk', 150, 8, 12),
(4, 'Apple', 95, 0.3, 19),
(5, 'Carrot', 41, 0.1, 5),
(6, 'Coca Cola', 140, 0, 39),      -- Coca Cola
(7, 'Pepsi', 150, 0, 41),          -- Pepsi
(8, 'Water Bottle', 0, 0, 0),      -- Water Bottle
(9, 'Orange Soda', 160, 0, 44),    -- Orange Soda
(10, 'Iced Tea', 90, 0, 23),       -- Iced Tea
(11, 'Potato Chips', 160, 10, 1),  -- Potato Chips
(12, 'Pretzels', 110, 1, 1),       -- Pretzels
(13, 'Popcorn', 120, 5, 0),        -- Popcorn
(14, 'Granola Bar', 150, 6, 7),    -- Granola Bar
(15, 'Cookies', 250, 12, 18),      -- Cookies
(16, 'Cheese', 113, 9, 1),         -- Cheese
(17, 'Yogurt', 80, 1.5, 11),       -- Yogurt
(18, 'Butter', 100, 11, 0),        -- Butter
(19, 'Cream Cheese', 99, 10, 1),   -- Cream Cheese
(20, 'Ice Cream', 270, 14, 28),    -- Ice Cream
(21, 'Banana', 105, 0.3, 14),      -- Banana
(22, 'Grapes', 62, 0.3, 15),       -- Grapes
(23, 'Mango', 99, 0.6, 23),        -- Mango
(24, 'Pineapple', 50, 0.1, 10),    -- Pineapple
(25, 'Strawberries', 53, 0.5, 8);  -- Strawberries

INSERT INTO orders (date_time, address, customer_name, customer_ph, total_price) VALUES
('2024-09-17 10:30', '123 Main St', 'John Doe', '555-1234', 30.08),
('2024-09-17 11:45', '456 Oak St', 'Jane Smith', '555-5678', 20.13),
('2024-09-17 12:15', '789 Pine St', 'Emily Davis', '555-8765', 22.22),
('2024-09-17 13:00', '321 Elm St', 'Michael Johnson', '555-4321', 15.15),
('2024-09-17 13:30', '654 Maple St', 'Sarah Wilson', '555-6789', 30.99);

INSERT INTO products_orders (order_id, product_id, amount) VALUES
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(3, 4, 3),
(4, 5, 5),
(5, 1, 1),
(5, 3, 2),
(5, 4, 2),
(1, 6, 3),     -- Coca Cola
(1, 11, 1),    -- Potato Chips
(2, 7, 2),     -- Pepsi
(2, 12, 2),    -- Pretzels
(3, 8, 1),     -- Water Bottle
(3, 13, 2),    -- Popcorn
(4, 9, 1),     -- Orange Soda
(4, 14, 2),    -- Granola Bar
(5, 10, 1),    -- Iced Tea
(5, 15, 1),    -- Cookies
(1, 16, 1),    -- Cheese
(2, 17, 3),    -- Yogurt
(3, 18, 2),    -- Butter
(4, 19, 1),    -- Cream Cheese
(5, 20, 1),    -- Ice Cream
(1, 21, 4),    -- Banana
(2, 22, 2),    -- Grapes
(3, 23, 3),    -- Mango
(4, 24, 1),    -- Pineapple
(5, 25, 2);    -- Strawberries

-- @d-i. כל הפריטים + הערך התזונתי + הקטגוריה
SELECT p.name, c.name AS category, n.calories, n.fats, n.sugar
FROM products p
JOIN category c        ON p.category_id = c.category_id
LEFT JOIN nutritions n ON n.product_id = p.product_id   -- LEFT: גם מוצר בלי ערך תזונתי יופיע
ORDER BY c.name, p.name;

-- @d-ii. כל ההזמנות, ובכל הזמנה כל פרטי המוצר
SELECT o.order_id, o.customer_name, p.product_id, p.name, p.price, po.amount
FROM orders o
JOIN products_orders po ON po.order_id = o.order_id
JOIN products p         ON p.product_id = po.product_id
ORDER BY o.order_id, p.product_id;

-- @d-iii. מוסיפים מוצר אחד לכל הזמנה (מוצר שעוד לא נמצא בה, אחרת ה-PK המורכב יחזיר שגיאה)
INSERT INTO products_orders (order_id, product_id, amount) VALUES
(1, 5, 1),   -- Carrot
(2, 5, 1),
(3, 5, 1),
(4, 3, 1),   -- להזמנה 4 כבר יש Carrot, אז Milk
(5, 5, 1);
SELECT order_id, COUNT(*) AS products FROM products_orders GROUP BY order_id;

-- @d-iv. מעדכנים את המחיר הכולל של כל הזמנה = סכום (כמות X מחיר המוצר)
UPDATE orders
SET total_price = (
    SELECT SUM(po.amount * p.price)
    FROM products_orders po
    JOIN products p ON p.product_id = po.product_id
    WHERE po.order_id = orders.order_id      -- תת-שאילתה מתואמת: רצה פעם אחת לכל הזמנה
);
SELECT order_id, customer_name, ROUND(total_price, 2) AS total_price FROM orders;
-- תשובה: 1 = 31.07, 2 = 21.12, 3 = 23.21, 4 = 18.35, 5 = 31.98

-- @d-v. ההזמנה הכי יקרה, הכי זולה, ממוצע
SELECT ROUND(MAX(total_price), 2) AS most_expensive,
       ROUND(MIN(total_price), 2) AS cheapest,
       ROUND(AVG(total_price), 2) AS average
FROM orders;
SELECT order_id, customer_name, ROUND(total_price, 2) AS total_price
FROM orders WHERE total_price = (SELECT MAX(total_price) FROM orders);
SELECT order_id, customer_name, ROUND(total_price, 2) AS total_price
FROM orders WHERE total_price = (SELECT MIN(total_price) FROM orders);
-- תשובה: הכי יקרה הזמנה 5 (Sarah Wilson) 31.98, הכי זולה הזמנה 4 (Michael Johnson) 18.35, ממוצע 25.15

-- @d-vi. הלקוח שהזמין הכי הרבה פעמים
-- (HAVING = MAX ולא LIMIT 1, כדי שבמקרה של תיקו יופיעו כל הלקוחות)
SELECT customer_name, COUNT(*) AS orders_count
FROM orders
GROUP BY customer_name
HAVING COUNT(*) = (SELECT MAX(cnt) FROM (SELECT COUNT(*) AS cnt FROM orders GROUP BY customer_name));
-- תשובה: תיקו - כל 5 הלקוחות הזמינו פעם אחת

-- @d-vii. המוצר שנמכר הכי הרבה / הכי פחות (לפי כמות יחידות), וממוצע
SELECT p.name, SUM(po.amount) AS units
FROM products p
JOIN products_orders po ON po.product_id = p.product_id
GROUP BY p.product_id
HAVING SUM(po.amount) = (SELECT MAX(units) FROM (SELECT SUM(amount) AS units FROM products_orders GROUP BY product_id));
SELECT p.name, SUM(po.amount) AS units
FROM products p
JOIN products_orders po ON po.product_id = p.product_id
GROUP BY p.product_id
HAVING SUM(po.amount) = (SELECT MIN(units) FROM (SELECT SUM(amount) AS units FROM products_orders GROUP BY product_id));
SELECT ROUND(AVG(units), 2) AS avg_units_per_product
FROM (SELECT SUM(amount) AS units FROM products_orders GROUP BY product_id);
-- תשובה: הכי הרבה Carrot (9 יחידות); הכי פחות: תיקו של 10 מוצרים עם יחידה אחת
--        (Chocolate Bar, Water Bottle, Orange Soda, Iced Tea, Potato Chips, Cookies, Cheese, Cream Cheese, Ice Cream, Pineapple);
--        ממוצע 2.32 יחידות למוצר (58 יחידות / 25 מוצרים, כולם נמכרו)

-- @d-viii. איזו קטגוריה נמכרת הכי הרבה / הכי פחות
SELECT c.name AS category, SUM(po.amount) AS units
FROM products_orders po
JOIN products p ON p.product_id = po.product_id
JOIN category c ON c.category_id = p.category_id
GROUP BY c.category_id
ORDER BY units DESC;
-- תשובה: הכי הרבה Fruits (17); הכי פחות: תיקו בין Vegetables ו-Snacks (9 כל אחת)

-- @d-ix. בונוס: המוצר שמופיע בהכי הרבה הזמנות שונות
SELECT p.name, COUNT(DISTINCT po.order_id) AS orders_count
FROM products p
JOIN products_orders po ON po.product_id = p.product_id
GROUP BY p.product_id
HAVING COUNT(DISTINCT po.order_id) = (SELECT MAX(cnt) FROM (SELECT COUNT(DISTINCT order_id) AS cnt FROM products_orders GROUP BY product_id));
-- תשובה: Carrot, ב-5 הזמנות שונות
