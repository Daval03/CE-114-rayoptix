# Command: `set_back_scan`

## Description

The `set_back_scan` command updates the back scan parameters for a bifacial radiance simulation using values from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): The path to the CSV file containing back scan parameters.

### Usage

```bash
set_back_scan --namefolder <folder_name> --pathcsv <csv_path>
```