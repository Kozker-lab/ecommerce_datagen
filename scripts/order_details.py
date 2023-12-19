from imports import *

# Function to generate synthetic order details data, ensuring it relates to the Orders and Products data.
fake = Faker()
def generate_normalized_list(n):
    # Generate a list of n random numbers
    random_numbers = [random.random() for _ in range(n)]

    # Calculate the sum of these numbers
    total_sum = sum(random_numbers)
    
    normalized_calc = lambda x: x/total_sum
    # Normalize each number by dividing it by the total sum
    normalized_numbers = [normalized_calc(number) for number in random_numbers]
    normalized_numbers = np.round(normalized_numbers, 2)
    return normalized_numbers

def generate_order_details(orders_df, n_items, products_df):
    order_details_data = []
    quantity_weights = generate_normalized_list(n_items)
    # Loading the products data to get valid ProductIDs and their prices
    for _, order in orders_df.iterrows():
        num_details = random.randint(1, 3)  # Assuming each order has 1 to 3 different products
    
        for _ in range(num_details):
            order_detail_id = fake.unique.random_int(min=1, max=999999)
            # Select a random OrderID from the previously generated orders data
            order_id = order['OrderID']
            # Select a random product and its price
            product_entry = products_df.sample(1).iloc[0]
            product_id = product_entry['ProductID']
            quantity = random.choices([1,2,3,4,5], quantity_weights)[0] # Assuming 1 to 5 units per product in an order
            price = product_entry['Price']  # Price at the time of order, assuming it remains constant for simplicity
            
            order_details_data.append({
                "OrderDetailID": order_detail_id,
                "OrderID": order_id,
                "ProductID": product_id,
                "Quantity": quantity,
                "Price": price,
                "TotalAmount": quantity * price
            })

    return pd.DataFrame(order_details_data)


