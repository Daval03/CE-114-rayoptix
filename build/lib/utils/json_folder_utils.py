import json
import os
# Function to load data from a JSON file
def load_data(json_file):
    """Loads data from a JSON file if it exists, otherwise returns an empty dictionary."""
    if os.path.exists(json_file):
        with open(json_file, 'r') as file:
            return json.load(file)
    return {}

# Function to save data to a JSON file
def save_data(json_file, data):
    """Saves the given data to a JSON file."""
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Function to check if the name_folder already exists in the JSON file
def check_unique_name(data, name_folder):
    """Checks if the name_folder is unique in the JSON file."""
    return name_folder not in data

def validate_folders_in_json(data):
    """Checks if folder paths stored in the JSON file exist. If not, removes them from the JSON."""
    json_file = os.path.expanduser('~/.rayoptix/simulation_folders.json')
    try:
        updated_data = {}
        removed_entries = []

        # Check if each folder path exists
        for name_folder, folder_path in data.items():
            if isinstance(folder_path, str) and os.path.exists(folder_path):
                updated_data[name_folder] = folder_path
            else:
                removed_entries.append(name_folder)

        # Save the updated data (only valid paths)
        save_data(json_file, updated_data)

        # Report the results
        if removed_entries:
            print(f"Removed the following invalid entries: {', '.join(removed_entries)}")
        else:
            print("All folder paths are valid.")

    except Exception as e:
        print(f"Error validating folders: {e}")

print("Todo bien")