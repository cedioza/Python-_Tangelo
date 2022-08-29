import time
from src.routes.country import Country


# Instancio la clase Country la cual tiene todas las funciones que ncesito para los requisitos

main=Country("country") 

# De https://restcountries.com/ obtenga el nombre del idioma que habla el país y encriptelo con SHA1 

# En la columna Time ponga el tiempo que tardó en armar la fila (debe ser automático)
initial_time = time.time()
main.getCountries('https://restcountries.com/v3.1/all',initial_time)

# La tabla debe ser creada en un DataFrame con la librería PANDA
main.createDataFrame()

# Creo la tabla  country en sql
main.createTable()

# inserto las filas de los datos de cada país

main.insertCountries()

# Con funciones de la librería pandas muestre el tiempo total, 
# el tiempo promedio, el tiempo mínimo y el máximo que tardo en procesar todas las filas de la tabla

main.getTimes()
# Genere un Json de la tabla creada y guárdelo como data.json
main.create_json()

