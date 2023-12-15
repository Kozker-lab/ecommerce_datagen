from imports import *

# Initialize Faker
fake = Faker()

# Generate product name based on category name
def generate_product_name(category_name):
    product_type = category_name.split('&')[0].strip() # Get the first word in the category name
    model_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) # Join 3 random letters and digits
    return f"{product_type} {model_suffix}" # Return the product name

# Generate product description based on product name and category name
def generate_description(product_name, category_name):
    # List of features to choose from
    features = [
        "an ergonomic design for ease of use",
        "state-of-the-art technology for peak performance",
        "a sleek and modern design",
        "unmatched durability and reliability",
        "energy-efficient operation",
        "user-friendly interface and features",
        "cutting-edge features for the modern user",
        "portable and lightweight design for convenience",
        "premium build quality",
        "excellent value for the price"
    ]
    
    adjective = random.choice(["high-performance", "powerful", "user-friendly", "compact and durable", "premium"]) # choosing randomly from a list of adjectives describing the product
    main_feature = random.choice(features) # choosing randomly from the list of features
    category_focus = category_name.split('&')[0].strip() # Get the first word in the category name
    return f"The {product_name}, a {adjective} {category_focus}, that features {main_feature}. Ideal for both everyday and professional use." # Use the variables to generate a description

# Generate products with the help of previous functions
def generate_products(num_obs, categories_df):
    products_data = [] # Initialize an empty list to store the data
    # Assuming categories_df is a DataFrame containing CategoryID and Name
    category_list = categories_df['CategoryID'].tolist()  # Get a list of CategoryIDs
    category_weights = [0.3, 0.18, 0.24, 0.12, 0.10, 0.04, 0.02]  # Weights for each category

    for _ in range(num_obs):
        product_id = fake.unique.random_int(min=1, max=9999) # Generate a unique product ID
        category_id = random.choices(category_list, weights=category_weights, k=1)[0] # Choose a category based on the weights
        category_name = categories_df.loc[categories_df['CategoryID'] == category_id, 'Name'].values[0] # Get the category name
        name = generate_product_name(category_name) # Generate a product name based on the category
        price = round(random.uniform(50, 1500), 2) #  randomly set a price between 50 and 1500
        description = generate_description(name, category_name) # Generate a description based on the product name and category
        supplier_id = fake.random_int(min=1, max=20) # Assuming 20 different suppliers.

        products_data.append({
            "ProductID": product_id,
            "Name": name,
            "CategoryID": category_id,
            "Price": price,
            "Description": description,
            "SupplierID": supplier_id
        })
    products_df = pd.DataFrame(products_data)
    return products_df