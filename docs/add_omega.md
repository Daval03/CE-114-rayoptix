# Command: `add_omega`

## Description

The `add_omega` command adds an omega profile to a bifacial radiance module based on parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing omega profile parameters such as material, thickness, and overlap.

### Usage

```bash
add_omega --namefolder <folder_name> --pathcsv <csv_path>
```