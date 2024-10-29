
# Comando: `set_weather`

## Descripción

El comando `set_weather` configura los archivos meteorológicos para la carpeta de simulación usando los parámetros de latitud, longitud, hora de inicio y fin, y otros ajustes especificados en un archivo CSV. Si se proporcionan correctamente, los archivos meteorológicos se configuran y se almacenan en la carpeta especificada.

## Uso

```bash
set_weather --namefolder <nombre_carpeta> --pathcsv <ruta_csv>
```
## Opciones

    --namefolder (str, obligatorio): Nombre de la carpeta que contiene los datos de simulación.
    --pathcsv (str, obligatorio): Ruta al archivo CSV con los parámetros.


