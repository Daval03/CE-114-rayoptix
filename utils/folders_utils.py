import os
import json
from bifacial_radiance import RadianceObj
from utils.json_folder_utils import *
import shutil

def create_folder(folder_path, name_folder):
    """Creates a folder if it doesn't exist and initializes a RadianceObj.
    Also saves folder_path and name_folder to a JSON file if name_folder is unique.
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    try:
        # Load existing data and validate
        data = load_data(json_file)
        validate_folders_in_json(data)

        # Check if the name is unique
        if check_unique_name(data, name_folder):
            folder_path = os.path.abspath(folder_path) if not os.path.isabs(folder_path) else folder_path
            
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                red = RadianceObj(name_folder, str(folder_path))  # Use this if necessary
                
                #name_radianceObj = name_folder + '.pickle'
                #red.save(name_radianceObj)

                print(f"Folder created at {folder_path}")
            else:
                print(f"Folder already exists at {folder_path}")

            # Save the new entry in the JSON
            data[name_folder] = folder_path
            save_data(json_file, data)
            print(f"Data saved: {name_folder} -> {folder_path}")
            
            # Create "metadata" folder inside folder_path
            metadata_folder = os.path.join(folder_path, "metadata")
            if not os.path.exists(metadata_folder):
                os.makedirs(metadata_folder)
                print(f"'metadata' folder created at {metadata_folder}")
            
        else:
            print(f"Name '{name_folder}' already exists in {json_file}.")
    
    except Exception as e:
        print(f"Error: {e}")

def setup_simulation_folder(folder_path: str, name_folder: str, use_absolute=True):
    """Sets up the simulation folder at the specified path."""
    folder_path = os.path.normpath(folder_path)
    create_folder(folder_path, name_folder)


##
# Validar que la ruta no se repita para crear o meter las varas en el json
##
# Example call
#setup_simulation_folder("C:/Users/cambr/bifacial_radiance/TEMP/Tutorial", "Test", False)
