-- hw17 חלק 1: עבודה עם שאילתות (ecommerce1.db, 5.11.2026) - Benjamin Anzel
-- פותחים ב-DB Browser: Open Database -> ecommerce1.db -> Execute SQL -> מסמנים שאילתה -> F5
-- שמות עמודות עם רווח כותבים בגרשיים כפולים: "Customer ID", "Total Spend"

-- 1. כמה לקוחות יש בטבלה?
SELECT COUNT(*) AS customers FROM ecomm;
-- תשובה: 350

-- 2. מהו גיל הלקוח הממוצע?
SELECT ROUND(AVG(Age), 2) AS avg_age FROM ecomm;
-- תשובה: 33.6

-- 3. כמה לקוחות גברים יש? וכמה נשים?
SELECT Gender, COUNT(*) AS customers FROM ecomm GROUP BY Gender;
-- תשובה: Female 175, Male 175

-- 4. כמה מוצרים בממוצע רוכשים הגברים? כמה הנשים?
SELECT Gender, ROUND(AVG("Items Purchased"), 2) AS avg_items FROM ecomm GROUP BY Gender;
-- תשובה: Female 10.76, Male 14.44

-- 5. כמה סוגי membership קיימים בטבלה?
SELECT COUNT(DISTINCT "Membership Type") AS membership_types FROM ecomm;
-- תשובה: 3

-- 6. כמה חברים יש בכל סוג של membership?
SELECT "Membership Type", COUNT(*) AS members FROM ecomm GROUP BY "Membership Type";
-- תשובה: Bronze 116, Gold 117, Silver 117

-- 7. כמה לקוחות גרים ב-New York?
SELECT COUNT(*) AS new_york_customers FROM ecomm WHERE City = 'New York';
-- תשובה: 59

-- 8. כמה לקוחות יש בכל עיר (בסדר יורד מהגדול לקטן)?
SELECT City, COUNT(*) AS customers FROM ecomm GROUP BY City ORDER BY customers DESC;
-- תשובה: New York 59, Los Angeles 59, ואחריהן San Francisco, Miami, Houston, Chicago עם 58 כל אחת

-- 9. כמה סה"כ שילמו הגברים (Total Spend)? כמה הנשים?
SELECT Gender, ROUND(SUM("Total Spend"), 2) AS total_spend FROM ecomm GROUP BY Gender;
-- תשובה: Female 123,170.00, Male 172,713.60

-- 10. מי הלקוח שקנה הכי הרבה מוצרים? מי הלקוח שקנה הכי פחות מוצרים?
-- (= MAX / = MIN ולא LIMIT 1: יש תיקו, ו-LIMIT 1 היה מראה רק לקוח אחד)
SELECT "Customer ID", Gender, City, "Items Purchased" FROM ecomm
WHERE "Items Purchased" = (SELECT MAX("Items Purchased") FROM ecomm);
SELECT "Customer ID", Gender, City, "Items Purchased" FROM ecomm
WHERE "Items Purchased" = (SELECT MIN("Items Purchased") FROM ecomm);
-- תשובה: הכי הרבה 21 מוצרים - תיקו של 24 לקוחות (כולם גברים מ-San Francisco, למשל 110, 128, 146);
--        הכי פחות 7 מוצרים - תיקו של 25 לקוחות (כולן נשים מ-Houston, למשל 112, 124, 142)
