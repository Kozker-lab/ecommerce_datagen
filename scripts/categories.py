from imports import *

# List of categories and their descriptions
def generate_categories(categories_info):


    categories_sample = {
        1: ("Smartphones & Accessories", "Devices and accessories for communication and productivity."),
        2: ("Computers & Laptops", "Computing devices from personal to professional use, including peripherals."),
        3: ("Cameras & Photography", "Equipment for capturing images and videos."),
        4: ("TVs & Monitors", "Visual display units for entertainment and work."),
        5: ("Gaming Consoles & Accessories", "Hardware and accessories for gaming enthusiasts."),
        6: ("Audio Equipment", "Devices for recording and playing back sound."),
        7: ("Wearable Technology", "Electronic devices that can be worn as accessories."),
        8: ("Drones & Tech Toys", "Remote-controlled and electronic gadgets for fun and recreation.")
    }
    # Check if category_info has 2 columns and the first column is Category and Second Column is Description
    if categories_info is not None:
        categories_info = pd.DataFrame(pd.read_csv(categories_info))
        if categories_info.columns[0] == 'Category' and categories_info.columns[1] == 'Description':
            categories_info = categories_info.to_dict()
        else: raise ValueError('categories_info should have 2 columns: Category and Description')
    
    # If the file is not found, use the sample    
    elif categories_info is None:
        categories_info = categories_sample
        
        
    # There won't be a ParentCategoryID since these are top-level categories
    categories_data = [{
        "CategoryID": category_id,
        "Name": details[0],
        "Description": details[1],
        "ParentCategoryID": None  # None indicates no parent category; these are top-level
    } for category_id, details in categories_info.items()]

    categories_df = pd.DataFrame(categories_data)
    return categories_df



