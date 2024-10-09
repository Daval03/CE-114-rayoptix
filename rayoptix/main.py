import click
from utils.folders_utils import *

from bifacial_radiance_local.setAnalysisObj import *
from bifacial_radiance_local.setModules import *
from bifacial_radiance_local.setScene import *
from bifacial_radiance_local.setSkyDome import *
from bifacial_radiance_local.setWeather import *

@click.group()
def cli():
    """Rayoptix Command Line Interface."""
    pass

########################### setFolders

@cli.command()
@click.option('--path', type=str, required=True, help='Path of configuration')
@click.option('--nameFolder', type=str, required=True, help='Name of the folder')
@click.option('--use_absolute', is_flag=True, help='If it uses abs paths')
def setup_folders(path, name, use_absolute):
    """Config folders"""
    setup_simulation_folder(path, nameFolder, use_absolute)
    click.echo(f'Setting up with path: {path}, name: {nameFolder} , absolute: {use_absolute}')

########################### setWeather

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder to retrieve demo')
@click.option('--pathCSV', type=str, required=True, help='CSV path for the variables')
def set_Weather(nameFolder, pathCSV):
    """Set the EPW files"""
    setWeatherFiles_local(nameFolder, pathCSV)

########################### setAnalysisObj

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathfile', type=str, required=True, help='Path to the OCT file used in the simulation')
@click.option('--name', type=str, required=True, help='Name assigned to the analysis object')
@click.option('--hpc', type=bool, required=True, help='Flag to indicate if HPC is used')
def make_analysis_obj(nameFolder, pathfile, name, hpc):
    """Sets the Analysis Object for a bifacial radiance simulation."""
    makeAnalysisObj_Local(nameFolder, pathfile, name, hpc)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathCSV', type=str, required=True, help='CSV path for the variables')
def set_module_analysis(nameFolder, pathCSV):
    """Configures and runs the module analysis for a bifacial radiance simulation."""
    setmoduleAnalysis_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--octfile', type=str, required=True, help='Path to the OCT file used in the simulation')
@click.option('--name', type=str, required=True, help='Name assigned to the analysis object')
@click.option('--frontscan', type=str, required=True, help='Path to the front scan points data')
@click.option('--backscan', type=str, required=True, help='Path to the back scan points data')
@click.option('--plotflag', type=bool, required=True, help='Flag to indicate if the result should be plotted')
@click.option('--accuracy', type=str, required=True, help='Accuracy level for the raytracing simulation (low or high)')
@click.option('--RGB', type=bool, required=True, help='Flag to indicate if analysis should be done in RGB')
def make_analysis(nameFolder, octfile, name, frontscan, backscan, plotflag, accuracy, RGB):
    """Performs the analysis for a bifacial radiance simulation."""
    makeAnalysis_Local(nameFolder, octfile, name, frontscan, backscan, plotflag, accuracy, RGB)

########################### setModules

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathCSV_makeModule', type=str, required=True, help='Path to the CSV file for general module parameters.')
@click.option('--pathCSV_cellModule', type=str, required=True, help='Path to the CSV file for cell module parameters.')
@click.option('--pathCSV_tubeParams', type=str, required=True, help='Path to the CSV file for torque tube parameters.')
@click.option('--pathCSV_omegaParams', type=str, required=True, help='Path to the CSV file for omega profile parameters.')
@click.option('--pathCSV_frameParams', type=str, required=True, help='Path to the CSV file for frame parameters.')
def make_module(nameFolder, pathCSV_makeModule, pathCSV_cellModule, pathCSV_tubeParams, pathCSV_omegaParams, pathCSV_frameParams):
    """Creates a bifacial radiance module based on CSV parameters."""
    makeModule_Local(nameFolder, pathCSV_makeModule, pathCSV_cellModule, pathCSV_tubeParams, pathCSV_omegaParams, pathCSV_frameParams)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file for torque tube parameters.')
def add_torque_tube(nameFolder, pathCSV):
    """Adds a torque tube to a bifacial radiance module."""
    addTorqueTube_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file for cell module parameters.')
def add_cell_module(nameFolder, pathCSV):
    """Adds a cell module to a bifacial radiance module."""
    addCellModule_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file for omega profile parameters.')
def add_omega(nameFolder, pathCSV):
    """Adds an omega profile to a bifacial radiance module."""
    addOmega_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file for frame parameters.')
def add_frame(nameFolder, pathCSV):
    """Adds a frame to a bifacial radiance module."""
    addFrame_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
def show_module(nameFolder):
    """Displays the current module configuration."""
    showModule_Local(nameFolder)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--name', type=str, required=True, help='Name of the module file to read.')
def read_module(nameFolder, name):
    """Reads and loads a module configuration file."""
    readModule_Local(nameFolder, name)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--rewriteModulefile', is_flag=True, help='Rewrite the existing module file with the compiled data.')
@click.option('--json', type=str, required=True, help='JSON string with parameters to compile into the module configuration.')
def compile_text(nameFolder, rewriteModulefile, json):
    """Compiles text data for a module configuration."""
    compileText_Local(nameFolder, rewriteModulefile, json)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--materialPath', type=str, required=True, help='Path to the folder containing material files.')
