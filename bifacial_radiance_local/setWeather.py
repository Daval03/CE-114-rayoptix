import os
import shutil
from utils.json_folder_utils import load_data
import bifacial_radiance as br
import json

def setEPW(name_folder, lat=None, lon=None, GetAll=False):
    """
    Sets up the EPW file for a specific simulation folder using bifacial_radiance
    and moves the EPWs folder to the desired location.

    Parameters:
    name_folder (str): The name of the simulation folder.
    lat (float, optional): Latitude of the location. Default is None.
    lon (float, optional): Longitude of the location. Default is None.
    GetAll (bool, optional): If True, get a list of all available EPW files. Default is False.
    """
    
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        
        # Combine folder_path with name_folder to get the full path
        full_path = os.path.join(folder_path, name_folder)
        
        # Load the Radiance object using the full path
        red = br.load.loadRadianceObj(full_path)

        # Retrieve the EPW file based on latitude and longitude
        epwfile = red.getEPW(lat, lon, GetAll)
        print(f"EPW file obtained: {epwfile}")
        
        # Define the source and destination of the EPWs folder
        epws_source = os.path.join(os.getcwd(), "EPWs")  # Assuming it gets created in the current working directory
        epws_destination = os.path.join(folder_path, "EPWs")
        
        # Check if the EPWs folder exists and move it
        if os.path.exists(epws_source):
            for filename in os.listdir(epws_source):
                file_path = os.path.join(epws_source, filename)
                shutil.move(file_path, epws_destination)
                print(f"Moved: {filename} to {epws_destination}")
            # Optionally, remove the empty EPWs folder
            os.rmdir(epws_source)
        else:
            print(f"EPWs folder not found at: {epws_source}")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

# Example usage
setEPW("T2", 37.5, -77.6)
