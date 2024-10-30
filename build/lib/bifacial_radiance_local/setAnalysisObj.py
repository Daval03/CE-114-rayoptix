import bifacial_radiance as br
import json
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from utils.json_folder_utils import *
from utils.metadata_utils import *
from utils.csv_folder_utils import load_params_from_csv
from utils.metrics_utils import *

def makeAnalysisObj_Local(name_folder, pathfile, name, hpc):
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
    pathfile = os.path.normpath(pathfile)
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

def setModuleAnalysis_Local(name_folder, pathCSV):
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
    pathCSV = os.path.normpath(pathCSV)
    # Load the data from the JSON file
    data = load_data(json_file)
    
    # Check if the folder name exists in the loaded data
    if name_folder in data:
        # Retrieve the folder path from the JSON data
        folder_path = data[name_folder]
        
        # Load the radianceObj and analysisObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)
        analysis = load_variable(folder_path, "analysis")

        # Load CSV parameters from pathCSV
        analysis_params = load_params_from_csv(pathCSV)        
        scene = analysis_params.get('scene')
        
        if not analysis_params:
            print("CSV files are missing.")
            return
        elif scene:
            # Extract and filter the module analysis parameters
            analysis_filtered_params = {
                'scene': red.scene,
                'modWanted': analysis_params.get('modWanted'),
                'rowWanted': analysis_params.get('rowWanted'),
                'sensorsy': analysis_params.get('sensorsy'),
                'sensorsx': analysis_params.get('sensorsx'),
                'frontsurfaceoffset': analysis_params.get('frontsurfaceoffset'),
                'backsurfaceoffset': analysis_params.get('backsurfaceoffset'),
                'modscanfront': analysis_params.get('modscanfront'),
                'modscanback': analysis_params.get('modscanback'),
                'relative': analysis_params.get('relative'),
                'debug': analysis_params.get('debug')
            }

            # Filter out parameters that have None values
            analysis_filtered_params = {key: value for key, value in analysis_filtered_params.items() if value is not None}
            # Run the moduleAnalysis with the filtered parameters
            frontscan, backscan = analysis.moduleAnalysis(**analysis_filtered_params)
            
            # Save results
            save_variable(folder_path, "frontscan", frontscan)
            save_variable(folder_path, "backscan", backscan)
            print("frontscan and backscan now exist")
        else:
            print("scene is not defined")
            return
        
        # Save the analysis object back
        save_variable(folder_path, "analysis", analysis)
        
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeAnalysis_Local(name_folder, octfile, name, frontscan, backscan, plotflag, accuracy, RGB):
    """
    Performs the analysis for a bifacial radiance simulation using previously defined scan points.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    octfile : str
        The path to the OCT file used in the simulation.
    name : str
        The name assigned to the analysis object.
    frontscan : str
        The path to the front scan points data.
    backscan : str
        The path to the back scan points data.
    plotflag : bool
        Whether to plot the results after the analysis.
    accuracy : str
        The accuracy level for the raytracing simulation (low or high).
    RGB : bool
        Whether to perform the analysis in RGB color format.

    Returns
    -------
    None
    """
    octfile = os.path.normpath(octfile)
    frontscan = os.path.normpath(frontscan)
    backscan = os.path.normpath(backscan)

    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    
    # Check if the folder exists in the data
    if name_folder in data:
        folder_path = data[name_folder]
        analysis = load_variable(folder_path, "analysis")
        
        # Verify that the necessary files exist
        if not os.path.exists(octfile):
            print(f"File '{octfile}' not found.")
            return
        elif not frontscan:
            print(f"File '{frontscan}' not exist.")
            return
        elif not backscan:
            print(f"File '{backscan}' not exist.")
            return
        else:
            frontscan = load_variable(folder_path, "frontscan")
            backscan = load_variable(folder_path, "backscan")
            
            # Extract and filter the analysis parameters
            analysis_filtered_params = {
                'octfile': octfile,
                'name': name,
                'frontscan': frontscan,
                'backscan': backscan,
                'plotflag': plotflag,
                'accuracy': accuracy,
                'RGB': RGB
            }
            
            # Filter out any parameters that have None values
            analysis_filtered_params = {key: value for key, value in analysis_filtered_params.items() if value is not None}
            # Change directory to the folder path and perform the analysis
            original_path = os.getcwd()
            os.chdir(folder_path)
            analysis.analysis(**analysis_filtered_params)
            os.chdir(original_path)
            
            # Save results
            save_variable(folder_path, "frontscan", frontscan)
            save_variable(folder_path, "backscan", backscan)
            
        # Save the analysis object back
        save_variable(folder_path, "analysis", analysis)

    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def setFrontScan(name_folder, pathcsv):
    """
    Updates the front scan parameters for a bifacial radiance simulation using values from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathcsv : str
        The path to the CSV file containing front scan parameters.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    pathcsv = os.path.normpath(pathcsv)
    
    # Check if the folder exists in the data
    if name_folder in data:
        folder_path = data[name_folder]
        
        # Verify that the necessary files exist
        if not os.path.exists(pathcsv):
            print(f"CSV '{pathcsv}' not found.")
            return

        # Load the existing frontscan object
        frontscan = load_variable(folder_path, "frontscan")

        # Extract and filter the frontscan_params 
        frontscan_params = load_params_from_csv(pathcsv)
        frontscan_params = {key: value for key, value in frontscan_params.items() if value is not None}

        # Update the frontscan dictionary with the new values from frontscan_params
        for key, value in frontscan_params.items():
            frontscan[key] = value  

        # Save the updated frontscan object
        save_variable(folder_path, "frontscan", frontscan)

        print(f"Frontscan updated successfully in folder '{name_folder}'.")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def setBackScan(name_folder, pathcsv):
    """
    Updates the back scan parameters for a bifacial radiance simulation using values from a CSV file.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    pathcsv : str
        The path to the CSV file containing back scan parameters.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    pathcsv = os.path.normpath(pathcsv)
    # Check if the folder exists in the data
    if name_folder in data:
        folder_path = data[name_folder]
        
        # Verify that the necessary files exist
        if not os.path.exists(pathcsv):
            print(f"CSV '{pathcsv}' not found.")
            return

        # Load the existing frontscan object
        backscan = load_variable(folder_path, "backscan")

        # Extract and filter the backscan_params 
        backscan_params = load_params_from_csv(pathcsv)
        backscan_params = {key: value for key, value in backscan_params.items() if value is not None}

        # Update the frontscan dictionary with the new values from backscan_params
        for key, value in backscan_params.items():
            backscan[key] = value  

        # Save the updated backscan object
        save_variable(folder_path, "backscan", backscan)

        print(f"Backscan updated successfully in folder '{name_folder}'.")
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def makeMultiAnalysis_Local(name_folder, sensorsx, sensorsy, p, octfile):
    """
    Executes multiple analyses on a bifacial radiance simulation based on the specified sensor configuration.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation data.
    sensorsx : int
        The number of sensors along the x-axis for the ground scan.
    sensorsy : int
        The number of sensors along the y-axis for the ground scan.
    p : float
        The parameter used for spacing calculations between sensors in the y-direction.
    octfile : str
        The path to the oct file that will be used for analysis.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    
    # Check if the folder exists in the data
    if name_folder in data:
        folder_path = data[name_folder]
        
        # Load the radianceObj and analysisObj
        red_save = os.path.join(folder_path, "save.pickle")
        red = br.load.loadRadianceObj(red_save)  
        analysis = load_variable(folder_path, "analysis")

        original_path = os.getcwd()
        os.chdir(folder_path)
        startgroundsample=-red.module.scenex
        spacingbetweensamples = (red.module.scenex*(40/sensorsx))/(sensorsx-1)

        #  Measure start time, memory, CPU, and GPU usage
        start_time = time.monotonic()
        start_mem, start_cpu = get_memory_cpu_usage()
        start_gpu_load, start_gpu_mem = get_gpu_usage()
        start_disk_read, start_disk_write = get_disk_usage()
        start_mem_read, start_mem_write = get_memory_bandwidth()
        start_cache_mem = get_cache_memory_usage()
        start_swap_mem = get_swap_memory_usage()
        start_cpu_freq, max_cpu_freq = get_cpu_frequency()

        for i in range (0, sensorsx): # Will map 20 points
            frontscan, backscan = analysis.moduleAnalysis(red.scene, sensorsy=sensorsy)
            groundscan = frontscan
            groundscan['zstart'] = 0.05  # setting it 5 cm from the ground.
            groundscan['zinc'] = 0   # no tilt necessary.
            groundscan['yinc'] = (p*(22/sensorsy))/(sensorsy-1)   # increasing spacing so it covers all distance between rows
            groundscan['xstart'] = startgroundsample + i*spacingbetweensamples   # increasing spacing so it covers all distance between rows
            analysis.analysis(octfile, red.name+"_groundscan_"+str(i), groundscan, backscan)  # compare the back vs front irradiance

        # Measure end time, memory, CPU, and GPU usage
        end_time = time.monotonic()
        end_mem, end_cpu = get_memory_cpu_usage()
        end_gpu_load, end_gpu_mem = get_gpu_usage()
        end_disk_read, end_disk_write = get_disk_usage()
        end_mem_read, end_mem_write = get_memory_bandwidth()
        end_cache_mem = get_cache_memory_usage()
        end_swap_mem = get_swap_memory_usage()
        end_cpu_freq, _ = get_cpu_frequency()

        os.chdir(original_path)

        # Print timing, memory usage, CPU usage, and GPU usage information
        print(f"Execution Time: {timedelta(seconds=end_time - start_time)}")
        print(f"Memory Usage: {end_mem - start_mem:.2f} MB")
        print(f"CPU Usage: {end_cpu:.2f}%")
        if end_gpu_load is not None:
            print(f"GPU Load: {end_gpu_load:.2f}%")
            print(f"GPU Memory Usage: {end_gpu_mem:.2f} GB")
        print(f"Disk Read: {end_disk_read - start_disk_read:.2f} MB")
        print(f"Disk Write: {end_disk_write - start_disk_write:.2f} MB")
        print(f"Memory Read: {end_mem_read - start_mem_read:.2f} MB")
        print(f"Memory Write: {end_mem_write - start_mem_write:.2f} MB")
        print(f"Cache Memory Usage: {end_cache_mem - start_cache_mem:.2f} MB")
        print(f"Swap Memory Usage: {end_swap_mem - start_swap_mem:.2f} MB")
        print(f"CPU Frequency: {end_cpu_freq:.2f} MHz (Max: {max_cpu_freq:.2f} MHz)")
    
    else:
        # Display an error if the folder is not found in the JSON data
        print(f"Folder '{name_folder}' not found.")

def saveResults_Local(name_folder, filestarter, output_path=None):
    """
    Generates a heatmap from the results of a bifacial radiance simulation and saves it to a specified path or displays it.

    Parameters
    ----------
    name_folder : str
        The name of the folder that contains the simulation results.
    filestarter : str
        The prefix used to filter the result files to be processed.
    output_path : str, optional
        The file path where the heatmap will be saved. If None, the heatmap will be displayed instead.

    Returns
    -------
    None
    """
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    data = load_data(json_file)
    
    # Check if the folder exists in the data
    if name_folder in data:
        folder_path = data[name_folder]
        filelist = sorted(os.listdir(os.path.join(folder_path, 'results')))
        prefixed = [filename for filename in filelist if filename.startswith(filestarter)]

        arrayWm2Front = []
        arrayWm2Back = []
        arrayMatFront = []
        arrayMatBack = []
        filenamed = []
        faillist = []

        print('{} files in the directory'.format(filelist.__len__()))
        print('{} groundscan files in the directory'.format(prefixed.__len__()))
        i = 0  # counter to track # files loaded.

        for i in range(len(prefixed)):
            ind = prefixed[i].split('_')
            file_path = os.path.join(folder_path, 'results', prefixed[i])
            try:
                resultsDF = br.load.read1Result(file_path)
                arrayWm2Front.append(list(resultsDF['Wm2Front']))
                arrayWm2Back.append(list(resultsDF['Wm2Back']))
                arrayMatFront.append(list(resultsDF['mattype']))
                arrayMatBack.append(list(resultsDF['rearMat']))
                filenamed.append(prefixed[i])
            except Exception as e:
                print(f" FAILED {i} {prefixed[i]}: {e}")
                faillist.append(prefixed[i])
         # Create DataFrame from the collected results
        resultsdf = pd.DataFrame(list(zip(arrayWm2Front, arrayWm2Back,
                                           arrayMatFront, arrayMatBack)),
                                 columns=['br_Wm2Front', 'br_Wm2Back',
                                          'br_MatFront', 'br_MatBack'])
        resultsdf['filename'] = filenamed
        
        # Save the DataFrame to a CSV file
        output_file = os.path.join(folder_path, 'results', 'consolidated_results.csv')
        resultsdf.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")

        df3 = pd.DataFrame(resultsdf['br_Wm2Front'].to_list())
        reversed_df = df3.T.iloc[::-1]
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        ax = sns.heatmap(reversed_df, cmap='viridis', linewidths=0, linecolor=None, cbar_kws={'label': 'Irradiation (Wh/m2)'})
        ax.set_yticks([])
        ax.set_xticks([])
        ax.set_ylabel('')
        ax.set_xlabel('')
        if output_path:
            plt.savefig(output_path, bbox_inches='tight')
            print(f"Heatmap saved to {output_path}")
        else:
            plt.show()
        plt.close()




#save_or_show_heatmap("C:/Users/cambr/bifacial_radiance/TEMP/Test_real/results/consolidated_results.csv")
#makePDF_Local("Test_real","irr_Test_real_groundscan")   
#makeMultiAnalysis_Local("Test_real", 20, 20, 1, "C:/Users/cambr/bifacial_radiance/TEMP/Test_real/Test_real.oct")

#def makeMultiAnalysis_Local(name_folder, sensorsx, sensorsy, p, octfile):
#setFrontScan("Test_real", "C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/back-frontscan_params.csv")

##Modified frontscan and backscan files frontscan, backscan = analysis.moduleAnalysis(scene, sensorsy=sensorsy)

#print("hola")
# makeAnalysis_Local(name_folder="Test_real", 
# octfile="C:/Users/cambr/bifacial_radiance/TEMP/Test_real/Test_real.oct", 
# name="Test_real_groundscan", 
# frontscan=True, 
# backscan=True, 
# plotflag=None, 
# accuracy=None, 
# RGB=None)

#makeAnalysisObj_Local(name_folder="Test_1", pathfile="C:/Users/cambr/bifacial_radiance/TEMP/Tutorial_11/tutorial_11.oct", name=None, hpc=False)

#setModuleAnalysis_Local(name_folder="Test_real", 
#pathCSV="C:/Users/cambr/Documents/Proyecto_CE-114/rayoptix/tests/moduleAnalysis_params.csv")

