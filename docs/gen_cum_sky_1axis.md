# Command: `gen_cum_sky_1axis`

## Description

The `gen_cum_sky_1axis` command generates a cumulative sky for a 1-axis tracker configuration in the simulation folder using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `trackerdict` (str, required): Path to the CSV file with tracker configurations.

### Usage

```bash
gen_cum_sky_1axis --namefolder <folder_name> --trackerdict <path_to_tracker_config_csv>
```