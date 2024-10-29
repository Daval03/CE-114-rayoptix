# Command: `make_scene1axis`

## Description

The `make_scene1axis` command creates a 1-axis tracker scene for the simulation using bifacial_radiance based on the parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing parameters for 1-axis tracker scene creation.

### Usage

```bash
make_scene1axis --namefolder <folder_name> --pathcsv <csv_file_path>
```