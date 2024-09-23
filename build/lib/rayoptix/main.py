import click
from utils.setup_folders import *
from bifacial_radiance.setGround import *

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
def ground(name):
    """Set the ground."""
    ground(name)
    click.echo(f'set ground')


@cli.command()
@click.option('--name', type=str, required=True, help='Name of the folder to retrieve demo')
def function_2(name):
    """F---2."""
    click.echo(f'Valores 2')

@cli.command()
def version():
    """Show up the version."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
