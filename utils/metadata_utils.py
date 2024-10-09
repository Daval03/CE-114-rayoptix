import pickle
import os
def save_variable(folder_path, filename, variable):
    """
    Saves a variable to a .pkl file inside the specified folder.

    Parameters
    ----------
    folder_path : str
        Path to the base folder where the .pkl file will be saved.
    filename : str
        Name of the file (without the .pkl extension).
    variable : any
        The variable to be saved in the .pkl file.

    Returns
    -------
    None
    """
    full_path = os.path.join(folder_path, f"{filename}.pkl")
    # Save the variable to the file
    with open(full_path, 'wb') as f:
        pickle.dump(variable, f)

def load_variable(folder_path, filename):
    """
    Loads a variable from a .pkl file inside the specified folder.

    Parameters
    ----------
    folder_path : str
        Path to the base folder where the .pkl file is located.
    filename : str
        Name of the file (without the .pkl extension).

    Returns
    -------
    any
        The variable loaded from the .pkl file.

    Raises
    ------
    FileNotFoundError
        If the specified .pkl file does not exist.
    """
    full_path = os.path.join(folder_path, f"{filename}.pkl")
    
    # Load the variable from the file
    if os.path.exists(full_path):
        with open(full_path, 'rb') as f:
            return pickle.load(f)
    else:
        raise FileNotFoundError(f"File not found: {full_path}")




#metdata= load_readWeatherFile("C:/Users/cambr/Documents/TEMP/T1")
#print(metdata.longitude)
#print(dir(metdata))
#C:\Users\cambr\bifacial_radiance\TEMP\Tutorial_11
#C:\Users\cambr\Documents\TEMP\T1