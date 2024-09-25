import click
from utils.folders_utils import *
from bifacial_radiance_local.setGround import ground
from bifacial_radiance_local.setWeather import set_WeatherFiles

@click.group()
def cli():
    """Rayoptix Command Line Interface."""
    pass

@cli.command()
@click.option('--path', type=str, required=True, help='Path of configuration')
@click.option('--name', type=str, required=True, help='Name of the folder')
@click.option('--use_absolute', is_flag=True, help='If it uses abs paths')
def setup_folders(path, name, use_absolute):
    """Config folders"""
    setup_simulation_folder(path, name, use_absolute)
    click.echo(f'Setting up with path: {path}, name: {name} , absolute: {use_absolute}')

@cli.command()
@click.option('--name', type=str, required=True, help='Name of the folder to retrieve demo')
@click.option('--material', type=str, required=False, help='Material name or albedo value for the ground')
@click.option('--material_file', type=bool, required=False, help='Path to the material file')
def set_ground(name, material, material_file):
    """Set the ground."""
    # Try to convert material to a float if it represents a number
    if material is not None:
        try:
            material = float(material)
            # Ensure the number is between 0 and 1 for albedo
            if not (0 <= material <= 1):
                raise ValueError("Material albedo value must be between 0 and 1.")
        except ValueError:
            # If the conversion fails, material is assumed to be a string (material name)
            pass
    ground(name, material, material_file)



@cli.command()
@click.option('--name', type=str, required=True, help='Name of the folder to retrieve demo')
@click.option('--pathCSV', type=str, required=True, help='')
def set_Weather(name, pathCSV):
    """Set the EPW files"""
    set_WeatherFiles(name, pathCSV)


@cli.command()
def version():
    """Show up the version."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
