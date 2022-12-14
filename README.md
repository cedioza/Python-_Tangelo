
# Repositorio prueba técnica de Tangelo en Python


### Librerías :
- Pandas: [Pandas](https://pandas.pydata.org/docs/getting_started/install.html)

- Requests: [Requests](https://pypi.org/project/requests/)


## Instalación

Instalar con pip:

```
$ pip install -r requirements.txt
```

## Estructura 
```
.
|──────src/
| |────routes/
| | |────country.py
| |────config/
| | |────database.py
| |────utils/
| | |────encrypt.py
|──────json/
|──────database/
|──────main.py

```


## Tabla Requerida


|   Región             |City Name|Language|Time
|----------------|-------------------------------|-----------------------------|-----------------------------|
|África'            |Angola|AF4F4762F9BD3FOF4A10CAF5B6E63DC4CE543724|0.23 ms             


Desarrolle una aplicación en python que genere la tabla anterior teniendo las siguientes consideraciones:

De https://restcountries.com/ obtenga el nombre del idioma que habla el país y encriptelo con SHA1 

En la columna Time ponga el tiempo que tardó en armar la fila (debe ser automático)

La tabla debe ser creada en un DataFrame con la librería PANDAS 

Con funciones de la librería pandas muestre el tiempo total, el tiempo promedio, el tiempo mínimo y el máximo que tardo en procesar todas las filas de la tabla

Guarde el resultado en sqlite

Genere un Json de la tabla creada y guárdelo como data.json

La prueba debe ser entregada en un repositorio git.
