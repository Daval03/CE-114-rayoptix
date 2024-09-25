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
            
            # Create "metadata" folder inside folder_path
            metadata_folder = os.path.join(folder_path, "metadata")
            if not os.path.exists(metadata_folder):
                os.makedirs(metadata_folder)
                print(f"'metadata' folder created at {metadata_folder}")
            
        else:
            print(f"Name '{folder_key}' already exists in {json_file}.")
    
    except Exception as e:
        print(f"Error: {e}")

def setup_simulation_folder(folder_path: str, name_folder: str, use_absolute=True):
    """Sets up the simulation folder at the specified path."""
    folder_path = os.path.normpath(folder_path)
    create_folder(folder_path, name_folder)

def move_epws_folder(folder_path):
    """Moves the EPWs folder from the current working directory to the specified destination."""
    # Define the source and destination of the EPWs folder
    epws_source = os.path.join(os.getcwd(), "EPWs")  # Assuming it gets created in the current working directory
    epws_destination = os.path.join(folder_path, "EPWs")
    
    # Check if the EPWs folder exists and move it
    if os.path.exists(epws_source):
        # Create destination directory if it doesn't exist
        os.makedirs(epws_destination, exist_ok=True)
        
        for filename in os.listdir(epws_source):
            file_path = os.path.join(epws_source, filename)
            shutil.move(file_path, epws_destination)
            print(f"Moved: {filename} to {epws_destination}")
        
        # Optionally, remove the empty EPWs folder
        os.rmdir(epws_source)
    else:
        print(f"EPWs folder not found at: {epws_source}")

# Example call
#setup_simulation_folder("../../TEMP/T3", "T3", True)
