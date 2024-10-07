import bifacial_radiance as br
import json
import pickle
from utils.json_folder_utils import *
from utils.metadata_utils import *

def setAnalysisObj_Local(name_folder, pathfile, name, hpc):
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
            save_variable(folder_path, "analisis", analysis)
        else:
            print(f"CSV file '{name_folder}' not found.")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def setmoduleAnalysis_Local(name_folder, pathfile):
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
        analysis = load_variable(folder_path, "analisis")

        # analysis.moduleAnalysis(scene=red.scene,
        # modWanted=,
        # rowWanted=,
        # sensorsy=,
        # sensorsx=,
        # frontsurfaceoffset=,
        # backsurfaceoffset=,
        # modscanfront=,
        # modscanback=,
        # relative=,
        # debug=False
        # )
        save_variable(folder_path, "analisis", analysis)

    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#setAnalysisObj_Local(name_folder="Test_1", pathOctfile="//", name=None, hpc=False)
