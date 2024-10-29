# Command: `gen_cum_sky`

## Description

The `gen_cum_sky` command generates a cumulative sky for the simulation folder using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `gencumsky_path` (str, optional): Path to the custom gencumsky file. If None, default values are used.
- `savefile` (str, required): Filename to save the cumulative sky file.

### Usage

```bash
gen_cum_sky --namefolder <folder_name> --gencumsky_path <custom_gencumsky_path> --savefile <filename>
```