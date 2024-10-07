import click
from utils.folders_utils import *
from bifacial_radiance_local.setScene import *
from bifacial_radiance_local.setWeather import setWeatherFiles_local

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
@click.option('--pathCSV', type=str, required=True, help='CSV path for the variables')
def set_Weather(name, pathCSV):
    """Set the EPW files"""
    setWeatherFiles_local(name, pathCSV)


@cli.command()
def version():
    """Show up the version."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
