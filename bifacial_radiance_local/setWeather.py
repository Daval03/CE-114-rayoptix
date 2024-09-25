import os
import shutil
import bifacial_radiance as br
import json
#setup_folders
from utils.json_folder_utils import load_data
from utils.csv_folder_utils import getWeather_csv
from utils.metadata_utils import save_readWeatherFile
from utils.folders_utils import move_epws_folder

def set_WeatherFiles(name_folder, pathCSV):
    
    # Path to the JSON file where simulation folders are stored
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    
    # Load the data from the JSON file
    data = load_data(json_file)
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        
        # Combine folder_path with name_folder to get the full path
        full_path = os.path.join(folder_path, name_folder)

        # Load the Radiance object using the full path
        red = br.load.loadRadianceObj(full_path)

        csv_weather = getWeather_csv(pathCSV)
        
        # Retrieve the EPW file based on latitude and longitude
        epwfile = red.getEPW( csv_weather[0]["lat"],
        csv_weather[0]["lon"],
        csv_weather[0]["GetAll"])

        metdata = red.readWeatherFile(weatherFile = epwfile, 
        starttime =csv_weather[0]["starttime"],
        endtime = csv_weather[0]["endtime"],
        label = csv_weather[0]["label"],
        source = csv_weather[0]["source"],
        coerce_year =csv_weather[0]["coerce_year"] ,
        tz_convert_val = csv_weather[0]["tz_convert_val"])
        save_readWeatherFile(folder_path, metdata)

        move_epws_folder(folder_path)

    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")


set_WeatherFiles("T1","bifacial_radiance_local/test.csv")
