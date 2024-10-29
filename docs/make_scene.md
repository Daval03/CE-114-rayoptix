# Command: `make_scene`

## Description

The `make_scene` command creates a scene for the simulation using bifacial_radiance based on the parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing parameters for scene creation.

### Usage

```bash
make_scene --namefolder <folder_name> --pathcsv <csv_file_path>
```