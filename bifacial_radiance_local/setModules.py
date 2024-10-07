from utils.json_folder_utils import *
from utils.csv_folder_utils import load_params_from_csv
from utils.metadata_utils import *
from utils.modules_utils import *
import bifacial_radiance as br
import json

def makeModule_Local(name_folder, pathCSV_makeModule, pathCSV_cellModule, pathCSV_tubeParams, pathCSV_omegaParams, pathCSV_frameParams):
    """
    Creates a bifacial radiance module based on parameters from multiple CSV files and saves it to the simulation folder.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV_makeModule : str
        Path to the CSV file containing general module parameters such as dimensions, number of panels, and gaps.
    pathCSV_cellModule : str
        Path to the CSV file containing cell-level parameters for the module.
    pathCSV_tubeParams : str
        Path to the CSV file containing tube-related parameters for the module.
    pathCSV_omegaParams : str
        Path to the CSV file containing omega-related parameters for the module.
    pathCSV_frameParams : str
        Path to the CSV file containing frame-related parameters for the module.
    """
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    
    # Check if the folder name exists in the loaded data
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return

    # Load the Radiance object using the folder path
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    
    original_path = os.getcwd()
    os.chdir(folder_path)

    # Load CSV parameters makeModule
    makeModule_params = load_params_from_csv(pathCSV_makeModule)
    if not makeModule_params:
        print("CSV files are missing.")
        return
    else:
        # Extract main module parameters
        name = makeModule_params.get('name')
        x = makeModule_params.get('x')
        y = makeModule_params.get('y')
        z = makeModule_params.get('z')
        modulefile = makeModule_params.get('modulefile')
        text = makeModule_params.get('text')
        customtext = makeModule_params.get('customtext') 
        if customtext is None: customtext = ""
        rewriteModulefile = makeModule_params.get('rewriteModulefile')
        glass = makeModule_params.get('glass')
        numpanels = makeModule_params.get('numpanels')
        xgap = makeModule_params.get('xgap')
        ygap = makeModule_params.get('ygap')
        zgap = makeModule_params.get('zgap')
        modulematerial = makeModule_params.get('zgmodulematerialap')
        bifi = makeModule_params.get('bifi')

        # Create the module
        module = red.makeModule(
            name=name,
            x=x,
            y=y,
            z=z,
            modulefile=modulefile,
            text=text,
            customtext=customtext,
            xgap=xgap,
            ygap=ygap,
            zgap=zgap,
            numpanels=numpanels,
            rewriteModulefile=rewriteModulefile,
            glass=glass,
            modulematerial=modulematerial,
            bifi=bifi)
        
    # Load CSV parameters addCellModule
    CellModule_params = load_params_from_csv(pathCSV_cellModule)
    if not CellModule_params:
        print("CSV files are missing.")
        return
    else:
        build_cell_module(module, CellModule_params)
    
    # Load CSV parameters pathCSV_tubeParams
    TorqueTube_params = load_params_from_csv(pathCSV_tubeParams)
    if not TorqueTube_params:
        print("CSV files are missing.")
        return
    else:
        build_tube(module, TorqueTube_params)
    
    # Load CSV parameters pathCSV_omegaParams
    Omega_params = load_params_from_csv(pathCSV_omegaParams)
    if not Omega_params:
        print("CSV files are missing.")
        return
    else:
        build_omega(module, Omega_params)
    
    # Load CSV parameters pathCSV_frameParams
    Frame_params = load_params_from_csv(pathCSV_frameParams)
    if not Frame_params:
        print("CSV files are missing.")
        return
    else:
        build_frame(module, Frame_params)

    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

def addTorqueTube_Local(name_folder, pathCSV):
    """
    Adds a torque tube to a bifacial radiance module based on parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing torque tube parameters such as diameter, material, and visibility.

    Returns
    -------
    None
    """
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    
    # Check if the folder name exists in the loaded data
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return

    # Load the Radiance object using the folder path
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)

    original_path = os.getcwd()
    os.chdir(folder_path)
    
    # Load CSV parameters pathCSV_tubeParams
    TorqueTube_params = load_params_from_csv(pathCSV)
    if not TorqueTube_params:
        print("CSV files are missing.")
        return
    else:
        build_tube(red.module, TorqueTube_params)

    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

