# Command: `gen_daylit_1axis`

## Description

The `gen_daylit_1axis` command generates daylighting data for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `metdata` (bool): Flag to use metdata from the Radiance object. If False, metdata is set to None.
- `trackerdict` (str, required): Path to the CSV file with tracker configurations.

### Usage

```bash
gen_daylit_1axis --namefolder <folder_name> --metdata [--trackerdict <tracker_config_path>]
```