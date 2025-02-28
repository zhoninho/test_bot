import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_products)


async def sql_insert_store(name_product, price, size, product_id, photo):
    cursor.execute(queries.INSERT_products_query,
                   (name_product, size, price, product_id, photo))
    db.commit()


def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""select * from products""").fetchall()
    conn.close()
    return products