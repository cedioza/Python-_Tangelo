from src.routes.country import Country


# instancio la clase Country la cual tiene todas las funciones que ncesito para los requisitos

app=Country() 

# De https://restcountries.com/ obtenga el nombre del idioma que habla el país y encriptelo con SHA1 

# En la columna Time ponga el tiempo que tardó en armar la fila (debe ser automático)
app.getCountries('https://restcountries.com/v3.1/all')

# La tabla debe ser creada en un DataFrame con la librería PANDA
app.createDataFrame()

# Creo la tabla  country en sql
app.createTable()

# inserto las filas de los datos de cada país

app.insertCountries()

# Con funciones de la librería pandas muestre el tiempo total, 
# el tiempo promedio, el tiempo mínimo y el máximo que tardo en procesar todas las filas de la tabla

app.getTimes()
# Genere un Json de la tabla creada y guárdelo como data.json
app.create_json()

