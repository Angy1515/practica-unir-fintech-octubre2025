# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

### Uso directo con Python

bash
python3 main.py <filename> <dup> <order>


*Parámetros:*
- filename: *ruta* al fichero que contiene la lista de palabras, una por línea
- dup: *yes|no*, yes para eliminar palabras duplicadas, no para mantener la lista
- order: *asc|desc*, asc para orden ascendente, desc para orden descendente

### Uso con Makefile

bash
# Ejecución local (sin Docker)
make run-local

# Ejecución con Docker
make run


## Ejemplo de ejecución

### Contenido del archivo palabras.txt:

zebra
apple
computer
butterfly
mountain
ocean
elephant


### Ejecutando la aplicación:

bash
$ python main.py palabras.txt yes asc
Se leerán las palabras del fichero palabras.txt
['apple', 'butterfly', 'computer', 'elephant', 'mountain', 'ocean', 'zebra']


bash
$ python main.py palabras.txt no desc
Se leerán las palabras del fichero palabras.txt
['zebra', 'ocean', 'mountain', 'elephant', 'computer', 'butterfly', 'apple']


### Con Makefile:

bash
$ make run-local
python main.py palabras.txt yes asc
Se leerán las palabras del fichero palabras.txt
['adventure', 'apple', 'butterfly', 'chocolate', 'computer', 'courage', 'discovery', 'elephant', 'freedom', 'guitar', 'harmony', 'journey', 'mountain', 'ocean', 'rainbow', 'serenity', 'sunshine', 'universe', 'wisdom', 'zebra']
