import os
import shutil
import bifacial_radiance as br
import json
import pandas as pd
from utils.folders_utils import move_epws_folder
from utils.metadata_utils import save_variable
from utils.json_folder_utils import load_data
from utils.csv_folder_utils import load_params_from_csv

def setWeatherFiles_local(name_folder, pathCSV):
    """
    Sets the weather file for the simulation folder based on latitude, longitude, and other parameters provided in a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathCSV : str
        Path to the CSV file containing weather-related parameters such as latitude, longitude, start and end time, and other settings.
    """
    pathCSV = os.path.normpath(pathCSV)
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        
        # Combine folder_path with name_folder to get the full path
        full_path = os.path.join(folder_path, name_folder)
        
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)

        csv_weather = load_params_from_csv(pathCSV)

        original_path = os.getcwd()
        os.chdir(folder_path)
        # Retrieve the EPW file based on latitude and longitude
        epwfile = red.getEPW( csv_weather["lat"],
        csv_weather["lon"],
        csv_weather["GetAll"])

        metdata = red.readWeatherFile(weatherFile = epwfile, 
        starttime =csv_weather["starttime"],
        endtime = csv_weather["endtime"],
        label = csv_weather["label"],
        source = csv_weather["source"],
        coerce_year =csv_weather["coerce_year"] ,
        tz_convert_val = csv_weather["tz_convert_val"])
        os.chdir(original_path)
        red.save(red_save)

    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def getTimeStamp_local(name_folder, time):
    """
    Retrieves a timestamp from the simulation data based on the provided time.
    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    time : str
        The time to be converted into a timestamp and matched in the simulation's datetime index.
    Returns
    -------
    pd.Timestamp or None
        The corresponding timestamp if found, otherwise None.
    """
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        
        # Combine folder_path with name_folder to get the full path
        full_path = os.path.join(folder_path, name_folder)
        
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        try:
            return red.metdata.datetime.index(pd.to_datetime(time)) 
        except Exception as e:
            print(f"Error: Could not find the timestamp for the provided time '{time}'. Details: {e}")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

#getTimeStamp_local(name_folder="Test_real", time="5")
#setWeatherFiles_local("Test_1","C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/test_weather.csv")
