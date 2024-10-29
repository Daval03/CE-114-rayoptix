# Command: `save_results`

## Description

The `save_results` command generates a heatmap from the results of a bifacial radiance simulation and saves it to a specified path or displays it.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation results.
- `filestarter` (str, required): The prefix used to filter the result files to be processed.
- `output_path` (str, optional): The file path where the heatmap will be saved. If not specified, the heatmap will be displayed instead.

### Usage

```bash
save_results --namefolder <folder_name> --filestarter <file_prefix> [--output_path <output_file_path>]
```