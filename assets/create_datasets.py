import pandas as pd
from assets.db import engine 



products = pd.read_csv("olist_products_dataset.csv")
items = pd.read_csv("olist_order_items_dataset.csv")

product_ids = items["product_id"].unique()