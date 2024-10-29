
# Command: `set_weather`

## Description

The `set_weather` command configures the weather files for the simulation folder using parameters for latitude, longitude, start and end times, and other settings specified in a CSV file. If provided correctly, the weather files are set up and stored in the specified folder.

## Usage

```bash
set_weather --namefolder <folder_name> --pathcsv <csv_path>
```

## Options

- `--namefolder` (str, required): Name of the folder containing simulation data.
- `--pathcsv` (str, required): Path to the CSV file with parameters.


