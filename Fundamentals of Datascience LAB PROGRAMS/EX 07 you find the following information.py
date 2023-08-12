import pandas as pd
order_data = pd.read_csv("C:/Users/koppo/OneDrive/Documents/order_data.csv")
total_orders_per_customer = order_data.groupby('customer_id')['order_date'].count()
average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Total Orders per Customer:\n", total_orders_per_customer)
print("\nAverage Order Quantity per Product:\n", average_order_quantity_per_product)
print("\nEarliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
