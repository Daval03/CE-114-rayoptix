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
@click.option('--namefolder', type=str, required=True, help='Name of the folder')
def setup_folders(path, namefolder):
    """Config folders"""
    create_folder(folder_path=path, name_folder=namefolder)
    click.echo(f'Setting up with path: {path}, name: {namefolder}')

########################### setWeather

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder to retrieve demo')
@click.option('--pathcsv', type=str, required=True, help='CSV path for the variables')
def set_weather(namefolder, pathcsv):
    """Set the EPW files"""
    setWeatherFiles_local(namefolder, pathcsv)

########################### setAnalysisObj

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathfile', type=str, required=True, help='Path to the OCT file used in the simulation')
@click.option('--name', type=str, required=True, help='Name assigned to the analysis object')
@click.option('--hpc', type=bool, required=False, help='Flag to indicate if HPC is used')
def make_analysis_obj(namefolder, pathfile, name, hpc):
    """Sets the Analysis Object for a bifacial radiance simulation."""
    makeAnalysisObj_Local(namefolder, pathfile, name, hpc)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='CSV path for the variables')
def set_module_analysis(namefolder, pathcsv):
    """Configures and runs the module analysis for a bifacial radiance simulation."""
    setModuleAnalysis_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--octfile', type=str, required=True, help='Path to the OCT file used in the simulation')
@click.option('--name', type=str, required=True, help='Name assigned to the analysis object')
@click.option('--frontscan', type=bool, required=True, help='Path to the front scan points data')
@click.option('--backscan', type=bool, required=True, help='Path to the back scan points data')
@click.option('--plotflag', type=bool, required=False, help='Flag to indicate if the result should be plotted')
@click.option('--accuracy', type=str, required=False, help='Accuracy level for the raytracing simulation (low or high)')
@click.option('--rgb', type=bool, required=False, help='Flag to indicate if analysis should be done in RGB')
def make_analysis(namefolder, octfile, name, frontscan, backscan, plotflag, accuracy, rgb):
    """Performs the analysis for a bifacial radiance simulation."""
    makeAnalysis_Local(namefolder, octfile, name, frontscan, backscan, plotflag, accuracy, rgb)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing front scan parameters')
