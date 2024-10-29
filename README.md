# Rayoptix

`Rayoptix` is a Python library designed to run from the terminal. It facilitates the creation and evaluation of simulations for complex bifacial photovoltaic systems using ray tracing techniques. With this tool, users can define modules, set up experimental conditions, and run simulations to analyze the energy performance of these systems.

## Installation

To install `Rayoptix`, simply run:

```bash
pip install rayoptix
```

Note: It is necessary to have the Radiance and bifacial_radiance libraries installed beforehand.

## Function Documentation

For more details on each of the functions in `Rayoptix`, please refer to the specific documentation:

- [Folder Setup (`setup_folders`)](docs/setup_folders.md): Allows creating and configuring folders to store simulation configurations.
- [Create Module (`make_module`)](docs/make_module.md): Creates a bifacial radiance module based on CSV parameters.
- [Add Torque Tube (`add_torque_tube`)](docs/add_torque_tube.md): Adds a torque tube to a bifacial radiance module.
- [Add Cell Module (`add_cell_module`)](docs/add_cell_module.md): Adds a cell module to a bifacial radiance module.
- [Add Omega Profile (`add_omega`)](docs/add_omega.md): Adds an omega profile to a bifacial radiance module.
- [Add Frame (`add_frame`)](docs/add_frame.md): Adds a frame to a bifacial radiance module.
- [Show Module (`show_module`)](docs/show_module.md): Displays the current module configuration.
- [Read Module (`read_module`)](docs/read_module.md): Reads and loads a module configuration file.
- [Compile Text (`compile_text`)](docs/compile_text.md): Compiles text data for a module configuration.
- [Return Material Files (`return_material_files`)](docs/return_material_files.md): Returns material file paths for a bifacial radiance simulation.
- [Set Ground (`set_ground`)](docs/set_ground.md): Sets the ground material for the simulation.
- [Set 1-Axis Tracker (`set_1axis`)](docs/set_1axis.md): Sets the 1-axis tracker configuration for the simulation.
- [Create Scene (`make_scene`)](docs/make_scene.md): Creates a scene based on CSV parameters.
- [Create 1-Axis Tracker Scene (`make_scene1axis`)](docs/make_scene1axis.md): Creates a 1-axis tracker scene based on CSV parameters.
- [Generate OCT File (`make_oct`)](docs/make_oct.md): Generates an .oct file for the simulation.
- [Generate 1-Axis OCT File (`make_oct1axis`)](docs/make_oct1axis.md): Generates an .oct file for a 1-axis tracker configuration.
- [Show Scene (`show_scene`)](docs/show_scene.md): Displays the scene for the simulation.
- [Create Custom Object (`make_customobject`)](docs/make_customobject.md): Creates a custom object based on CSV parameters.
- [Append to Scene (`append_to_scene`)](docs/append_to_scene.md): Appends a custom object to the scene.
- [Generate Cumulative Sky (`gen_cum_sky`)](docs/gen_cum_sky.md): Generates a cumulative sky for the simulation folder.
- [Generate Cumulative Sky for 1-Axis Tracker (`gen_cum_sky_1axis`)](docs/gen_cum_sky_1axis.md): Generates a cumulative sky for a 1-axis tracker configuration.
- [Generate Daylighting Data (`gen_daylit`)](docs/gen_daylit.md): Generates daylighting data for a specific time index.
- [Manually Generate Daylighting Data (`gen_daylit_manual`)](docs/gen_daylit_manual.md): Manually generates daylighting data using specified values.
- [Generate Daylighting Data for 1-Axis Tracker (`gen_daylit_1axis`)](docs/gen_daylit_1axis.md): Generates daylighting data for a 1-axis tracker configuration.


Each link leads to detailed documentation on how to use the corresponding commands, their options, and usage examples.