import os
from setuptools import setup, find_packages
from setuptools.command.install import install
import json

class PostInstallCommand(install):
    """Post-installation for creating the JSON file."""
    def run(self):
        # Llamamos al método original de instalación
        install.run(self)
        
        # Definir la ruta para el archivo JSON
        json_file_path = os.path.expanduser('~/.rayoptix/simulation_folders.json')
        
        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(json_file_path), exist_ok=True)
        print(json_file_path)
        # Si el archivo no existe, crearlo con un diccionario vacío
        if not os.path.exists(json_file_path):
            with open(json_file_path, 'w') as json_file:
                json.dump({}, json_file, indent=4)
            print(f"Created JSON file at {json_file_path}")
        else:
            print(f"JSON file already exists at {json_file_path}")

setup(
    name='rayoptix',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Añade tus dependencias aquí
    entry_points={
        'console_scripts': [
            'rayoptix=rayoptix.main:cli',  # Cambia según tu función principal
        ],
    },
    cmdclass={
        'install': PostInstallCommand,  # Vincular el comando de instalación con PostInstallCommand
    },
)
