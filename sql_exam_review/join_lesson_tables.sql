-- טבלאות התרגול של שיעור ה-JOIN (29.10). להריץ ב-DB Browser ואז לפתור את התרגילים.
CREATE TABLE departments (id INTEGER PRIMARY KEY, dept_name TEXT NOT NULL, budget REAL NOT NULL);
INSERT INTO departments VALUES (1,'Engineering',150000),(2,'Marketing',80000),(3,'Sales',60000),(4,'HR',45000);
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT NOT NULL, dept_id INTEGER, salary REAL NOT NULL,
 FOREIGN KEY (dept_id) REFERENCES departments(id));
INSERT INTO employees VALUES (1,'Dana',1,9000),(2,'Omar',2,7200),(3,'Noa',1,6800),(4,'Liam',3,5500),(5,'Rina',NULL,6000),(6,'Kai',2,7000);
CREATE TABLE cars (id INTEGER PRIMARY KEY, model TEXT NOT NULL, price REAL NOT NULL);
INSERT INTO cars VALUES (1,'Toyota Corolla',22000),(2,'Honda Civic',24000),(3,'Ford Focus',19000),(4,'Tesla Model 3',42000);
CREATE TABLE drivers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, car_id INTEGER, FOREIGN KEY (car_id) REFERENCES cars(id));
INSERT INTO drivers VALUES (1,'Dana',1),(2,'Omar',2),(3,'Noa',NULL),(4,'Liam',3),(5,'Rina',NULL);
CREATE TABLE Pastries (PastryName VARCHAR(50)); CREATE TABLE Toppings (ToppingName VARCHAR(50));
INSERT INTO Pastries VALUES ('Croissant'),('Muffin'),('Donut');
INSERT INTO Toppings VALUES ('Chocolate'),('Glaze'),('Sprinkles'),('Caramel');
CREATE TABLE Baristas (Name VARCHAR(50), HourlyRate DECIMAL(10,2)); CREATE TABLE Shifts (ShiftType VARCHAR(20), Income DECIMAL(10,2));
INSERT INTO Baristas VALUES ('Alice',18),('Bob',22),('Charlie',15),('Diana',25);
INSERT INTO Shifts VALUES ('Morning',95),('Afternoon',85),('Evening',70);
CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL);
INSERT INTO customers VALUES (1,'Alice','alice@mail.com'),(2,'Bob','bob@mail.com'),(3,'Carol','carol@mail.com'),(4,'Dan','dan@mail.com'),(5,'Eva','eva@mail.com'),(6,'Frank','frank@mail.com');
CREATE TABLE products (id INTEGER PRIMARY KEY, product_name TEXT NOT NULL, price REAL NOT NULL, category TEXT NOT NULL);
INSERT INTO products VALUES (1,'Wireless Mouse',29.99,'Electronics'),(2,'USB-C Hub',49.99,'Electronics'),(3,'Notebook',5.99,'Stationery'),(4,'Gel Pen Set',8.49,'Stationery'),(5,'Desk Lamp',34.99,'Furniture'),(6,'Whiteboard',59.99,'Furniture'),(7,'Coffee Mug',12.99,'Kitchen'),(8,'Water Bottle',18.99,'Kitchen'),(9,'Backpack',74.99,'Bags'),(10,'Tote Bag',22.99,'Bags'),(11,'Keyboard',89.99,'Electronics');
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER NOT NULL, product_id INTEGER NOT NULL, quantity INTEGER NOT NULL, order_date TEXT NOT NULL,
 FOREIGN KEY (customer_id) REFERENCES customers(id), FOREIGN KEY (product_id) REFERENCES products(id));
INSERT INTO orders VALUES (1,1,3,2,'2024-01-05'),(2,1,7,1,'2024-01-18'),(3,2,1,3,'2024-02-02'),(4,2,10,1,'2024-02-14'),(5,3,5,2,'2024-03-01'),(6,4,2,1,'2024-03-15'),(7,4,8,4,'2024-03-22'),(8,1,4,1,'2024-04-10'),(9,5,6,2,'2024-04-18');
