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

def gen_CumSky1axis_Local(name_folder, trackerdict):
    
    #------------We need to use set1axis before --- Needs works --- not finish

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

def gen_DayLit1Axis_Local(name_folder):
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)

    #------------We need to use set1axis before --- Needs works --- not finish
    
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
        
        red.gendaylit1axis()
        
        os.chdir(original_path)
        red.save(red_save)
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")


# gen_CumSky_Local(name_folder= "Test_2", 
# gencumsky_path="EPWs/metdata_temp.csv", gendaylit2manual
# savefile= "eje")

# gen_CumSky1axis_Local(name_folder= "Test_2",
# trackerdict=None)

# gen_Daylit_Local(name_folder="Test_2", 
# timeindex=420, 
# metdata=True, debug=False)

# gen_Daylit2Manual_Local(name_folder="Test_2", gendaylit1axis
# dni =40, 
# dhi =45, 
# sunalt=90,
# sunaz =45)
