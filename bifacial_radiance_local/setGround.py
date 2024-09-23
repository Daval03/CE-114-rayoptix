from utils.json_folder_utils import *
from bifacial_radiance import RadianceObj
import json

def ground(name_folder, material=None, material_file=None):
    """
    Sets the ground material for the simulation folder.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    material : numeric or str, optional
        Material name or albedo value to be used for the ground. Default is None.
    material_file : str, optional
        Path to the material file. Default is None.
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    
    if name_folder in data:
        folder_path = data[name_folder]
        red = RadianceObj(name_folder, str(folder_path))        
        #Pass the material and material_file to setGround
        red.setGround(material=material, material_file=material_file)
    else:
        print(f"Folder '{name_folder}' not found.")
        

