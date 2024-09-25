import pickle
import os
def save_readWeatherFile(folder_path, variable):
    # Save the readWeatherFile variable
    full_path = os.path.join(folder_path, "metadata", "weather.pkl")
    
    with open(full_path, 'wb') as f:
        pickle.dump(variable, f)
    
def load_readWeatherFile(folder_path):
    # Save the readWeatherFile variable
    full_path = os.path.join(folder_path, "metadata", "weather.pkl")
    
    # Cargar la variable desde el archivo
    with open(full_path, 'rb') as f:
        metdata = pickle.load(f)
        return metdata
