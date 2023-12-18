from imports import *
from datetime import date, timedelta


# Initialize Faker
fake = Faker()

# Define a function to generate sales dates with improved representation for December
def generate_order_dates(start_date, end_date, num_dates):
    # Define key holiday periods for the electronics market
    
    # Black Friday to Cyber Monday
    black_friday_2021 = pd.date_range(start='2021-11-25', end='2021-11-28')  # Black Friday to Cyber Monday 2021
    black_friday_2022 = pd.date_range(start='2022-11-25', end='2022-11-28')  # Black Friday to Cyber Monday 2022
    black_friday_2023 = pd.date_range(start='2023-11-25', end='2023-11-28')  # Black Friday to Cyber Monday 2023
    black_friday = black_friday_2021.union(black_friday_2022).union(black_friday_2023)

    # Christmas season
    christmas_2022 = pd.date_range(start='2022-12-10', end='2022-12-25')# Christmas 2022
    christmas_2021 = pd.date_range(start='2021-12-10', end='2021-12-25')# Christmas 2021
    christmas_2023 = pd.date_range(start='2023-12-10', end='2023-12-25') #Christmas 2023
    christmas_season = christmas_2021.union(christmas_2022).union(christmas_2023)
    
    # new years
    new_years_2023 = pd.date_range(start='2023-01-01', end='2023-01-05')  # New Year 2023
    new_years_2022 = pd.date_range(start='2022-01-01', end='2022-01-05')  # New Year 2022
    new_years = new_years_2022.union(new_years_2023)
    
    # back to school
    back_to_school_2023 = pd.date_range(start='2023-08-20', end='2023-09-10')  # Late August to early September 2023
    back_to_school_2022 = pd.date_range(start='2022-08-20', end='2022-09-10')  # Late August to early September 2022
    back_to_school = back_to_school_2022.union(back_to_school_2023)

    # Combine all holiday periods
    holiday_dates = black_friday.union(christmas_season).union(new_years).union(back_to_school)

    # Generate random dates for occasional peaks
    random_dates = pd.date_range(start=start_date, end=end_date).difference(holiday_dates)

    # Ensure a better distribution of dates by randomly selecting 20% of the dates as holiday peak dates
    
    num_holiday_dates = int(num_dates * 0.2)  # 20% of dates during the holiday season
    num_random_dates = num_dates - num_holiday_dates # Remaining 80% of dates as random dates
    holiday_peak_dates = np.random.choice(holiday_dates, size=num_holiday_dates, replace=True) # R
    random_peak_dates = np.random.choice(random_dates, size=num_random_dates, replace=True)

    # Combine holiday peak dates and random peak dates
    all_dates = np.concatenate((holiday_peak_dates, random_peak_dates))

    # Shuffle and return the dates
    np.random.shuffle(all_dates)
    return all_dates[:num_dates]


def generate_order_status(row, current_date):
    days_since_order = (current_date - row['OrderDate']).days
    if days_since_order <= 2:
        return np.random.choice(['Processing', 'Shipped'], p = [0.7, 0.3])
    elif days_since_order <=10:
        return np.random.choice(['Processing', 'Shipped'], p = [0.2, 0.8])
    elif days_since_order <= 25:
        return 'Shipped'
    elif days_since_order <= 30:
        return np.random.choice(['Delivered', 'Cancelled'], p=[0.95, 0.05])
    else:
        return np.random.choice(['Delivered', 'Returned'], p=[0.9, 0.1])

def generate_orders(customers_df, orders_per_customer):
    # Generate a realistic number of orders based on the number of customers (assuming not every customer makes an order)
    num_customers = customers_df.shape[0]
    # Assuming each customer could have made up to 5 orders in the past 2 years
    num_orders = random.randint(num_customers, num_customers * int(orders_per_customer))
    # Start Date and end_date
    end_date = date.today()
    start_date = end_date - timedelta(days=365 * 2)
    order_dates = generate_order_dates(start_date, end_date, num_orders)
    
    orders_data = []
    
    for i in range(num_orders):
        order_id = fake.unique.random_int(min=1, max=999999) 
        customer_id = random.choice(customers_df['CustomerID'].tolist())  # Select a random customer ID from the previously generated customers data
        
        orders_data.append({ 
        "OrderID": order_id,
        "CustomerID": customer_id,
        "OrderDate": order_dates[i],
        "Status": generate_order_status(i, date.today()) 
        })
        
    orders_df = pd.DataFrame(orders_data)
    
    return orders_df