# Repo para EIEC - DevOps - UNIR - Bryan Ron

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutar los comandos Python directamente.

## Ejecución

```bash
python3 main.py <filename> <remove_duplicates> <order>
```

### Parámetros:
- `filename`: **ruta** al fichero que contiene la lista de palabras, una por línea
- `remove_duplicates`: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista
- `order`: **asc|desc**, asc para orden ascendente, desc para orden descendente

## Ejemplos de Uso

### Ejemplo 1: Orden ascendente con eliminación de duplicados
```bash
python3 main.py palabras.txt yes asc
```

**Salida esperada:**
```
Reading words from file: palabras.txt
Remove duplicates: True
Sort order: ascending
Sorted word list:
['apple', 'banana', 'cherry', 'grape', 'kiwi', 'mango', 'orange', 'pineapple', 'strawberry', 'watermelon', 'zebra']
```

### Ejemplo 2: Orden descendente sin eliminar duplicados
```bash
python3 main.py palabras.txt no desc
```

**Salida esperada:**
```
Reading words from file: palabras.txt
Remove duplicates: False
Sort order: descending
Sorted word list:
['zebra', 'zebra', 'zebra', 'watermelon', 'strawberry', 'pineapple', 'orange', 'mango', 'kiwi', 'grape', 'cherry', 'banana', 'banana', 'apple', 'apple', 'apple']
```

### Ejemplo 3: Orden ascendente sin eliminar duplicados
```bash
python3 main.py palabras.txt no asc
```

**Salida esperada:**
```
Reading words from file: palabras.txt
Remove duplicates: False
Sort order: ascending
Sorted word list:
['apple', 'apple', 'apple', 'banana', 'banana', 'cherry', 'grape', 'kiwi', 'mango', 'orange', 'pineapple', 'strawberry', 'watermelon', 'zebra', 'zebra', 'zebra']
```

## Comandos del Makefile

### Ejecución con Docker
```bash
make run
```

### Ejecución local (sin Docker)
```bash
make run-local              # Con eliminación de duplicados, orden ascendente
make run-local-no-duplicates # Sin eliminar duplicados, orden ascendente  
make run-local-desc         # Con eliminación de duplicados, orden descendente
```

## Archivo de Ejemplo

El proyecto incluye `palabras.txt` con frutas de ejemplo que contiene duplicados para demostrar la funcionalidad del programa.
