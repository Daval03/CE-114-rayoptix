import os
import json
from bifacial_radiance import RadianceObj
from utils.json_folder_utils import *

# Function to create the folder if it doesn't exist and save it in JSON
def create_folder(folder_path, name_folder):
    """Creates a folder if it doesn't exist and initializes a RadianceObj.
    Also saves folder_path and name_folder to a JSON file if name_folder is unique.
    """
    json_file='simulation_folders.json'
    try:
        # Load existing data
        data = load_data(json_file)
        
        if check_unique_name(json_file, name_folder):
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                redi = RadianceObj(name_folder, str(folder_path))
                print(f"Folder created at {folder_path}")
            else:
                print(f"Folder already exists at {folder_path}")

            # Save the new entry in JSON
            data[name_folder] = folder_path
            save_data(json_file, data)
            print(f"Data saved: {name_folder} -> {folder_path}")
        else:
            print(f"Name '{name_folder}' already exists in {json_file}.")
    
    except Exception as e:
        print(f"Error: {e}")


def setup_simulation_folder(folder_path: str, name_folder: str, use_absolute=True):
    """Sets up the simulation folder at the specified path."""
    folder_path = os.path.normpath(folder_path)
    if not use_absolute:
        folder_path = os.path.abspath(folder_path)

    print(f"Your simulation will be stored in {folder_path}")
    create_folder(folder_path, name_folder)


create_folder