from faker import Faker
import pandas as pd
import random

fake = Faker()
NUM_ROWS = 50000

# ---- Users ----
users = [{
    "user_id": i,
    "name": fake.name(),
    "email": fake.email(),
    "created_at": fake.date_time_this_decade(),
    "country": fake.country()
} for i in range(1, NUM_ROWS + 1)]

pd.DataFrame(users).to_csv("data/users.csv", index=False)

# ---- Products ----
categories = ["Electronics", "Clothing", "Books", "Toys", "Home"]
products = [{
    "product_id": i,
    "name": fake.word(),
    "category": random.choice(categories),
    "price": round(random.uniform(5, 500), 2),
    "created_at": fake.date_time_this_decade()
} for i in range(1, NUM_ROWS + 1)]

pd.DataFrame(products).to_csv("data/products.csv", index=False)

# ---- Orders ----
orders = [{
    "order_id": i,
    "user_id": random.randint(1, NUM_ROWS),
    "product_id": random.randint(1, NUM_ROWS),
    "quantity": random.randint(1, 5),
    "total_amount": 0,  # will calculate below
    "order_date": fake.date_time_this_year()
} for i in range(1, NUM_ROWS + 1)]

# Calculate total_amount
product_prices = pd.DataFrame(products).set_index('product_id')['price'].to_dict()
for order in orders:
    order['total_amount'] = round(order['quantity'] * product_prices[order['product_id']], 2)

pd.DataFrame(orders).to_csv("data/orders.csv", index=False)

print("Data generated successfully!")
