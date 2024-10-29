# Command: `add_torque_tube`

## Description

The `add_torque_tube` command adds a torque tube to a bifacial radiance module based on parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing torque tube parameters such as diameter, material, and visibility.

### Usage

```bash
add_torque_tube --namefolder <folder_name> --pathcsv <csv_path>
```