import sqlite3

db = sqlite3.connect('store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('База данных подключена!')

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    product_id TEXT,
    photo TEXT
    )
""")


async def sql_insert_store(name_product, category, size, price, product_id, photo):
    cursor.execute("""
    INSERT INTO products (name_product, categoty, size, price, product_id, photo)
    VALUES (?, ?, ?, ?, ?, ?)
""", (name_product, category, size, price, product_id, photo))
    db.commit()


def get_db_connection():
    conn = sqlite3.connect('store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""select * from products""").fetchall()
    print(products)
    conn.close()
    return products