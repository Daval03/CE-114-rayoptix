# Command: `gen_daylit`

## Description

The `gen_daylit` command generates daylighting data for a specific time index using bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `timeindex` (int, required): Time index for which the daylighting data should be generated.
- `metdata` (bool, optional): Flag to indicate whether to use metdata from the Radiance object. Default is False.
- `debug` (bool, optional): Flag for enabling debug mode. Default is False.

### Usage

```bash
gen_daylit --namefolder <folder_name> --timeindex <index> [--metdata] [--debug]
```