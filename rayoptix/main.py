import click
from rayoptix.setup_folders import setup_simulation_folder


@click.group()
def cli():
    """Rayoptix Command Line Interface."""
    pass

@cli.command()
@click.option('--path', type=str, required=True, help='Path of configuration')
@click.option('--name', type=str, required=True, help='Name of the folder')
@click.option('--use_absolute', is_flag=True, help='If it uses abs paths')
def setup_folders(path, name, use_absolute):
    """Configura el entorno."""
    setup_simulation_folder(path, name, use_absolute)
    click.echo(f'Setting up with path: {path}, name: {name} , absolute: {use_absolute}')

@cli.command()
@click.option('--name', type=str, required=True, help='Name of the folder to retrieve demo')
def function_1(name):
    """F_1."""
    click.echo(f'Valores guardados')


@cli.command()
@click.option('--name', type=str, required=True, help='Name of the folder to retrieve demo')
def function_2(name):
    """F_2."""
    click.echo(f'Valores guardados')

@cli.command()
def version():
    """Show up the versio."""
    click.echo('Rayoptix version 0.1.0')

if __name__ == '__main__':
    cli()
