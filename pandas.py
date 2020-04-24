#Libreria pandas
import pandas as pd
#leer fichero y guardar en variable
dataframe = pd.read_csv('c:/calif.csv')
print (dataframe, '\n')

descripcion = dataframe.describe()
print (descripcion, '\n')
#leer columna
columna = dataframe['NOMBRE']
print (columna, '\n')
#nombre especifico de una posicion
nombre = dataframe['NOMBRE'][0]
print ('El nombre que eligio es: ', nombre, '\n')
#ejemplo de lectura de dos columnas
doscolumnas = dataframe[['NOMBRE','MATERIA']]
print (doscolumnas, '\n')
#calificacion max
maxcal = dataframe['CALIFICACION'] >=70
print (maxcal, '\n')
#aplicacion de filtro
filtro = dataframe['CALIFICACION'] >= 70
dataframe2 = dataframe[filtro]
print (dataframe2, '\n')

#transformar los datos csv a un array
array = dataframe2.values
print (array, '\n')

nombreArray = conversionArray[0,0]
print (nombreArray)
