import sqlite3, os

DB = "DBcomputer_store.db"
if os.path.exists(DB):
    os.remove(DB)
conn = sqlite3.connect(DB)
cur = conn.cursor()


def run(title, sql, params=()):
    print(f"\n>> {title}")
    cur.execute(sql, params)
    if sql.strip().upper().startswith("SELECT"):
        rows = cur.fetchall()
        for r in rows:
            print(r)
        if not rows:
            print("(نتیجه‌ای یافت نشد)")
    else:
        conn.commit()
        print(f"تعداد رکورد تغییر یافته: {cur.rowcount}")


cur.executescript("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY, name TEXT NOT NULL,
    category TEXT NOT NULL, price REAL NOT NULL, stock INTEGER NOT NULL
);
CREATE TABLE customers (
    id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
    phone TEXT, city TEXT
);
CREATE TABLE employees (
    id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
    position TEXT, salary REAL NOT NULL
);
""")

products = [
    (1, "Intel Core i3-12100", "CPU", 4500000, 22),
    (2, "Intel Core i5-13400F", "CPU", 7200000, 18),
    (3, "AMD Ryzen 7 7800X3D", "CPU", 23500000, 3),
    (4, "NVIDIA RTX 4060 Ti", "GPU", 19800000, 12),
    (5, "NVIDIA RTX 4070", "GPU", 32000000, 6),
    (6, "NVIDIA RTX 4090", "GPU", 68000000, 1),
    (7, "Corsair Vengeance 16GB", "RAM", 2100000, 30),
    (8, "Kingston Fury 32GB", "RAM", 4300000, 25),
    (9, "Samsung 970 EVO 1TB", "SSD", 3600000, 2),
    (10, "WD Black SN850 1TB", "SSD", 4900000, 9),
    (11, "ASUS ROG STRIX B650", "Motherboard", 11200000, 7),
    (12, "Gigabyte B760M", "Motherboard", 6700000, 14),
]
customers = [
    (1, "Ali", "Rezaei", "09121111111", "Tehran"),
    (2, "Sara", "Ahmadi", "09121111112", "Tehran"),
    (3, "Mohammad", "Karimi", "09121111113", "Tehran"),
    (4, "Fatemeh", "Hosseini", "09121111114", "Isfahan"),
    (5, "Reza", "Jafari", "09121111115", "Isfahan"),
    (6, "Zahra", "Moradi", "09121111116", "Shiraz"),
    (7, "Hossein", "Ghasemi", "09121111117", "Shiraz"),
    (8, "Narges", "Sadeghi", "09121111118", "Mashhad"),
    (9, "Amir", "Hashemi", "09121111119", "Tabriz"),
    (10, "Leila", "Norouzi", "09121111120", "Qom"),
    (11, "Mehdi", "Rostami", None, "Karaj"),
    (12, "Maryam", "Kazemi", "09121111121", None),
]
employees = [
    (1, "Amir", "Mohammadi", "Manager", 45000000),
    (2, "Sara", "Ebrahimi", "Salesperson", 18000000),
    (3, "Reza", "Karimi", "Salesperson", 19500000),
    (4, "Niloofar", "Ahmadi", "Accountant", 25000000),
    (5, "Javad", "Rahimi", "Warehouse", 15000000),
    (6, "Maryam", "Sadeghi", "Support", 16500000),
    (7, "Hamid", "Ghorbani", "Salesperson", 20000000),
    (8, "Fatemeh", "Yousefi", "Accountant", 33000000),
    (9, "Ali", "Fallahi", "Warehouse", 14000000),
    (10, "Zohreh", "Moradi", "Support", 38000000),
    (11, "Kaveh", "Naderi", "Manager", 50000000),
    (12, "Somayeh", "Karbasi", None, 22000000),
]
cur.executemany("INSERT INTO products VALUES (?,?,?,?,?)", products)
cur.executemany("INSERT INTO customers VALUES (?,?,?,?,?)", customers)
cur.executemany("INSERT INTO employees VALUES (?,?,?,?,?)", employees)
conn.commit()

queries = [
    ("همه محصولات", "SELECT * FROM products"),
    ("فقط نام و قیمت", "SELECT name, price FROM products"),
    ("دسته‌بندی‌ها بدون تکرار", "SELECT DISTINCT category FROM products"),
    ("قیمت بیشتر از ۱۰ میلیون", "SELECT * FROM products WHERE price > 10000000"),
    ("موجودی کمتر از ۵", "SELECT * FROM products WHERE stock < 5"),
    ("فقط دسته GPU", "SELECT * FROM products WHERE category='GPU'"),
    (
        "قیمت بین ۱۰ تا ۳۰ میلیون",
        "SELECT * FROM products WHERE price BETWEEN 10000000 AND 30000000",
    ),
    ("نام شامل RTX", "SELECT * FROM products WHERE name LIKE '%RTX%'"),
    ("مرتب‌سازی قیمت نزولی", "SELECT * FROM products ORDER BY price DESC"),
    ("۳ محصول گران‌قیمت", "SELECT * FROM products ORDER BY price DESC LIMIT 3"),
    ("همه مشتریان", "SELECT * FROM customers"),
    ("مشتریان ساکن تهران", "SELECT * FROM customers WHERE city='Tehran'"),
    (
        "مشتریان اصفهان یا شیراز",
        "SELECT * FROM customers WHERE city IN ('Isfahan','Shiraz')",
    ),
    ("شهرها بدون تکرار", "SELECT DISTINCT city FROM customers"),
    ("مرتب بر اساس نام خانوادگی", "SELECT * FROM customers ORDER BY last_name"),
    ("۵ مشتری اول", "SELECT * FROM customers LIMIT 5"),
    ("همه کارکنان", "SELECT * FROM employees"),
    ("حقوق بیشتر از ۳۰ میلیون", "SELECT * FROM employees WHERE salary > 30000000"),
    ("سمت Manager", "SELECT * FROM employees WHERE position='Manager'"),
    ("مرتب بر اساس حقوق نزولی", "SELECT * FROM employees ORDER BY salary DESC"),
    ("۳ کارمند پردرآمد", "SELECT * FROM employees ORDER BY salary DESC LIMIT 3"),
    (
        "افزایش ۱۰٪ قیمت دسته RAM",
        "UPDATE products SET price = price*1.1 WHERE category='RAM'",
    ),
    (
        "افزایش ۵ واحد موجودی محصول id=9",
        "UPDATE products SET stock = stock+5 WHERE id=9",
    ),
    ("تغییر شهر مشتری id=9", "UPDATE customers SET city='Isfahan' WHERE id=9"),
    (
        "افزایش ۵٪ حقوق Salesperson ها",
        "UPDATE employees SET salary = salary*1.05 WHERE position='Salesperson'",
    ),
    (
        "تعیین سمت برای کارمند بدون سمت",
        "UPDATE employees SET position='Support' WHERE id=12",
    ),
    (
        "درج محصول آزمایشی برای تست DELETE",
        "INSERT INTO products VALUES (101,'Test Item','GPU',500000,0)",
    ),
    ("حذف محصولی با موجودی صفر", "DELETE FROM products WHERE stock=0"),
    ("تعداد کل محصولات", "SELECT COUNT(*) AS total FROM products"),
    ("میانگین قیمت محصولات", "SELECT AVG(price) AS avg_price FROM products"),
    (
        "گران‌ترین و ارزان‌ترین قیمت",
        "SELECT MAX(price) AS max_p, MIN(price) AS min_p FROM products",
    ),
    ("مجموع حقوق کارکنان", "SELECT SUM(salary) AS total_salary FROM employees"),
    (
        "تعداد مشتریان هر شهر",
        "SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city",
    ),
    (
        "میانگین قیمت هر دسته",
        "SELECT category, AVG(price) AS avg_price FROM products GROUP BY category",
    ),
    (
        "دسته‌های با میانگین قیمت بالای ۱۵ میلیون",
        "SELECT category, AVG(price) AS avg_price FROM products GROUP BY category HAVING avg_price>15000000",
    ),
    (
        "میانگین حقوق هر سمت",
        "SELECT position, AVG(salary) AS avg_salary FROM employees GROUP BY position",
    ),
    (
        "شهرهای با حداقل ۲ مشتری",
        "SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city HAVING cnt>=2",
    ),
    ("نام محصولات با حروف بزرگ", "SELECT UPPER(name) FROM products"),
    (
        "نام کامل مشتری در یک ستون",
        "SELECT first_name || ' ' || last_name AS full_name FROM customers",
    ),
    ("گرد کردن قیمت محصولات", "SELECT name, ROUND(price) FROM products"),
    (
        "ارزش موجودی هر محصول",
        "SELECT name, price*stock AS inventory_value FROM products",
    ),
    (
        "حقوق سالانه کارکنان",
        "SELECT first_name||' '||last_name AS full_name, salary*12 AS annual_salary FROM employees",
    ),
    (
        "مشتریان با شماره یا شهر NULL",
        "SELECT * FROM customers WHERE phone IS NULL OR city IS NULL",
    ),
    (
        "کارکنان با حقوق بیشتر از میانگین",
        "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)",
    ),
    (
        "محصولات گران‌تر از میانگین قیمت",
        "SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products)",
    ),
    (
        "شهر با بیشترین تعداد مشتری",
        "SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city ORDER BY cnt DESC LIMIT 1",
    ),
]

for title, sql in queries:
    run(title, sql)

print("\n--- سناریوی کامل CRUD ---")
run(
    "Create: محصول جدید",
    "INSERT INTO products VALUES (401,'Logitech G Pro Mouse','GPU',3200000,10)",
)
run("Read: محصول جدید", "SELECT * FROM products WHERE id=401")
run("Update: تغییر قیمت محصول جدید", "UPDATE products SET price=3450000 WHERE id=401")
run("Read بعد از Update", "SELECT * FROM products WHERE id=401")
run("Delete: حذف محصول جدید", "DELETE FROM products WHERE id=401")
run("Read بعد از Delete (باید خالی باشد)", "SELECT * FROM products WHERE id=401")

print("\n--- گزارش نهایی ---")
report = [
    ("تعداد کل محصولات", "SELECT COUNT(*) FROM products"),
    ("گران‌ترین محصول", "SELECT * FROM products ORDER BY price DESC LIMIT 1"),
    ("ارزش کل موجودی فروشگاه", "SELECT SUM(price*stock) FROM products"),
    ("تعداد کل مشتریان", "SELECT COUNT(*) FROM customers"),
    (
        "شهر با بیشترین مشتری",
        "SELECT city, COUNT(*) AS cnt FROM customers GROUP BY city ORDER BY cnt DESC LIMIT 1",
    ),
    ("تعداد کل کارکنان", "SELECT COUNT(*) FROM employees"),
    ("میانگین حقوق کارکنان", "SELECT AVG(salary) FROM employees"),
    (
        "کارکنان با حقوق بالاتر از میانگین",
        "SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees)",
    ),
]
for title, sql in report:
    run(title, sql)

conn.close()
print("\nپایگاه داده در فایل زیر ذخیره شد:", os.path.abspath(DB))
