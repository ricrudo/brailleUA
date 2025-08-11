## Conversor MusicXML → BRF (Braille ASCII) con `music21`

Este script permite convertir un archivo **MusicXML** (o MXL / MusicXML comprimido) a un archivo **BRF** en notación braille ASCII, listo para ser usado en embosadoras o lectores de braille.

### Uso

1. Coloca el script y el archivo de origen en la misma carpeta.
2. Desde la terminal, ejecuta:

```bash
python xml_a_brf_music21.py archivo_origen
```

> **Ejemplo**
> Si tu archivo se llama `title_sonata_composer_bach.mxl`:
>
> ```bash
> python xml_a_brf_music21.py title_sonata_composer_bach.mxl
> ```
>
> Esto generará automáticamente `title_sonata_composer_bach.brf` en la misma carpeta.

### Formato recomendado para el nombre del archivo

Para aprovechar la detección automática de título y compositor, se recomienda que el archivo de origen use el siguiente formato:

```
title_<titulo>_composer_<compositor>.<extensión>
```

* `<titulo>` → Nombre de la obra (sin espacios, usar guiones bajos o medios).
* `<compositor>` → Nombre del compositor.
* `<extensión>` → Puede ser `xml`, `mxl` o `musicxml`.

**Ejemplos válidos:**

* `title_sonata_composer_bach.xml`
* `title_fuga_composer_Bach.mxl`
* `title_etude.xml`
* `composer_beethoven.mxl`

### Salida

* El script creará un archivo `.brf` en la misma carpeta que el archivo original.
* El contenido estará en **Braille ASCII (6 puntos)**, con un ancho de línea típico de 40 caracteres.
