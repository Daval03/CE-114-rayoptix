from utils.json_folder_utils import *
from utils.csv_folder_utils import load_params_from_csv
from utils.metadata_utils import save_variable
import bifacial_radiance as br
import json


def build_cell_module_params(cell_data):
    """Build the cell module parameters dictionary."""
    return {
        'numcellsx': cell_data.get('numcellsx'),
        'numcellsy': cell_data.get('numcellsy'),
        'xcell': cell_data.get('xcell'),
        'ycell': cell_data.get('ycell'),
        'xcellgap': cell_data.get('xcellgap'),
        'ycellgap': cell_data.get('ycellgap')
    } if cell_data else None

def build_tube_params(tube_data):
    """Build the tube parameters dictionary."""
    return {
        'tubetype': tube_data.get('tubetype'),
        'material': tube_data.get('tubematerial'),
        'diameter': tube_data.get('diameter'),
        'axisofrotation': tube_data.get('axisofrotation')
    } if tube_data else None

def build_omega_params(omega_data):
    """Build the omega parameters dictionary."""
    return {
        'omega_material': omega_data.get('omega_material'),
        'mod_overlap': omega_data.get('mod_overlap'),
        'x_omega1': omega_data.get('x_omega1'),
        'y_omega': omega_data.get('y_omega'),
        'z_omega1': omega_data.get('z_omega1'),
        'x_omega2': omega_data.get('x_omega2'),
        'x_omega3': omega_data.get('x_omega3'),
        'z_omega3': omega_data.get('z_omega3')
    } if omega_data else None

def make_Module_Local(name_folder, pathCSV_makeModule, pathCSV_cellModule, pathCSV_tubeParams, pathCSV_omegaParams):
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
    
    # Load CSV parameters
    makeModule_params = load_params_from_csv(pathCSV_makeModule)
    if not makeModule_params:
        print("CSV files are missing.")
        return
    
    # Extract main module parameters
    name = makeModule_params.get('name')
    x = makeModule_params.get('x')
    y = makeModule_params.get('y')
    z = makeModule_params.get('z')
    numpanels = makeModule_params.get('numpanels')
    xgap = makeModule_params.get('xgap')
    ygap = makeModule_params.get('ygap')
    zgap = makeModule_params.get('zgap')
    bifi = makeModule_params.get('bifi')
    
    # Prepare optional parameters
    cellModule_params = build_cell_module_params(load_params_from_csv(pathCSV_cellModule))
    tubeParams = build_tube_params(load_params_from_csv(pathCSV_tubeParams))
    omegaParams = build_omega_params(load_params_from_csv(pathCSV_omegaParams))
    
    # Create the module
    original_path = os.getcwd()
    os.chdir(folder_path)
    module = red.makeModule(
        name=name,
        x=x,
        y=y,
        z=z,
        numpanels=numpanels,
        xgap=xgap,
        ygap=ygap,
        zgap=zgap,
        bifi=bifi,
        cellModule=cellModule_params,
        tubeParams=tubeParams,
        omegaParams=omegaParams
    )
    os.chdir(original_path)
    # Save the module and variable
    red.save(red_save)

make_Module_Local(name_folder= "Test_2", 
pathCSV_makeModule="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeModule_params.csv", 
pathCSV_cellModule= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/cellModule_params.csv",
pathCSV_tubeParams= None,
pathCSV_omegaParams= None)



# make_Module_Local(name_folder= "T1", 
# pathCSV_makeModule="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/makeModule_params.csv", 
# pathCSV_cellModule= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/cellModule_params.csv",
# pathCSV_tubeParams= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/tubeParams.csv",
# pathCSV_omegaParams= "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/omegaParams.csv")