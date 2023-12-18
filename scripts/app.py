import streamlit as st
from categories import generate_categories
from products import generate_products
from customers import generate_customers
from orders import generate_orders
from order_details import generate_order_details
import pandas as pd


def main():
    st.title('E-commerce Data Generator')
    if 'categories_df' not in st.session_state:
        st.session_state['categories_df'] = pd.DataFrame()
        
    # Section for generating customer data
    st.subheader('Generate Customer Data')
    num_customers = st.number_input('Number of Customers', min_value=10, max_value=10000, step=10)
    if st.button('Generate Customers'):
        customers_df = generate_customers(num_customers)
        st.session_state['customers_df'] = customers_df
        st.write('Customers Generated!')
        st.dataframe(customers_df.head())  # Display a preview of the data
        st.download_button('Download Customers Data', customers_df.to_csv().encode('utf-8'), 'customers.csv', 'text/csv')

   # Section for generating category data
    st.subheader('Generate Category Data')
    categories_file = st.file_uploader('Upload a CSV file for Categories', type=['csv'])
    if st.button('Generate Categories'):
        categories_df = generate_categories(categories_file)
        st.session_state['categories_df'] = categories_df
        st.write('Categories Generated!')
        st.dataframe(categories_df.head())
        st.download_button('Download Categories Data', categories_df.to_csv().encode('utf-8'), 'categories.csv', 'text/csv')

    # Section for generating product data
    st.subheader('Generate Product Data')
    num_products = st.number_input('Number of Products', min_value=10, max_value=1000, step=10)
    if st.button('Generate Products'):   
        if 'categories_df' in st.session_state:
            categories_df = st.session_state['categories_df']
            products_df = generate_products(num_products, categories_df)
            st.session_state['products_df'] = products_df
            st.write('Products Generated!')
            st.dataframe(products_df.head())
            st.download_button('Download Products Data', products_df.to_csv().encode('utf-8'), 'products.csv', 'text/csv')
        else:
            st.error('Please generate categories first.')
    
    # Section for generating order data
    st.subheader('Generate Order Data')
    orders_per_customer = st.number_input('Number of Orders per Customer', min_value=1, max_value=10, step=1)
    if st.button('Generate Orders'):
        if 'customers_df' in st.session_state:
            customers_df = st.session_state['customers_df']
            orders_df = generate_orders(customers_df, orders_per_customer)
            st.session_state['orders_df'] = orders_df
            st.write('Orders Generated!')
            st.dataframe(orders_df.head())
            st.download_button('Download Orders Data', orders_df.to_csv().encode('utf-8'), 'orders.csv', 'text/csv')
        else:
            st.error('Please generate customers first.')
    
    # Section for generating order details data
    st.subheader('Generate Order Details')
    n_items = st.number_input('Number of Items per Order', min_value=1, max_value=10, step=1)
    if st.button('Generate Order Details'):
        if 'orders_df' in st.session_state and 'products_df' in st.session_state:
            orders_df = st.session_state['orders_df']
            products_df = st.session_state['products_df']
            order_details_df = generate_order_details(orders_df, n_items, products_df)
            st.session_state['order_details_df'] = order_details_df
            st.write('Order Details Generated!')
            st.dataframe(order_details_df.head())
            st.download_button('Download Order Details Data', order_details_df.to_csv().encode('utf-8'), 'order_details.csv', 'text/csv')
        else:
            st.error('Please generate orders and products first.')

if __name__ == "__main__":
    main()
