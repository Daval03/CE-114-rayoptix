# Command: `make_oct1axis`

## Description

The `make_oct1axis` command generates an .oct file for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `trackerdict` (dict, required): Dictionary of tracker configurations.
- `singleindex` (int, required): Index of the tracker configuration to be used.
- `customname` (str, required): Custom name for the .oct file.

### Usage

```bash
make_oct1axis --namefolder <folder_name> --trackerdict <tracker_configuration_dict> --singleindex <index> --customname <oct_file_name>
```