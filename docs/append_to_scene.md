# Command: `append_to_scene`

## Description

The `append_to_scene` command appends a custom object to the scene for a bifacial radiance simulation.

### Parameters

- `namefolder` (str, required): The name of the folder that contains the simulation data.
- `radfile` (str, required): Indicates whether to use a radiance file in the scene.
- `pathobject` (str, required): The path to the custom object file to be appended to the scene.
- `text` (str, required): Additional text to include with the object in the scene.

### Usage

```bash
append_to_scene --namefolder <folder_name> --radfile <radiance_file> --pathobject <object_file_path> --text <additional_text>
```