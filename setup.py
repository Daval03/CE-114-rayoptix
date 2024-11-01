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
        
        try:
            # Crear el directorio si no existe
            os.makedirs(os.path.dirname(json_file_path), exist_ok=True)    
            # Si el archivo no existe, crearlo con un diccionario vacío
            if not os.path.exists(json_file_path):
                with open(json_file_path, 'w') as json_file:
                    json.dump({}, json_file, indent=4)
                print(f"Created JSON file at {json_file_path}")
            else:
                print(f"JSON file already exists at {json_file_path}")
        
        except Exception as e:
            print(f"Error creating JSON file: {e}")

setup(
    name='rayoptix',  # El nombre de tu paquete en PyPI
    version='1.0.2',  # Asegúrate de actualizar la versión con cada release
    packages=find_packages(),
    install_requires=[
        "bifacial_radiance",
        "pandas",
        "matplotlib",
        "sutil",
        "GPUtil",
        "seaborn",
        "psutil"
    ],
    entry_points={
        'console_scripts': [
            'rayoptix=rayoptix.main:cli',
        ],
    },
    cmdclass={
        'install': PostInstallCommand,
    },
    author="Aldo Cambronero Ureña",  # Tu nombre o el de tu organización
    author_email="cambroneroaldo03@gmail.com",
    description="Rayoptix is a terminal-based Python library for creating and evaluating simulations of bifacial photovoltaic systems using ray tracing. It allows users to define modules, configure experimental conditions, and analyze energy performance in complex solar setups.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Daval03/CE-114-rayoptix",  # URL del repositorio del proyecto
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Ajusta según tu licencia
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',  # Versión mínima de Python requerida
    include_package_data=True,  # Incluye otros archivos especificados en MANIFEST.in
)
