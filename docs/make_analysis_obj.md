# Command: `make_analysis_obj`

## Description

The `make_analysis_obj` command sets up the analysis object for a bifacial radiance simulation. It requires parameters for the simulation data folder, the path to the OCT file, and the name of the analysis object. Optionally, it allows specifying if high-performance computing (HPC) is used.

## Parameters

- `--namefolder` (str, required): Name of the folder containing simulation data.
- `--pathfile` (str, required): Path to the OCT file used in the simulation.
- `--name`  (str, required): Name assigned to the analysis object.
- `--hpc` (bool, optional): Indicator for using high-performance computing (HPC), default is  `False`.

## Usage

```bash
make_analysis_obj --namefolder <nombre_carpeta> --pathfile <ruta_archivo> --name <nombre_objeto> [--hpc <true/false>]
```

