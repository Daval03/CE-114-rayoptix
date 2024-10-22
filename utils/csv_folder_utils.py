import os
import csv
def convert_value(value):
    """
    Convert the string value to an appropriate type (int, float, None, bool, or str).

    Parameters
    ----------
    value : str or list
        The value to be converted. Can be a string, list, or already typed value.

    Returns
    -------
    int, float, None, bool, str
        Returns the converted value. Converts to int or float if possible, 
        booleans for 'true'/'false' values, None for empty strings, 
        or returns the original string or list.
    """
    if isinstance(value, list):  # Check if value is a list
        return ', '.join(map(str, value))  # Join list elements as a string
    elif isinstance(value, str):  # Only convert if it's a string
        value = value.strip()
        if value.lower() in ['true']:  # Convert to boolean True
            return True
        elif value.lower() in ['false']:  # Convert to boolean False
            return False
        if value == "":
            return None  # Convert empty strings to None
        try:
            # Try to convert to float first
            return float(value) if '.' in value or 'e' in value.lower() else int(value)
        except ValueError:
            return value  # If conversion fails, return the original string
    return value  # Return the value as is if it's not a string or list

def get_csv(pathCSV):
    """
    Reads a CSV file and returns a list of dictionaries with all its data.

    Parameters
    ----------
    pathCSV : str
        The path to the CSV file to be read.

    Returns
    -------
    list of dict or None
        Returns a list of dictionaries where each dictionary represents a row from the CSV file. 
        If the file cannot be found or decoded, returns None.
    """
    data = []
    try:
        # Open the CSV file
        with open(pathCSV, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Use DictReader to read rows as dictionaries
            for row in reader:
                # Convert each value in the row using the convert_value function
                converted_row = {key: convert_value(value) for key, value in row.items()}
                data.append(converted_row)  # Each row is now a dictionary with converted values
    except FileNotFoundError:
        print(f"Error: The file {pathCSV} was not found.")
        return None  # Return None on error
    except UnicodeDecodeError:
        print(f"Error: The file {pathCSV} could not be decoded. Check the file encoding.")
        return None  # Return None on error
    except Exception as e:
        print(f"Error reading {pathCSV}: {e}")
        return None  # Return None on error

    return data


def load_params_from_csv(path):
    """
    Convert the string value to an appropriate type (int, float, None, bool, or str).

    Parameters
    ----------
    path : str or None
        Path to the CSV file. If None, the function will return None.

    Returns
    -------
    int, float, None, bool, str
        Returns the converted value. Converts to int or float if possible, 
        booleans for 'true'/'false' values, None for empty strings, 
        or returns the original string or list. Returns None if path is None or 
        the path does not exist.
    """
    if path is None:
        return None
    elif not os.path.exists(path):
        print("Path doesn't exist.")
        return None
    else:
        path = os.path.normpath(path)
        params = get_csv(path)
        return params[0]
