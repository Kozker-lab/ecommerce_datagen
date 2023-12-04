import imports
# List of categories and their descriptions
categories_info = {
    1: ("Smartphones & Accessories", "Devices and accessories for communication and productivity."),
    2: ("Computers & Laptops", "Computing devices from personal to professional use, including peripherals."),
    3: ("Cameras & Photography", "Equipment for capturing images and videos."),
    4: ("TVs & Monitors", "Visual display units for entertainment and work."),
    5: ("Gaming Consoles & Accessories", "Hardware and accessories for gaming enthusiasts."),
    6: ("Audio Equipment", "Devices for recording and playing back sound."),
    7: ("Wearable Technology", "Electronic devices that can be worn as accessories."),
    8: ("Drones & Tech Toys", "Remote-controlled and electronic gadgets for fun and recreation.")
}

# There won't be a ParentCategoryID since these are top-level categories
categories_data = [{
    "CategoryID": category_id,
    "Name": details[0],
    "Description": details[1],
    "ParentCategoryID": None  # None indicates no parent category; these are top-level
} for category_id, details in categories_info.items()]

categories_df = pd.DataFrame(categories_data)

# Save the data to a CSV file
categories_csv_file_path = './data/categories.csv'
categories_df.to_csv(categories_csv_file_path, index=False)