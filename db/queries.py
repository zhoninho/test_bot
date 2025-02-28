CREATE_TABLE_products = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_product TEXT,
    size TEXT,
    price TEXT,
    product_id TEXT,
    photo TEXT
    )
"""

INSERT_products_query = """
    INSERT INTO products (name_product, price, size, product_id, photo)
    VALUES (?, ?, ?, ?, ?)
"""

FETCH_ALL_PRODUCTS_QUERY = """
    SELECT * FROM store
"""