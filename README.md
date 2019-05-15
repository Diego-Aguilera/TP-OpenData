# TP-OpenData

Este proyecto consiste en una base de datos CSV abierta del proyecto https://tembiapo.mopc.gov.py.

Tambien inclye un scrapper en python para generar la ultima version de este CSV.

## Para generar el CSV
  
### Requisitos

* Python 3 con:

Pipenv

html-requests

pandas

* OpenRefine

### Instrucciones

* Ejecutar el scrapper.py

```
pipenv run python scrapper.py
```

* Con OpenRefine abrir el archivo results.csv generado, utilizando codificacion UTF-8.

* Aplicar las transformaciones de OpenRefine ubicadas en el archivo transformaciones.txt.

* Exportar el archivo como Comma-Separated Values.

## Licencia

Este proyecto esta bajo la licencia GNU General Public License v3.0 - lee el archivo [LICENSE.md](LICENSE.md) para mas detalles
