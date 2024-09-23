from utils.json_folder_utils import *
from bifacial_radiance import RadianceObj
import json

def ground(name_folder):
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    print(data)
    
    if check_unique_name(json_file, name_folder):
        folder_path = data[name_folder] 
        red = RadianceObj(name_folder, str(folder_path)) 

    else:
        print(f"Carpetas no existente")


ground("T1")