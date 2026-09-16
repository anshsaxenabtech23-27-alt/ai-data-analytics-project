import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from db_connection import conn
from analysis import df
# Top Selling Products
plt.figure(figsize=(8,5))
sns.barplot(x="product_name", y="total_sold", data=df, palette="viridis")
plt.title("Top Selling Products")
plt.xticks(rotation=45)
plt.show()
# Monthly Revenue Trend
query2 = "SELECT MONTH(order_date) AS month, SUM(p.price * o.quantity) AS revenue FROM Orders o JOIN Products p ON o.product_id = p.product_id GROUP BY MONTH(order_date);"
df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(8,5))
sns.lineplot(x="month", y="revenue", data=df2, marker="o", color="red")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# customer order count
query3 = "SELECT c.name, COUNT(o.order_id) AS total_orders FROM Customers c JOIN Orders o ON c.customer_id = o.customer_id GROUP BY c.name;"
df3 = pd.read_sql(query3, conn)

plt.figure(figsize=(8,5))
sns.barplot(x="name", y="total_orders", data=df3, palette="coolwarm")
plt.title("Customer Orders Count")
plt.xticks(rotation=45)
plt.show()
