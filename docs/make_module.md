# Command: `make_module`

## Description

The `make_module` command creates a bifacial radiance module based on parameters from multiple CSV files and saves it to the simulation folder.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `pathcsv_makemodule` (str, optional): Path to the CSV file for general module parameters such as dimensions, number of panels, and gaps.
- `pathcsv_cellmodule` (str, optional): Path to the CSV file for cell-level parameters for the module.
- `pathcsv_tubeparams` (str, optional): Path to the CSV file for tube-related parameters for the module.
- `pathcsv_omegaparams` (str, optional): Path to the CSV file for omega-related parameters for the module.
- `pathcsv_frameparams` (str, optional): Path to the CSV file for frame-related parameters for the module.

### Usage

```bash
make_module --namefolder <folder_name> [--pathcsv_makemodule <csv_path_make_module>] [--pathcsv_cellmodule <csv_path_cell_module>] [--pathcsv_tubeparams <csv_path_tube_params>] [--pathcsv_omegaparams <csv_path_omega_params>] [--pathcsv_frameparams <csv_path_frame_params>]
```