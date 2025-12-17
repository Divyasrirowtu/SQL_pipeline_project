import duckdb

con = duckdb.connect("pipeline.duckdb")

# ---- Drop tables if exist ----
con.execute("""
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
""")

# ---- Create tables ----
con.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    created_at TIMESTAMP,
    country VARCHAR
);
""")

con.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name VARCHAR,
    category VARCHAR,
    price DECIMAL,
    created_at TIMESTAMP
);
""")

con.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER,
    total_amount DECIMAL,
    order_date TIMESTAMP
);
""")

# ---- Load CSVs ----
con.execute("COPY users FROM 'data/users.csv' (HEADER, AUTO_DETECT TRUE);")
con.execute("COPY products FROM 'data/products.csv' (HEADER, AUTO_DETECT TRUE);")
con.execute("COPY orders FROM 'data/orders.csv' (HEADER, AUTO_DETECT TRUE);")

print("Data loaded into DuckDB successfully!")
