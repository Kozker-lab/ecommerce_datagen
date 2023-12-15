from imports import *

# Initialize Faker to a variable
fake = Faker()

# Set the number of observations - for a medium-sized e-commerce electronics store, 
# a sample of 1000 customers is reasonable for demonstrative purposes.
num_obs = 10000

# Define a function to generate the data
def generate_customers(num_obs):
    customers_data = []
    for _ in range(num_obs):
        customer_id = fake.unique.random_int(min=1, max=999999)
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        address = fake.address()
        registration_date = fake.date_between(start_date='-5y', end_date='today')
        # Ensuring last login is a date object, and not before the registration date
        last_login = registration_date + timedelta(days=random.randint(0, 365 * 2))
        last_login = min(last_login, fake.date_time_this_decade(before_now=True, after_now=False).date()) 
        
        customers_data.append({
            "CustomerID": customer_id,
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Address": address.replace('\n', ', '),
            "RegistrationDate": registration_date,
            "LastLogin": last_login
        })
    customers_df = pd.DataFrame(customers_data)
    return customers_df
