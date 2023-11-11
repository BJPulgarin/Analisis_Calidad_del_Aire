import pandas as pd
import requests
import sqlite3

# importar datos Ciudades
url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
data = pd.read_csv(url, sep=';')

# parsear datos: Concentrations para cada City
registros = []
cont = 1
def cargarRegistro(ciudad, concentraciones, contador):
    registro = {'city': ciudad, 'overall_aqi': concentraciones['overall_aqi']}
    for key in concentraciones:
        if isinstance(concentraciones[key], dict) and 'concentration' in concentraciones[key]:
            registro[key] = concentraciones[key]['concentration']
    registros.append(registro)
    print(f'Registro numero {contador} añadido')

# Limpieza de tabla Ciudades
del data['Race']
del data['Count']
del data['Number of Veterans']
data.drop_duplicates(inplace=True)

# Establecer lista de ciudades luego de limpiar para no traer registros repetidos
cities = data['City']
for city in cities:
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'HE13V9zEkVqINUGixrZdQg==ppS2Lv7A6j9yBMbO'})
    if response.status_code == requests.codes.ok:
        concentrations = response.json()
        cargarRegistro(city, concentrations, cont)
        cont += 1

df_aqis = pd.DataFrame(registros)

# Exportando a la base de datos
con = sqlite3.connect('calidad_del_aire.db')
df_aqis.to_sql('Concentrations', con, if_exists='replace', index=False)
data.to_sql('Cities', con, if_exists='replace', index=False)
con.close()
