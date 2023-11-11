ANÁLISIS DE CALIDAD DEL AIRE  

Para el proyecto, ya realizamos la respectiva limpieza y 
generamos la base de datos correspondiente.  

En la base de datos podemos observar dos tablas:
- Cities: _Contiene la información demográfica de cada ciudad._  
- Concentrations: _Contiene la información de la calidad del aire; concentraciones de los contaminantes e indice de calidad del aire._  

Consultas en SQL:  

Para realizar el respectivo análisis y poder sacar conclusiones de nuestro conjunto de datos, realizamos una serie
de consultas en lenguaje SQL.  

La consulta principal fue buscar las ciudades con mayor AQI, puesto que son las que peor calidad del aire presentan. 
La consulta usada fue la siguiente:  

_SELECT c.*, c2.*  
FROM Cities c  
JOIN Concentrations c2  
ON c.City = c2.city  
ORDER BY c2.overall_aqi DESC  
LIMIT 10;_

| Ciudad            | Edad Media | Población Masculina | Población Femenina | Población Total | Población de extranjeros | AQI |
|-------------------|------------|---------------------|--------------------|-----------------|--------------------------|-----|
| Syracuse          | 30.3       | 69462.0             | 74690.0            | 144152          | 17733.0                  | 222 |
| Long Beach        | 34.6       | 238159.0            | 236013.0           | 474172          | 127764.0                 | 206 |
| Clovis            | 37.8       | 52392.0             | 51780.0            | 104172          | 13409.0                  | 204 |
| Fresno            | 30.0       | 256130.0            | 263942.0           | 520072          | 103453.0                 | 203 |
| Mesa              | 36.9       | 234998.0            | 236835.0           | 471833          | 57492.0                  | 200 |
| Worcester         | 34.9       | 90951.0             | 93855.0            | 184806          | 36907.0                  | 200 |
| Gilbert           | 33.2       | 116711.0            | 130812.0           | 247523          | 24531.0                  | 200 |
| Tempe             | 28.8       | 91350.0             | 84476.0            | 175826          | 26620.0                  | 200 |
| Scottsdale        | 46.9       | 115712.0            | 121132.0           | 236844          | 27207.0                  | 200 |
| Salinas           | 30.4       | 77765.0             | 79621.0            | 157386          | 58693.0                  | 200 |
_Las tablas no son exactas, muestran una idea general del resultado de la consulta._

Revisando los datos obtenidos, pudimos observar que la ciudad con peor calidad del aire era Syracuse, y observando más adetalle se puede notar que esto es debido a
su gran concentracion de contaminantes industriales (PM2.5 y PM10), es por esto que se procedió a realizar
otra consulta en SQL, para obtener las ciudades que presentan mayor concentración de PM2.5 y PM10. La consulta
usada fue la siguiente:  

_SELECT Cities.City, (Concentrations."PM2.5" + Concentrations."PM10") AS total_PM  
FROM Cities  
JOIN Concentrations  
ON Cities.City = Concentrations.city  
ORDER BY total_PM DESC  
LIMIT 10;_  

| Ciudad        | Concentración PM |
|---------------|-------------------|
| Syracuse      | 352.64            |
| Alexandria    | 213.46            |
| Yuma          | 160.96            |
| Bethlehem     | 118.81            |
| New Britain   | 71.36             |
| Medford       | 68.0              |
| Quincy        | 67.83             |
| Somerville    | 67.83             |
| Boston        | 67.83             |
| Lynn          | 67.79             |
_Las tablas no son exactas, muestran una idea general del resultado de la consulta._

Como podemos observar, efectivamente Syracuse, por su gran
actividad industrial, está presentando altos niveles de contaminación. Pero esto no acaba aquí,
porque aunque ya encontramos la razón de que Syracuse sea la ciudad con peor calidad del aire, aún
no podemos decir que es la razón por la que todas las otras ciudades están así.
  
Volviendo a la asignación, la idea es consultar si las ciudades más pobladas son las que tienen peor
calidad del aire, para eso realizamos la siguiente consulta:

_SELECT c.*, c2.overall_aqi  
FROM Cities c  
JOIN Concentrations c2  
ON c.City = c2.city  
ORDER BY c."Total Population" DESC  
LIMIT 10;_  

| Ciudad           | Poblacion Masculina | Población Femenina | Población Total | Población Extranjera | AQI |
|------------------|---------------------|--------------------|-----------------|----------------------|-----|
| New York         | 4081698.0           | 4468707.0          | 8550405         | 3212500.0            | 49  |
| Los Angeles      | 1958998.0           | 2012898.0          | 3971896         | 1485425.0            | 162 |
| Chicago          | 1320015.0           | 1400541.0          | 2720556         | 573463.0             | 57  |
| Houston          | 1149686.0           | 1148942.0          | 2298628         | 696210.0             | 80  |
| Philadelphia     | 741270.0            | 826172.0           | 1567442         | 205339.0             | 73  |
| Phoenix          | 786833.0            | 776168.0           | 1563001         | 300702.0             | 137 |
| San Antonio      | 721405.0            | 748419.0           | 1469824         | 208046.0             | 43  |
| San Diego        | 693826.0            | 701081.0           | 1394907         | 373842.0             | 187 |
| Dallas           | 639019.0            | 661063.0           | 1300082         | 326825.0             | 37  |
| San Jose         | 518317.0            | 508602.0           | 1026919         | 401493.0             | 191 |
_Las tablas no son exactas, muestran una idea general del resultado de la consulta._

Para abordar la interrogante sobre si las ciudades más pobladas presentan la peor calidad del aire, la conclusión es un claro NO. Estas ciudades no se encuentran ni cerca de ser catalogadas como las de peor calidad del aire. Este veredicto se atribuye principalmente a que la población no constituye un factor determinante por sí solo en este análisis. La evaluación de la calidad del aire depende de una serie de factores, que incluyen, pero no se limitan a, la población. Elementos como la influencia de la industria en la ciudad, el turismo, las políticas locales y hasta el tipo predominante de actividad económica desempeñan un papel crucial.

Los datos proporcionados nos ofrecen una visión más precisa, aunque no exhaustiva, de los factores que podrían influir en la calidad del aire en las ciudades analizadas. Aunque no podemos concluir con certeza por qué estas ciudades específicas se encuentran entre las más contaminadas, sí nos orientan hacia las áreas de enfoque necesarias para obtener respuestas más claras a nuestras preguntas.

_Brajan Pulgarin._
