import bifacial_radiance as br
import json
import pickle
from utils.json_folder_utils import *
from utils.metadata_utils import *
from utils.csv_folder_utils import load_params_from_csv

def setAnalysisObj_Local(name_folder, pathfile, name, hpc):
    """
    Sets the Analysis Object for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathfile : str
        The path to the OCT file used in the simulation.
    name : str
        The name to assign to the analysis object.
    hpc : bool
        A flag indicating if High Performance Computing (HPC) is being used.

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
        if os.path.exists(pathfile):
            analysis = br.AnalysisObj(octfile=pathfile, name=name, hpc=hpc)
            save_variable(folder_path, "analysis", analysis)
        else:
            print(f"CSV file '{name_folder}' not found.")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def setmoduleAnalysis_Local(name_folder, pathCSV):
    """
    Configures and runs the module analysis for a bifacial radiance simulation, loading parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        The path to the CSV file containing the parameters for the module analysis.

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
        
        #Load the radianceObj and analysisObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        analysis = load_variable(folder_path, "analysis")

        # Load CSV parameters pathCSV
        analysis_params = load_params_from_csv(pathCSV)        
        scene = analysis_params.get('scene')
        if not analysis_params:
            print("CSV files are missing.")
            return
        elif scene:
            modWanted = analysis_params.get('modWanted')
            rowWanted = analysis_params.get('rowWanted')
            sensorsy = analysis_params.get('sensorsy')
            sensorsx = analysis_params.get('sensorsx')
            frontsurfaceoffset = analysis_params.get('frontsurfaceoffset')
            backsurfaceoffset = analysis_params.get('backsurfaceoffset') 
            modscanfront = analysis_params.get('modscanfront')
            cusmodscanbacktomtext = analysis_params.get('modscanback') 
            modscanback = analysis_params.get('modscanback')
            relative = analysis_params.get('relative') 
            debug = analysis_params.get('debug')
            
            frontscan, backscan = analysis.moduleAnalysis(scene=red.scene,
                modWanted=modWanted,
                rowWanted=rowWanted,
                sensorsy=sensorsy,
                sensorsx=sensorsx,
                frontsurfaceoffset=frontsurfaceoffset,
                backsurfaceoffset=backsurfaceoffset,
                modscanfront=modscanfront,
                modscanback=modscanback,
                relative=relative,
                debug=debug)
            save_variable(folder_path, "frontscan", frontscan)
            save_variable(folder_path, "backscan", backscan)
            print("frontscan and backscan now exist")
        else:
            print("scene is not define")
            return
        save_variable(folder_path, "analysis", analysis)

    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#setAnalysisObj_Local(name_folder="Test_1", pathfile="C:/Users/cambr/bifacial_radiance/TEMP/Tutorial_11/tutorial_11.oct", name=None, hpc=False)
#setmoduleAnalysis_Local(name_folder="Test_1", pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/moduleAnalysis_params.csv")