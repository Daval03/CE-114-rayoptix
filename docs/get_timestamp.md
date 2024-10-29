
# Comando: `get_timestamp`

## Descripción

El comando `get_timestamp` recupera una marca de tiempo (timestamp) de los datos de simulación según la hora proporcionada. Si se encuentra una marca de tiempo que coincida, se imprime en la salida; de lo contrario, se informa que no se pudo encontrar.

## Uso

```bash
get_timestamp --namefolder <nombre_carpeta> --time <hora>
```

## Opciones

    --namefolder (str, obligatorio): Nombre de la carpeta que contiene los datos de simulación.
    --time (str, obligatorio): La hora específica a buscar en los datos de simulación.

