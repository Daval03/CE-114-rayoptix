import pickle
import os
def save_variable(folder_path, filename, variable):
    """
    Saves a variable to a .pkl file inside the 'metadata' folder.
    
    :param folder_path: Path to the base folder.
    :param filename: Name of the file (without the .pkl extension).
    :param variable: The variable to be saved.
    """
    full_path = os.path.join(folder_path, "metadata", f"{filename}.pkl")
        
    # Save the variable to the file
    with open(full_path, 'wb') as f:
        pickle.dump(variable, f)

def load_variable(folder_path, filename):
    """
    Loads a variable from a .pkl file inside the 'metadata' folder.
    
    :param folder_path: Path to the base folder.
    :param filename: Name of the file (without the .pkl extension).
    :return: The variable loaded from the file.
    """
    full_path = os.path.join(folder_path, "metadata", f"{filename}.pkl")
    
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