def set_front_scan(namefolder, pathcsv):
    """Updates the front scan parameters for a bifacial radiance simulation."""
    setFrontScan(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing back scan parameters')
def set_back_scan(namefolder, pathcsv):
    """Updates the back scan parameters for a bifacial radiance simulation."""
    setBackScan(namefolder, pathcsv)

@cli.command()
@click.option('--name-folder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--sensorsx', type=int, required=True, help='Number of sensors in the X direction')
@click.option('--sensorsy', type=int, required=True, help='Number of sensors in the Y direction')
@click.option('--p', type=float, required=True, help='Pitch value for the analysis')
@click.option('--octfile', type=str, required=True, help='Octree file for the analysis')
def multi_analysis(name_folder, sensorsx, sensorsy, p, octfile):
    """Runs a multi-point analysis for bifacial radiance."""
    makeMultiAnalysis_Local(name_folder, sensorsx, sensorsy, p, octfile)


########################### setModules

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathcsv_makemodule', type=str, required=False, help='Path to the CSV file for general module parameters.')
@click.option('--pathcsv_cellmodule', type=str, required=False, help='Path to the CSV file for cell module parameters.')
@click.option('--pathcsv_tubeparams', type=str, required=False, help='Path to the CSV file for torque tube parameters.')
@click.option('--pathcsv_omegaparams', type=str, required=False, help='Path to the CSV file for omega profile parameters.')
@click.option('--pathcsv_frameparams', type=str, required=False, help='Path to the CSV file for frame parameters.')
def make_module(namefolder, pathcsv_makemodule, pathcsv_cellmodule, pathcsv_tubeparams, pathcsv_omegaparams, pathcsv_frameparams):
    """Creates a bifacial radiance module based on CSV parameters."""
    makeModule_Local(namefolder, pathcsv_makemodule, pathcsv_cellmodule, pathcsv_tubeparams, pathcsv_omegaparams, pathcsv_frameparams)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file for torque tube parameters.')
def add_torque_tube(namefolder, pathcsv):
    """Adds a torque tube to a bifacial radiance module."""
    addTorqueTube_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file for cell module parameters.')
def add_cell_module(namefolder, pathcsv):
    """Adds a cell module to a bifacial radiance module."""
    addCellModule_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file for omega profile parameters.')
def add_omega(namefolder, pathcsv):
    """Adds an omega profile to a bifacial radiance module."""
    addOmega_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file for frame parameters.')
def add_frame(namefolder, pathcsv):
    """Adds a frame to a bifacial radiance module."""
    addFrame_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
def show_module(namefolder):
    """Displays the current module configuration."""
    showModule_Local(namefolder)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--name', type=str, required=True, help='Name of the module file to read.')
def read_module(namefolder, name):
    """Reads and loads a module configuration file."""
    readModule_Local(namefolder, name)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--rewritemodulefile', is_flag=True, help='Rewrite the existing module file with the compiled data.')
@click.option('--json', type=str, required=True, help='JSON string with parameters to compile into the module configuration.')
def compile_text(namefolder, rewritemodulefile, json):
    """Compiles text data for a module configuration."""
    compileText_Local(namefolder, rewritemodulefile, json)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder containing the simulation data.')
@click.option('--materialpath', type=str, required=True, help='Path to the folder containing material files.')
def return_material_files(namefolder, materialpath):
    """Returns material file paths for a bifacial radiance simulation."""
    returnMaterialFiles_Local(namefolder, materialpath)

########################### setScene

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--material', callback=validate_material, default=None, help='Material name or albedo value for the ground')
@click.option('--materialfile', type=str, default=None, help='Path to the material file')
def set_ground(namefolder, material, materialfile):
    """Set the ground material for the simulation"""
    setGround_Local(namefolder, material, materialfile)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing the parameters')
def set_1axis(namefolder, pathcsv):
    """Set 1-axis tracker configuration"""
    set1axis_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing scene parameters')
def make_scene(namefolder, pathcsv):
    """Create a scene based on CSV parameters"""
    makeScene_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing parameters')
def make_scene1axis(namefolder, pathcsv):
    """Create a 1-axis tracker scene based on CSV parameters"""
    makeScene1axis_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--octname', type=str, required=False, help='Name for the .oct file')
def make_oct(namefolder,octname):
    """Generate an .oct file for the simulation"""
    makeOct_Local(namefolder,octname)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--trackerdict', type=bool, required=True, help='Tracker configuration dictionary')
@click.option('--singleindex', type=int, required=True, help='Index of the tracker configuration')
@click.option('--customname', type=str, required=True, help='Custom name for the .oct file')
def make_oct1axis(namefolder, trackerdict, singleindex, customname):
    """Generate an .oct file for a 1-axis tracker configuration"""
    makeOct1axis_Local(namefolder, trackerdict, singleindex, customname)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
def show_scene(namefolder):
    """Display the scene for the simulation"""
    showScene_Local(namefolder)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--pathcsv', type=str, required=True, help='Path to the CSV file containing custom object parameters')
def make_customobject(namefolder, pathcsv):
    """Create a custom object based on CSV parameters"""
    makeCustomObject_Local(namefolder, pathcsv)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--radfile', type=str, required=True, help='Whether to use a radiance file in the scene')
@click.option('--pathobject', type=str, required=True, help='Path to the custom object file')
@click.option('--text', type=str, required=True, help='Additional text to include with the object in the scene')
def append_to_scene(namefolder, radfile, pathobject, text):
    """Append a custom object to the scene"""
    appendtoScene_Local(namefolder, radfile, pathobject, text)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--time', type=str, required=True, help='The time to look up in the simulation data')
def get_timestamp(namefolder, time):
    """Retrieve a timestamp from the simulation data"""
    timestamp = getTimeStamp_local(namefolder, time)
    if timestamp:
        print(f"Timestamp found: {timestamp}")
    else:
        print(f"Timestamp for time '{time}' could not be found.")

########################### setSkyDome

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--gencumsky_path', type=str, required=False, help='Path to the custom gencumsky file. If None, default values are used')
@click.option('--savefile', type=str, required=True, help='Filename to save the cumulative sky file')
def gen_cum_sky(namefolder, gencumsky_path, savefile):
    """Generates a cumulative sky for the simulation folder"""
    genCumSky_Local(namefolder, gencumsky_path, savefile)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--trackerdict', type=str, required=True, help='Path to the CSV file with tracker configurations')
def gen_cum_sky_1axis(namefolder, trackerdict):
    """Generates a cumulative sky for a 1-axis tracker configuration"""
    # Load tracker dictionary from CSV
    genCumSky1axis_Local(namefolder, trackerdict)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--timeindex', type=int, required=True, help='Time index for which the daylighting data should be generated')
@click.option('--metdata', is_flag=True,required=False, help='Flag to use metdata from Radiance object')
@click.option('--debug', is_flag=True,required=False, help='Flag for enabling debug mode')
def gen_daylit(namefolder, timeindex, metdata, debug):
    """Generates daylighting data for a specific time index"""
    genDaylit_Local(namefolder, timeindex, metdata, debug)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--dni', type=float, required=True, help='Direct normal irradiance (DNI) value')
@click.option('--dhi', type=float, required=True, help='Diffuse horizontal irradiance (DHI) value')
@click.option('--sunalt', type=float, required=True, help='Sun altitude angle')
@click.option('--sunaz', type=float, required=True, help='Sun azimuth angle')
def gen_daylit_manual(namefolder, dni, dhi, sunalt, sunaz):
    """Manually generates daylighting data using specified values"""
    genDaylit2Manual_Local(namefolder, dni, dhi, sunalt, sunaz)

@cli.command()
@click.option('--namefolder', type=str, required=True, help='Name of the folder that contains the simulation data')
@click.option('--metdata', is_flag=True, help='Flag to use metdata from Radiance object')
@click.option('--trackerdict', type=str, required=True, help='Path to the CSV file with tracker configurations')
def gen_daylit_1axis(namefolder, metdata, trackerdict):
    """Generates daylighting data for a 1-axis tracker configuration"""
    genDayLit1Axis_Local(namefolder, metdata, trackerdict)

########################### version

@cli.command()
def version():
    """Show up the version."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
