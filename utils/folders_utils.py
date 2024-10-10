import os
import json
import bifacial_radiance as br
from utils.json_folder_utils import *
import shutil

def move_epws_folder(folder_path):
    """
    Moves the 'EPWs' folder from the current working directory to the specified destination.

    Parameters
    ----------
    folder_path : str
        The destination folder path where the 'EPWs' folder should be moved.

    Returns
    -------
    None
    """
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

def create_folder(folder_path, name_folder):
    """
    Creates a folder at the specified path if it doesn't already exist and initializes a RadianceObj.
    Also saves the folder path and name_folder in a JSON file if name_folder is unique.

    Parameters
    ----------
    folder_path : str
        The path where the new folder should be created.
    name_folder : str
        The unique name for the folder. It will be used as the key in the JSON file.

    Returns
    -------
    None
    """
    folder_path = os.path.normpath(folder_path)
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
                red = br.RadianceObj(name_folder, str(folder_path)) 
                red_save = os.path.join(folder_path, "save.pickle")
                red.save(red_save)
                
                # Save the new entry in the JSON
                data[name_folder] = folder_path
                save_data(json_file, data)
                print(f"Data saved: {name_folder} -> {folder_path}")
                print(f"Folder created at {folder_path}")
            else:
                print(f"Folder already exists at {folder_path}")
        else:
            print(f"Name '{name_folder}' already exists in {json_file}.")
    
    except Exception as e:
        print(f"Error: {e}")


#create_folder("C:/Users/cambr/bifacial_radiance/TEMP/Test_99", "Test_99")
#create_folder("../../../bifacial_radiance/TEMP/Test_98", "Test_98") 