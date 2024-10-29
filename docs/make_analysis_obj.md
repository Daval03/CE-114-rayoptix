# Comando: `make_analysis_obj`

## Descripción

El comando `make_analysis_obj` configura el objeto de análisis para una simulación de radiancia bifacial. Requiere los parámetros de la carpeta de datos de simulación, la ruta al archivo OCT, y el nombre del objeto de análisis. Opcionalmente, permite especificar si se utiliza computación de alto rendimiento (HPC).

## Uso

```bash
make_analysis_obj --namefolder <nombre_carpeta> --pathfile <ruta_archivo> --name <nombre_objeto> [--hpc <true/false>]
```

## Opciones

- `--namefolder` (str, obligatorio): Nombre de la carpeta que contiene los datos de simulación.
- `--pathfile` (str, obligatorio): Ruta al archivo OCT utilizado en la simulación.
- `--name` (str, obligatorio): Nombre asignado al objeto de análisis.
- `--hpc` (bool, opcional): Indicador de uso de computación de alto rendimiento (HPC), por defecto `False`.
