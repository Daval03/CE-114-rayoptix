import os
import csv
def convert_value(value):
    """Convert the string value to an appropriate type (int, float, None, bool, or str)."""
    if isinstance(value, list):  # Check if value is a list
        return ', '.join(map(str, value))  # Join list elements as a string
    elif isinstance(value, str):  # Only convert if it's a string
        value = value.strip()
        if value.lower() in ['true', '1']:  # Convert to boolean True
            return True
        elif value.lower() in ['false', '0']:  # Convert to boolean False
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
    """Reads a CSV file and returns a list of dictionaries with all its data."""
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
    """Load CSV and return the first row of parameters."""
    params = get_csv(path)
    return params[0] if params else None