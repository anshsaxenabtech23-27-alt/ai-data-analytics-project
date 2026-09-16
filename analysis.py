import pandas as pd
from db_connection import conn
query = "SELECT p.product_name, SUM(o.quantity) AS total_sold " \
"FROM Orders o JOIN Products p ON o.product_id = p.product_id GROUP BY p.product_name;"
df = pd.read_sql(query, conn)  
print(df)
