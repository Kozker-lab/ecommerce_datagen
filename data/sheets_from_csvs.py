# Creating an excel file with csv files as the sheets

# Import the required libraries
import os
import pandas as pd
import xlsxwriter as xw


# Specify the directory containing the CSV files
csv_directory = './data/csv'

# Get the list of CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
csv_files.sort()

# Create a Pandas Excel writer using XlsxWriter as the engine
xlsx_path = './data/xlsx/data.xlsx'
writer = pd.ExcelWriter(xlsx_path, engine='xlsxwriter')

# Iterate over each CSV file
for csv_file in csv_files:
    # Read the CSV file
    csv_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(csv_path)
    
    # Write the CSV file as a sheet in the XLSX file
    sheet_name = csv_file.replace('.csv', '')
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    
# Close the Pandas Excel writer and output the Excel file
writer.save()
