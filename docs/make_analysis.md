# Command: `make_analysis`

## Description

The `make_analysis` command performs the analysis for a bifacial radiance simulation using previously defined scan points.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `octfile` (str, required): The path to the OCT file used in the simulation.
- `name` (str, required): The name assigned to the analysis object.
- `frontscan` (str, required): The path to the front scan points data.
- `backscan` (str, required): The path to the back scan points data.
- `plotflag` (bool, optional): Whether to plot the results after the analysis.
- `accuracy` (str, optional): The accuracy level for the ray tracing simulation (low or high).
- `rgb` (bool, optional): Whether to perform the analysis in RGB color format.

### Usage

```bash
make_analysis --namefolder <folder_name> --octfile <oct_file_path> --name <object_name> --frontscan <front_scan_path> --backscan <back_scan_path> [--plotflag <true/false>] [--accuracy <low/high>] [--rgb <true/false>]
```