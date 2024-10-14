import bifacial_radiance as br
import json

def build_cell_module(radianceObj, cell_data):
    """
    Configures the cell module within the bifacial radiance module using the provided cell data.

    Parameters
    ----------
    moduleObj : object
        The module object that will be configured with cell parameters.
    cell_data : dict
        A dictionary containing the cell module parameters. Expected keys are:
        - 'numcellsx': Number of cells along the x-axis.
        - 'numcellsy': Number of cells along the y-axis.
        - 'xcell': Width of each cell.
        - 'ycell': Height of each cell.
        - 'xcellgap': Gap between cells in the x-axis.
        - 'ycellgap': Gap between cells in the y-axis.
        - 'centerJB': Position of the junction box in the module.
        - 'recompile': Boolean to indicate if recompilation of the module is needed.

    Returns
    -------
    None
    """
    if cell_data is None:
        return
    else:
         # Extract and filter the cell_params 
        cell_params = {key: value for key, value in cell_data.items() if value is not None}

        # Create the cell module with only the parameters that have values
        radianceObj.module.addCellModule(**cell_params)

        print("CellModule has been added")


def build_tube(radianceObj,tube_data):
    """
    Configures the torque tube within the bifacial radiance module using the provided tube data.

    Parameters
    ----------
    moduleObj : object
        The module object that will be configured with torque tube parameters.
    tube_data : dict
        A dictionary containing the tube parameters. Expected keys are:
        - 'diameter': Diameter of the torque tube.
        - 'tubetype': Type of tube (e.g., round or square).
        - 'tubematerial': Material of the tube.
        - 'axisofrotation': Axis around which the tube rotates.
        - 'visible': Boolean indicating if the tube is visible in the simulation.
        - 'recompile': Boolean to indicate if recompilation of the module is needed.

    Returns
    -------
    None
    """
    if tube_data is None:
        return

    # Extract and filter the tube_params 
    tube_params = {key: value for key, value in tube_data.items() if value is not None}

    # Create the torque tube with only the parameters that have values
    radianceObj.module.addTorquetube(**tube_params)

    print("Torquetube has been added")

def build_omega(radianceObj, omega_data):
    """
    Configures the omega profile within the bifacial radiance module using the provided omega data.

    Parameters
    ----------
    moduleObj : object
        The module object that will be configured with omega profile parameters.
    omega_data : dict
        A dictionary containing the omega profile parameters. Expected keys are:
        - 'omega_material': Material of the omega profile.
        - 'omega_thickness': Thickness of the omega profile.
        - 'inverted': Boolean indicating if the omega profile is inverted.
        - 'x_omega1': Horizontal position of the first omega point.
        - 'x_omega3': Horizontal position of the third omega point.
        - 'y_omega': Vertical position of the omega points.
        - 'mod_overlap': Amount of overlap with the module.
        - 'recompile': Boolean to indicate if recompilation of the module is needed.

    Returns
    -------
    None
    """
    if omega_data is None:
        return

    # Extract and filter the omega_params 
    omega_params = {key: value for key, value in omega_data.items() if value is not None}

    # Create the omega profile with only the parameters that have values
    radianceObj.module.addOmega(**omega_params)

    print("Omega has been added")

def build_frame(radianceObj, frame_data):
    """
    Configures the frame of the bifacial radiance module using the provided frame data.

    Parameters
    ----------
    moduleObj : object
        The module object that will be configured with frame parameters.
    frame_data : dict
        A dictionary containing the frame parameters. Expected keys are:
        - 'frame_material': Material of the frame.
        - 'frame_thickness': Thickness of the frame.
        - 'frame_z': Vertical position of the frame.
        - 'nSides_frame': Number of sides of the frame.
        - 'frame_width': Width of the frame.
        - 'recompile': Boolean to indicate if recompilation of the module is needed.

    Returns
    -------
    None
    """
    if frame_data is None:
        return

    # Extract and filter the frame_params 
    frame_params = {key: value for key, value in frame_data.items() if value is not None}

    # Create the frame with only the parameters that have values
    radianceObj.module.addFrame(**frame_params)

    print("Frame has been added")