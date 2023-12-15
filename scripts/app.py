import streamlit as st
from categories import generate_categories
from products import generate_products
from customers import generate_customers
import pandas as pd

def main():
    st.title('E-commerce Data Generator')

    # Section for generating customer data
    st.subheader('Generate Customer Data')
    num_customers = st.number_input('Number of Customers', min_value=10, max_value=10000, step=10)
    if st.button('Generate Customers'):
        customers_df = generate_customers(num_customers)
        st.write('Customers Generated!')
        st.dataframe(customers_df.head())  # Display a preview of the data
        st.download_button('Download Customers Data', customers_df.to_csv().encode('utf-8'), 'customers.csv', 'text/csv')

   # Section for generating category data
    st.subheader('Generate Category Data')
    categories_file = st.file_uploader('Upload a CSV file for Categories', type=['csv'])
    if st.button('Generate Categories'):
        categories_df = generate_categories(categories_file)
        st.write('Categories Generated!')
        st.dataframe(categories_df.head())
        st.download_button('Download Categories Data', categories_df.to_csv().encode('utf-8'), 'categories.csv', 'text/csv')

    # Section for generating product data
    st.subheader('Generate Product Data')
    num_products = st.number_input('Number of Products', min_value=10, max_value=1000, step=10)
    if st.button('Generate Products'):
        if categories_df is not None:
            products_df = generate_products(categories_df, num_products)
            st.write('Products Generated!')
            st.dataframe(products_df.head())
            st.download_button('Download Products Data', products_df.to_csv().encode('utf-8'), 'products.csv', 'text/csv')
        else:
            st.error('Please generate categories first.')


if __name__ == "__main__":
    main()
