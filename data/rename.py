import os
import pandas as pd

# Specify the directory containing the CSV files
csv_directory = 'c:/Users/Client/Desktop/Automation Python/Data'

# Get the list of CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Iterate over each CSV file
for csv_file in csv_files:
    # Read the CSV file
    csv_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(csv_path)
    
    # Create a new XLSX file name
    xlsx_file = csv_file.replace('.csv', '.xlsx')
    xlsx_path = os.path.join(csv_directory, xlsx_file)
    
    # Save the data to the XLSX file
    df.to_excel(xlsx_path, index=False)

