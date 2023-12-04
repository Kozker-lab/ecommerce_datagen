import imports
import customers
import products

# Function to generate synthetic order data taking into account the customers and products data previously generated.

def generate_orders(num_orders, customers_df, products_df):
    order_statuses = ["Processing", "Shipped", "Delivered", "Cancelled", "Returned"]
    
    orders_data = []
    for _ in range(num_orders):
        order_id = fake.unique.random_int(min=1, max=999999)
        # Select a random customer ID from the previously generated customers data
        customer_id = random.choice(customers_df['CustomerID'].tolist())
        order_date = fake.date_between(start_date='-2y', end_date='today')
        # TotalAmount will be a random value, realistically assuming a range for electronic products
        total_amount = round(random.uniform(50, 5000), 2)
        status = random.choice(order_statuses)
        
        orders_data.append({
            "OrderID": order_id,
            "CustomerID": customer_id,
            "OrderDate": order_date,
            "TotalAmount": total_amount,
            "Status": status
        })
    
    return pd.DataFrame(orders_data)

# Load the customers data to ensure we are referencing existing CustomerIDs
customers_df_loaded = pd.read_csv('./data/customers.csv')
# We don't need to load the product data for this table since it doesn't reference specific products

# Generate a realistic number of orders based on the number of customers (assuming not every customer makes an order)
num_customers = customers_df_loaded.shape[0]
# Assuming each customer could have made up to 5 orders in the past 2 years
num_orders = random.randint(num_customers, num_customers * 5)

# Generate the orders data
orders_df = generate_orders(num_orders, customers_df_loaded, None)

# Save the data to a CSV file
orders_csv_file_path = './data/orders.csv'
orders_df.to_csv(orders_csv_file_path, index=False)

