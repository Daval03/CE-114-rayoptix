# Command: `add_frame`

## Description

The `add_frame` command adds a frame to a bifacial radiance module based on parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing frame parameters such as material, thickness, and number of sides.

### Usage

```bash
add_frame --namefolder <folder_name> --pathcsv <csv_path>
```