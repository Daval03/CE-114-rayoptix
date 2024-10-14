from utils.json_folder_utils import *
from utils.scene_utils import *
from utils.csv_folder_utils import load_params_from_csv
import bifacial_radiance as br
import json
import pickle

def setGround_Local(name_folder, material=None, material_file=None):
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

def set1axis_Local(name_folder, pathCSV):
    """
    Sets the 1-axis tracker configuration for the simulation folder using bifacial_radiance.
    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing parameters for the 1-axis tracker configuration.
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

        # Extract and filter the parameters for the 1-axis tracker
        tracker_params = {key: value for key, value in {
            'metdata': red.metdata if set1axis_params.get('metdata') else None,
            'azimuth': set1axis_params.get('azimuth'),
            'limit_angle': set1axis_params.get('limit_angle'),
            'angledelta': set1axis_params.get('angledelta'),
            'backtrack': set1axis_params.get('backtrack'),
            'gcr': set1axis_params.get('gcr'),
            'cumulativesky': set1axis_params.get('cumulativesky'),
            'fixed_tilt_angle': set1axis_params.get('fixed_tilt_angle'),
            'useMeasuredTrackerAngle': set1axis_params.get('useMeasuredTrackerAngle')
        }.items() if value is not None}

        original_path = os.getcwd()
        os.chdir(folder_path)
        
        red.set1axis(**tracker_params)

        # Save the object back using pickle
        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeScene_Local(name_folder, pathCSV):    
    """
    Creates a scene for the simulation folder using bifacial_radiance based on the parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing parameters for scene creation.
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
        makeScene_params = load_params_from_csv(pathCSV)

        if not makeScene_params:
            print("CSV files are missing.")
            return
        
        # Extract and filter scene parameters
        scene_params = {key: makeScene_params.get(key) for key in [
            'tilt', 'pitch', 'azimuth', 'nMods', 'nRows', 'hub_height', 'clearance_height'
        ] if makeScene_params.get(key) is not None}
        
        radname = makeScene_params.get('radname')
        # Check if red.module exists
        moduleObj = makeScene_params.get('module')

        original_path = os.getcwd()
        os.chdir(folder_path)
        
        red.makeScene(module=moduleObj, sceneDict=scene_params, radname=radname)
        os.chdir(original_path)
        print("new scene had been added")
        # Save the object back using pickle
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeScene1axis_Local(name_folder, pathCSV):    
    """
    Creates a 1-axis tracker scene for the simulation folder using bifacial_radiance based on the parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing parameters for 1-axis tracker scene creation.
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
        makeScene1axis_params = load_params_from_csv(pathCSV)

        if not makeScene1axis_params:
            print("CSV files are missing.")
            return

        # Extract parameters with filtering
        trackerdict = red.trackerdict if makeScene1axis_params.get('trackerdict') else None
        module = red.module if makeScene1axis_params.get('module') else None
        sceneDict = {
            'tilt': makeScene1axis_params.get('tilt'),
            'pitch': makeScene1axis_params.get('pitch'),
            'azimuth': makeScene1axis_params.get('azimuth'),
            'hub_height': makeScene1axis_params.get('hub_height'),
        }
        cumulativesky = makeScene1axis_params.get('cumulativesky')

        # Filter the sceneDict to only include parameters with values
        sceneDict = {key: value for key, value in sceneDict.items() if value is not None}

        original_path = os.getcwd()
        os.chdir(folder_path)

        # Call the makeScene1axis method with filtered parameters
        red.makeScene1axis(trackerdict=trackerdict, module=module, sceneDict=sceneDict, cumulativesky=cumulativesky)
        os.chdir(original_path)
        
        # Save the object back using pickle
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeOct_Local(name_folder, octname):    
    """
    Generates an .oct file for the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    octname : str
        The name to be used for the .oct file.
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
        red.makeOct(filelist=red.getfilelist(), octname=octname)
        os.chdir(original_path)
        
        # Save the object back using pickle
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeOct1axis_Local(name_folder, trackerdict, singleindex, customname):
    """
    Generates an .oct file for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    trackerdict : dict
        Dictionary of tracker configurations.
    singleindex : int
        Index of the tracker configuration to be used.
    customname : str
        Custom name for the .oct file.
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
        
        # Initialize trackerObj based on trackerdict value
        trackerObj = red.trackerdict if trackerdict else None

        original_path = os.getcwd()
        os.chdir(folder_path)
        
        # Call the makeOct1axis method with trackerObj
        red.makeOct1axis(trackerdict=trackerObj,
                         singleindex=singleindex,
                         customname=customname)

        os.chdir(original_path)
        
        # Save the object back using pickle
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def showScene_Local(name_folder):
    """
    Displays the scene for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.

    Returns
    -------
    None
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
        
        red.scene.showScene()

        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeCustomObject_Local(name_folder, pathCSV):
    """
    Creates a custom object for a bifacial radiance simulation using parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        The path to the CSV file containing custom object parameters.

    Returns
    -------
    None
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
        object_params = load_params_from_csv(pathCSV)
        name = object_params.get('name')
        text = object_params.get('text')

        if not object_params:
            print("CSV files are missing.")
            return
        else:
            original_path = os.getcwd()
            os.chdir(folder_path)

            red.makeCustomObject(name=name, text=text)
            
            os.chdir(original_path)
            red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def appendtoScene_Local(name_folder, radfile, pathObject, text):
    """
    Appends a custom object to the scene for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    radfile : str
        Whether to use a radiance file in the scene.
    pathObject : str
        The path to the custom object file to be appended to the scene.
    text : str
        Additional text to include with the object in the scene.

    Returns
    -------
    None
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
        radfile = str_to_bool(radfile)
        
        if radfile and os.path.exists(pathObject):
            original_path = os.getcwd()
            os.chdir(folder_path)
            red.appendtoScene(radfile=red.scene.radfiles, customObject=pathObject, text=text)
            os.chdir(original_path)
        else:
            print("pathRadfile or pathObject doesn't exist")
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#appendtoScene_Local("Test_1", "True", "C:/Users/cambr/bifacial_radiance/TEMP/Test_1/objects/Post1.rad", "!xform -rz 0")
#makeCustomObject_Local("Test_1", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeObject_params.csv")
#showScene_Local("Test_1")
#setGround_Local("Test_1", material=0.2, material_file= None) 
#set1axis_Local("Test_1", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/set1axis_params.csv")
#makeScene_Local("Test_1", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeScene_params.csv")
#makeScene1axis_Local("Test_2", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeScene1axis_params.csv")
#makeOct_Local("Test_1", octname=None)
#makeOct1axis_Local("Test_2", trackerdict=False, singleindex=None, customname=None)