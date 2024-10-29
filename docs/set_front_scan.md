# Command: `set_front_scan`

## Description

The `set_front_scan` command updates the front scan parameters for a bifacial radiance simulation using values from a CSV file.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv` (str, required): The path to the CSV file containing front scan parameters.

### Usage

```bash
set_front_scan --namefolder <folder_name> --pathcsv <csv_path>
```