from utils.json_folder_utils import *
import bifacial_radiance as br
import json
from utils.scene_utils import set_ground_properties

def ground(name_folder, material=None, material_file=None):
    """
    Sets the ground material for the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    material : numeric or str, optional
        Material name or albedo value to be used for the ground. Default is None.
    material_file : str, optional
        Path to the material file. Default is None.
    """
    
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    
    # Check if the folder name exists in the loaded data
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        # Combine folder_path with name_folder to get the full path
        full_path = os.path.join(folder_path, name_folder)
        # Load the Radiance object using the full path
        red = br.load.loadRadianceObj(full_path)
        
        if isinstance(material, str):
            red.setGround()
            set_ground_properties(red, material)
        else:
            #Set the ground material using the material and material_file parameters
            red.setGround(material=material, material_file=material_file)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#ground("T1", 0.25)
