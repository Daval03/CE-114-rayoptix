# Command: `add_cell_module`

## Description

The `add_cell_module` command adds a cell module to a bifacial radiance module based on parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): Path to the CSV file containing cell module parameters such as the number of cells, gaps, and junction box.

### Usage

```bash
add_cell_module --namefolder <folder_name> --pathcsv <csv_path>
```