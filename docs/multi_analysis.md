# Command: `multi_analysis`

## Description

The `multi_analysis` command runs a multi-point analysis for bifacial radiance. It executes multiple analyses on a bifacial radiance simulation based on the specified sensor configuration.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `sensorsx` (int, required): The number of sensors along the x-axis for the ground scan.
- `sensorsy` (int, required): The number of sensors along the y-axis for the ground scan.
- `p` (float, required): The parameter used for spacing calculations between sensors in the y-direction.
- `octfile` (str, required): The path to the oct file that will be used for analysis.

### Usage

```bash
multi_analysis --namefolder <folder_name> --sensorsx <number_of_sensors_x> --sensorsy <number_of_sensors_y> --p <pitch_value> --octfile <oct_file_path>
```