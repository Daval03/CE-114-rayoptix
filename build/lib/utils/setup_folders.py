import os
import json
from bifacial_radiance import RadianceObj
from utils.json_folder_utils import *

# Function to create the folder if it doesn't exist and save it in JSON
def create_folder(folder_path, name_folder):
    """Creates a folder if it doesn't exist and initializes a RadianceObj.
    Also saves folder_path and name_folder to a JSON file if name_folder is unique.
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    try:
        # Load existing data and validate
        data = load_data(json_file)
        validate_folders_in_json(data)
        
        # Normalize the folder name (to uppercase)
        folder_key = name_folder.upper()

        # Check if the name is unique
        if check_unique_name(data, folder_key):
            folder_path = os.path.abspath(folder_path) if not os.path.isabs(folder_path) else folder_path
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                red = RadianceObj(folder_key, str(folder_path))  # Use this if necessary
                red.save(folder_key)
                print(f"Folder created at {folder_path}")
            else:
                print(f"Folder already exists at {folder_path}")

            # Save the new entry in the JSON
            data[folder_key] = folder_path
            save_data(json_file, data)
            print(f"Data saved: {folder_key} -> {folder_path}")
        else:
            print(f"Name '{folder_key}' already exists in {json_file}.")
    
    except Exception as e:
        print(f"Error: {e}")

def setup_simulation_folder(folder_path: str, name_folder: str, use_absolute=True):
    """Sets up the simulation folder at the specified path."""
    folder_path = os.path.normpath(folder_path)
    create_folder(folder_path, name_folder)

# Example call
setup_simulation_folder("../../TEMP/T2", "T2", True)
