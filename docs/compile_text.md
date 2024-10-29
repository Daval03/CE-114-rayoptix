# Command: `compile_text`

## Description

The `compile_text` command compiles text data for a bifacial radiance module configuration.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `rewritemodulefile` (bool, optional): If True, rewrites the existing module file with the compiled data.
- `json` (str, required): JSON string with parameters to compile into the module configuration.

### Usage

```bash
compile_text --namefolder <folder_name> [--rewritemodulefile] --json <json_string>
```