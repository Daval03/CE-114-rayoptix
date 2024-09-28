from utils.json_folder_utils import *
from utils.scene_utils import set_ground_properties
from utils.csv_folder_utils import load_params_from_csv
import bifacial_radiance as br
import json
import pickle


def set_Ground_Local(name_folder, material=None, material_file=None):
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
        
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        
        original_path = os.getcwd()
        os.chdir(folder_path)
        
        if isinstance(material, str):
            red.setGround()
            set_ground_properties(red, material)
        else:
            #Set the ground material using the material and material_file parameters
            red.setGround(material=material, material_file=material_file)
        
        os.chdir(original_path)
        # Save the object back using pickle
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def set_1axis_Local(name_folder, pathCSV):
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
        
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        
        # Load CSV parameters
        set1axis_params = load_params_from_csv(pathCSV)

        if not set1axis_params:
            print("CSV files are missing.")
            return
        print(set1axis_params)
        # Extract main module parameters
        metdata = set1axis_params.get('metdata')
        azimuth = set1axis_params.get('azimuth')
        limit_angle = set1axis_params.get('limit_angle')
        angledelta = set1axis_params.get('angledelta')
        backtrack = set1axis_params.get('backtrack')
        gcr = set1axis_params.get('gcr')
        cumulativesky = set1axis_params.get('cumulativesky')
        fixed_tilt_angle = set1axis_params.get('fixed_tilt_angle')
        useMeasuredTrackerAngle = set1axis_params.get('useMeasuredTrackerAngle')
        
        if metdata is True:
            metobj = red.metdata
        else:
            metobj = None

        original_path = os.getcwd()
        os.chdir(folder_path)
        
        red.set1axis(metdata=metobj,
        azimuth=azimuth,
        limit_angle=limit_angle,
        angledelta=angledelta,
        backtrack=backtrack,
        gcr=gcr,
        cumulativesky=cumulativesky,
        fixed_tilt_angle=fixed_tilt_angle,
        useMeasuredTrackerAngle=useMeasuredTrackerAngle)
        
        # Save the object back using pickle
        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#set_Ground_Local("Test_2", material=0.2, material_file= None)
#set_1axis_Local("Test_2", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/set1axis_params.csv")