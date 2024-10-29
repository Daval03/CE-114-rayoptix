# Command: `get_timestamp`

## Description

The `get_timestamp` command retrieves a timestamp from the simulation data based on the provided time. If a matching timestamp is found, it is printed to the output; otherwise, a message is displayed indicating that it could not be found.

## Usage

```bash
get_timestamp --namefolder <folder_name> --time <time>
```

## Options

- `--namefolder` (str, required): Name of the folder containing simulation data.
- `--time` (str, required): The specific time to search for in the simulation data.

