# Command: `gen_daylit_manual`

## Description

The `gen_daylit_manual` command manually generates daylighting data for the simulation folder using specified values in bifacial_radiance.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `dni` (float, required): Direct normal irradiance (DNI) value.
- `dhi` (float, required): Diffuse horizontal irradiance (DHI) value.
- `sunalt` (float, required): Sun altitude angle.
- `sunaz` (float, required): Sun azimuth angle.

### Usage

```bash
gen_daylit_manual --namefolder <folder_name> --dni <dni_value> --dhi <dhi_value> --sunalt <sun_altitude> --sunaz <sun_azimuth>
```