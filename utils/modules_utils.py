import bifacial_radiance as br
import json

def build_cell_module(moduleObj, cell_data):
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
        numcellsx= cell_data.get('numcellsx')
        numcellsy= cell_data.get('numcellsy')
        xcell= cell_data.get('xcell')
        ycell= cell_data.get('ycell')
        xcellgap= cell_data.get('xcellgap')
        ycellgap= cell_data.get('ycellgap')
        centerJB= cell_data.get('centerJB')
        recompile= cell_data.get('recompile')
        
        moduleObj.addCellModule(numcellsx=numcellsx,
            numcellsy=numcellsy, 
            xcell=xcell, 
            ycell=ycell,
            xcellgap=xcellgap, 
            ycellgap=ycellgap, 
            centerJB=centerJB,
            recompile=recompile)
        print("Bien")

def build_tube(moduleObj,tube_data):
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
    else:
        diameter= tube_data.get('diameter')
        tubetype= tube_data.get('tubetype')
        material= tube_data.get('tubematerial')
        axisofrotation = tube_data.get('axisofrotation')
        visible= tube_data.get('visible')
        recompile= tube_data.get('recompile')
        
        moduleObj.addTorquetube(diameter=diameter,
            tubetype=tubetype, 
            material=material, 
            axisofrotation=axisofrotation,
            visible=visible,
            recompile=recompile)
        print("Bien1")

def build_omega(moduleObj, omega_data):
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
    else:
        omega_material= omega_data.get('omega_material')
        omega_thickness= omega_data.get('omega_thickness')
        inverted= omega_data.get('inverted')
        x_omega1= omega_data.get('x_omega1')
        x_omega3= omega_data.get('x_omega3')
        y_omega= omega_data.get('y_omega')
        mod_overlap= omega_data.get('mod_overlap')
        recompile= omega_data.get('recompile')
        
        moduleObj.addOmega(omega_material=omega_material,
            omega_thickness=omega_thickness, 
            inverted=inverted, 
            x_omega1=x_omega1,
            x_omega3=x_omega3,
            y_omega=y_omega,
            mod_overlap=mod_overlap,
            recompile=recompile)
        print("Bien2")

def build_frame(moduleObj, frame_data):
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
    else:
        frame_material= frame_data.get('frame_material')
        frame_thickness= frame_data.get('frame_thickness')
        frame_z= frame_data.get('frame_z')
        nSides_frame= frame_data.get('nSides_frame')
        frame_width= frame_data.get('frame_width')
        recompile= frame_data.get('recompile')
        
        moduleObj.addFrame(frame_material=frame_material,
            frame_thickness=frame_thickness, 
            frame_z=frame_z, 
            nSides_frame=nSides_frame,
            frame_width=frame_width,
            recompile=recompile)
        print("Bien3")
