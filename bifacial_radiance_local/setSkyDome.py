from utils.json_folder_utils import *
import bifacial_radiance as br
import json

def gen_CumSky_Local(name_folder, gencumsky_path, savefile):
    """
    Generates a cumulative sky for the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    gencumsky_path : str
        Path to the custom gencumsky file. If None, default values are used.
    savefile : str
        Filename to save the cumulative sky file.
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
        # Verify if gencumsky_path is a valid path
        if gencumsky_path is None: 
            red.genCumSky(savefile=savefile)
        elif os.path.exists(gencumsky_path):
            print(f"The path '{gencumsky_path}' exists.")
            red.genCumSky(gencumsky_metfile=gencumsky_path, savefile=savefile)    
        else:
            print(f"The path '{gencumsky_path}' does not exist.")
        os.chdir(original_path)
        
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def gen_CumSky1axis_Local(name_folder, trackerdict):
    """
    Generates a cumulative sky for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    trackerdict : dict
        Dictionary of tracker configurations.
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
        
        red.genCumSky1axis(trackerdict=trackerdict)

        os.chdir(original_path)
        
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def gen_Daylit_Local(name_folder, timeindex, metdata, debug=False):
    """
    Generates daylighting data for a specific time index using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    timeindex : int
        Time index for which the daylighting data should be generated.
    metdata : bool
        Whether to use metdata from the Radiance object. If False, metdata is set to None.
    debug : bool, optional
        Flag for enabling debug mode. Default is False.
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
        
        #Load the radianceObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        
        if metdata is True:
            metobj = red.metdata
        else:
            metobj = None
        
        #Move the process to the folder_path
        original_path = os.getcwd()
        os.chdir(folder_path)
        red.gendaylit(timeindex=timeindex,metdata=metobj,debug=debug)
        os.chdir(original_path)
        
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def gen_Daylit2Manual_Local(name_folder, dni, dhi, sunalt, sunaz):
    """
    Manually generates daylighting data for the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    dni : float
        Direct normal irradiance (DNI) value.
    dhi : float
        Diffuse horizontal irradiance (DHI) value.
    sunalt : float
        Sun altitude angle.
    sunaz : float
        Sun azimuth angle.
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
        
        #Load the radianceObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        
        #Move the process to the folder_path
        original_path = os.getcwd()
        os.chdir(folder_path)
        
        red.gendaylit2manual(dni=dni, dhi=dhi, sunalt=sunalt, sunaz=sunaz)
        
        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

###
#Not working
###
def gen_DayLit1Axis_Local(name_folder, metdata, trackerdict):
    """
    Generates daylighting data for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    metdata : bool
        Whether to use metdata from the Radiance object. If False, metdata is set to None.
    trackerdict : dict
        Dictionary of tracker configurations.
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
        
        #Load the radianceObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        
        #Check if red.module exist
        if metdata  is True:
            metObj = red.module
        else:
            metObj = None
          
        #Move the process to the folder_path
        original_path = os.getcwd()
        os.chdir(folder_path)
        
        red.gendaylit1axis(metdata=metObj,trackerdict=trackerdict)
        
        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

# gen_CumSky_Local(name_folder= "Test_2", 
# gencumsky_path="EPWs/metdata_temp.csv", 
# savefile= "eje")

# gen_CumSky1axis_Local(name_folder= "Test_2",
# trackerdict=None)

# gen_Daylit_Local(name_folder="Test_2", 
# timeindex=420, 
# metdata=True, debug=False)

# gen_Daylit2Manual_Local(name_folder="Test_2", 
# dni =40, 
# dhi =45, 
# sunalt=90,
# sunaz =45)

# gen_DayLit1Axis_Local(name_folder="Test_2", 
# metdata=False, 
# trackerdict=None)