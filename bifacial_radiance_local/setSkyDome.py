from utils.json_folder_utils import *
import bifacial_radiance as br
import json

def gen_CumSky_Local(name_folder,gencumsky_path, savefile):
    
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


gen_CumSky_Local(name_folder= "Test_2",
gencumsky_path="EPWs/metdata_temp.csv",
savefile= "eje")

# gen_CumSky_Local(name_folder= "Tutorial4",
# gencumsky_path=None,
# savefile= None)