def addCellModule_Local(name_folder, pathCSV):
    """
    Adds a cell module to a bifacial radiance module based on parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing cell module parameters such as the number of cells, gaps, and junction box.

    Returns
    -------
    None
    """ 
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    
    original_path = os.getcwd()
    os.chdir(folder_path)

    # Load CSV parameters addCellModule
    CellModule_params = load_params_from_csv(pathCSV)
    if not CellModule_params:
        print("CSV files are missing.")
        return
    else:
        build_cell_module(red.module, CellModule_params)

    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

def addOmega_Local(name_folder, pathCSV):
    """
    Adds an omega profile to a bifacial radiance module based on parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing omega profile parameters such as material, thickness, and overlap.

    Returns
    -------
    None
    """
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    # Load the data from the JSON file
    data = load_data(json_file)
    # Check if the folder name exists in the loaded data
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    # Load the Radiance object using the folder path
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)

    original_path = os.getcwd()
    os.chdir(folder_path)

    # Load CSV parameters pathCSV_omegaParams
    Omega_params = load_params_from_csv(pathCSV)
    if not Omega_params:
        print("CSV files are missing.")
        return
    else:
        build_omega(red.module, Omega_params)
        
    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

def addFrame_Local(name_folder, pathCSV):
    """
    Adds a frame to a bifacial radiance module based on parameters from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing frame parameters such as material, thickness, and number of sides.

    Returns
    -------
    None
    """
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    # Load the data from the JSON file
    data = load_data(json_file)
    # Check if the folder name exists in the loaded data
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    # Load the Radiance object using the folder path
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    original_path = os.getcwd()
    os.chdir(folder_path)

    # Load CSV parameters pathCSV_frameParams
    Frame_params = load_params_from_csv(pathCSV)
    if not Frame_params:
        print("CSV files are missing.")
        return
    else:
        build_frame(red.module, Frame_params)
        
    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

def showModule_Local(name_folder):
    """
    Displays the current module configuration for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    folder_path = data.get(name_folder)
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    original_path = os.getcwd()
    os.chdir(folder_path)
    
    red.module.showModule()

    os.chdir(original_path)
    red.save(red_save)

def readModule_Local(name_folder, name):
    """
    Reads and loads a module configuration file for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    name : str
        The name of the module file to read.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    folder_path = data.get(name_folder)
    
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    original_path = os.getcwd()
    os.chdir(folder_path)
    
    red.module.readModule(name=name)

    os.chdir(original_path)
    red.save(red_save)

def compileText_Local(name_folder, rewriteModulefile, json):
    """
    Compiles text data for a bifacial radiance module configuration.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    rewriteModulefile : bool
        If True, rewrites the existing module file with the compiled data.
    json : dict
        A dictionary with parameters to compile into the module configuration.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    folder_path = data.get(name_folder)
    
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    original_path = os.getcwd()
    os.chdir(folder_path)
    
    red.module.compileText(rewriteModulefile=rewriteModulefile,json=json)

    os.chdir(original_path)
    red.save(red_save)

def returnMaterialFiles_Local(name_folder, material_path):
    """
    Returns material file paths for a bifacial radiance simulation.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    material_path : str
        The path to the folder containing material files.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    folder_path = data.get(name_folder)
    
    if not folder_path:
        print(f"Folder '{name_folder}' not found.")
        return
    
    full_path = os.path.join(folder_path, name_folder)
    red_save = os.path.join(folder_path, "save.pickle")
    red = br.load.loadRadianceObj(red_save)
    original_path = os.getcwd()
    os.chdir(folder_path)
    
    print(red.returnMaterialFiles(material_path=material_path))

    os.chdir(original_path)
    red.save(red_save)

#returnMaterialFiles_Local(name_folder="Test_1",material_path=None)
#compileText_Local(name_folder="Test_1" ,rewriteModulefile=True, json=True)
#readModule_Local(name_folder= "Test_1", name="") 
#showModule_Local(name_folder= "Test_1") 

# addTorqueTube_Local(name_folder= "Test_1", 
# pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addTorqueTube_params.csv") 

# addOmega_Local(name_folder= "Test_1", 
# pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addOmega_params.csv") 

# addFrame_Local(name_folder= "Test_1", 
# pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addFrame_params.csv") 

# addCellModule_Local(name_folder= "Test_1", 
# pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addCellModule_params.csv") 

# makeModule_Local(name_folder= "Test_1", 
# pathCSV_makeModule="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeModule_params.csv", 
# pathCSV_cellModule= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addCellModule_params.csv",
# pathCSV_tubeParams= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addTorqueTube_params.csv",
# pathCSV_omegaParams= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addOmega_params.csv",
# pathCSV_frameParams= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/addFrame_params.csv")