# Command: `set_module_analysis`

## Description

The `set_module_analysis` command configures and runs the module analysis for a bifacial radiance simulation, loading parameters from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): The path to the CSV file containing the parameters for the module analysis.

### Usage

```bash
set_module_analysis --namefolder <folder_name> --pathcsv <csv_path>
```