def return_material_files(nameFolder, materialPath):
    """Returns material file paths for a bifacial radiance simulation."""
    returnMaterialFiles_Local(nameFolder, materialPath)

########################### setScene

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--material', type=str, default=None, help='Material name or albedo value for the ground')
@click.option('--materialFile', type=str, default=None, help='Path to the material file')
def set_Ground(nameFolder, material, materialFile):
    """Set the ground material for the simulation"""
    setGround_Local(nameFolder, material, materialFile)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file containing the parameters')
def set_1axis(nameFolder, pathCSV):
    """Set 1-axis tracker configuration"""
    set1axis_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file containing scene parameters')
def make_Scene(nameFolder, pathCSV):
    """Create a scene based on CSV parameters"""
    makeScene_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file containing parameters')
def make_Scene1axis(nameFolder, pathCSV):
    """Create a 1-axis tracker scene based on CSV parameters"""
    makeScene1axis_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--octname', type=str, required=True, help='Name for the .oct file')
def make_Oct(nameFolder, octname):
    """Generate an .oct file for the simulation"""
    makeOct_Local(nameFolder, octname)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--trackerdict', type=bool, required=True, help='Tracker configuration dictionary')
@click.option('--singleIndex', type=int, required=True, help='Index of the tracker configuration')
@click.option('--customName', type=str, required=True, help='Custom name for the .oct file')
def make_Oct1axis(nameFolder, trackerdict, singleIndex, customName):
    """Generate an .oct file for a 1-axis tracker configuration"""
    makeOct1axis_Local(nameFolder, trackerdict, singleIndex, customName)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
def show_Scene(nameFolder):
    """Display the scene for the simulation"""
    showScene_Local(nameFolder)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathCSV', type=str, required=True, help='Path to the CSV file containing custom object parameters')
def make_CustomObject(nameFolder, pathCSV):
    """Create a custom object based on CSV parameters"""
    makeCustomObject_Local(nameFolder, pathCSV)

@cli.command()
@click.option('--nameFolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--radfile', type=bool, required=True, help='Whether to use a radiance file in the scene')
@click.option('--pathObject', type=str, required=True, help='Path to the custom object file')
@click.option('--text', type=str, required=True, help='Additional text to include with the object in the scene')
def append_to_Scene(nameFolder, radfile, pathObject, text):
    """Append a custom object to the scene"""
    appendtoScene_Local(nameFolder, radfile, pathObject, text)

########################### setSkyDome

@cli.command()
@click.option('--name_folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--gencumsky_path', type=str, required=False, help='Path to the custom gencumsky file. If None, default values are used')
@click.option('--savefile', type=str, required=True, help='Filename to save the cumulative sky file')
def gen_cum_sky(name_folder, gencumsky_path, savefile):
    """Generates a cumulative sky for the simulation folder"""
    genCumSky_Local(name_folder, gencumsky_path, savefile)

@cli.command()
@click.option('--name_folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--trackerdict', type=str, required=True, help='Path to the CSV file with tracker configurations')
def gen_cum_sky_1axis(name_folder, trackerdict):
    """Generates a cumulative sky for a 1-axis tracker configuration"""
    # Load tracker dictionary from CSV
    trackerdict_data = load_data(trackerdict)  # Asumimos que esta función carga el CSV
    genCumSky1axis_Local(name_folder, trackerdict_data)

@cli.command()
@click.option('--name_folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--timeindex', type=int, required=True, help='Time index for which the daylighting data should be generated')
@click.option('--metdata', is_flag=True, help='Flag to use metdata from Radiance object')
@click.option('--debug', is_flag=True, help='Flag for enabling debug mode')
def gen_daylit(name_folder, timeindex, metdata, debug):
    """Generates daylighting data for a specific time index"""
    genDaylit_Local(name_folder, timeindex, metdata, debug)

@cli.command()
@click.option('--name_folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--dni', type=float, required=True, help='Direct normal irradiance (DNI) value')
@click.option('--dhi', type=float, required=True, help='Diffuse horizontal irradiance (DHI) value')
@click.option('--sunalt', type=float, required=True, help='Sun altitude angle')
@click.option('--sunaz', type=float, required=True, help='Sun azimuth angle')
def gen_daylit_manual(name_folder, dni, dhi, sunalt, sunaz):
    """Manually generates daylighting data using specified values"""
    genDaylit2Manual_Local(name_folder, dni, dhi, sunalt, sunaz)

@cli.command()
@click.option('--name_folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--metdata', is_flag=True, help='Flag to use metdata from Radiance object')
@click.option('--trackerdict', type=str, required=True, help='Path to the CSV file with tracker configurations')
def gen_daylit_1axis(name_folder, metdata, trackerdict):
    """Generates daylighting data for a 1-axis tracker configuration"""
    # Load tracker dictionary from CSV
    trackerdict_data = load_data(trackerdict)  # Asumimos que esta función carga el CSV
    genDayLit1Axis_Local(name_folder, metdata, trackerdict_data)

########################### version

@cli.command()
def version():
    """Show up the version."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
