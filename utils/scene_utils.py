from bifacial_radiance import *

def set_ground_properties(radianceobj, ground_type):
    """
    Set the ground properties for the 'demo' object based on the type of ground.
    
    Parameters:
    - radianceobj: The object with a 'ground' attribute whose properties need to be updated. 
            (This is probably a bifacial_radiance.RadianceObj, but hey, whatever floats your boat.)
    - ground_type (str): A string representing the type of ground you want. 
                         Choose wisely from the following options:
                         "litesoil", "concrete", "white_EPDM", "beigeroof", 
                         "beigeroof_lite", "beigeroof_heavy", "black", or "asphalt".

    Raises:
    - ValueError: If the ground_type is not recognized. Yeah, we're strict like that. 
    
    Example usage:
        radianceobj = bifacial_radiance.RadianceObj(simulationName, path=testfolder)
        radianceobj.setGround()  
        set_ground_properties(radianceobj, "concrete")
        print(radianceobj.ground.ReflAvg)  # Outputs 0.2815
    """
    
    # Our trusty dictionary that stores ground properties for different types of surfaces
    ground_data = {
        "litesoil": {
            "ReflAvg": 0.2133, "Rrefl": 0.29, "Grefl": 0.187, "Brefl": 0.163, "normval": 0.208151
        },
        "concrete": {
            "ReflAvg": 0.2815, "Rrefl": 0.364, "Grefl": 0.257, "Brefl": 0.2235, "normval": 0.2785671
        },
        "white_EPDM": {
            "ReflAvg": 0.7997, "Rrefl": 0.863, "Grefl": 0.791, "Brefl": 0.745, "normval": 0.8059202
        },
        "beigeroof": {
            "ReflAvg": 0.427, "Rrefl": 0.547, "Grefl": 0.395, "Brefl": 0.339, "normval": 0.4251318
        },
        "beigeroof_lite": {
            "ReflAvg": 0.2983, "Rrefl": 0.388, "Grefl": 0.273, "Brefl": 0.234, "normval": 0.2959524
        },
        "beigeroof_heavy": {
            "ReflAvg": 0.2487, "Rrefl": 0.321, "Grefl": 0.228, "Brefl": 0.197, "normval": 0.246625
        },
        "black": {
            "ReflAvg": 0.01, "Rrefl": 0.01, "Grefl": 0.01, "Brefl": 0.01, "normval": 0.010034
        },
        "asphalt": {
            "ReflAvg": 0.1, "Rrefl": 0.1, "Grefl": 0.1, "Brefl": 0.1, "normval": 0.10034
        }
    }

    # Check if the provided ground type is valid
    if ground_type in ground_data:
        # Grab the values for this ground type
        values = ground_data[ground_type]
        
        # Update the radianceobj.ground attributes with the new values
        radianceobj.ground.ReflAvg = values["ReflAvg"]
        radianceobj.ground.Rrefl = values["Rrefl"]
        radianceobj.ground.Grefl = values["Grefl"]
        radianceobj.ground.Brefl = values["Brefl"]
        radianceobj.ground.normval = values["normval"]
        radianceobj.ground.ground_type = ground_type
    else:
        # Throw an error if the ground type doesn't exist, no funny business here!
        raise ValueError(f"Ground type '{ground_type}' not recognized.")

def str_to_bool(value):
    """
    Converts a string to a boolean value.
    Parameters
    ----------
    value : str
        The string value to convert (e.g., 'true', 'false', '1', '0').

    Returns
    -------
    bool
        The corresponding boolean value.
    
    Raises
    ------
    ValueError
        If the value cannot be converted to a boolean.
    """
    # Convertir a minúsculas para asegurar que no sea sensible a mayúsculas/minúsculas
    value = value.lower()
    
    # Definir los valores que deberían considerarse como True
    if value in ['true', '1', 'yes', 'y']:
        return True
    # Definir los valores que deberían considerarse como False
    elif value in ['false', '0', 'no', 'n']:
        return False
    else:
        # Opción para manejar valores que no son ni True ni False válidos
        raise ValueError(f"Cannot convert {value} to a boolean.")
