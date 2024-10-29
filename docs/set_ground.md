# Command: `set_ground`

## Description

The `set_ground` command sets the ground material for the simulation using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `material` (numeric or str, optional): Material name or albedo value to be used for the ground. Default is None.
- `materialfile` (str, optional): Path to the material file. Default is None.

### Usage

```bash
set_ground --namefolder <folder_name> [--material <material_name_or_albedo>] [--materialfile <material_file_path>]
```