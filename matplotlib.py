#Libreria matlplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(0,20)
print (x)

y = x**2
print (y)

plt.plot(x,y,'g*')
plt.title('Grafico')
plt.xlabel('Eje de x')
plt.ylabel('Eje de y')
plt.show()


array = np.arange(0,50).reshape(10,5)
print (array)
plt.imshow(array)
plt.colorbar()
plt.show()


array2 = np.random.randint(0,1000,100)
print (array2)
array2 = array2.reshape(10,10)
print ('\n', array2)
plt.imshow(array2)
plt.colorbar()
plt.show()

#graficando datos del achivo .csv
dataframe = pd.read_csv('c:/calif.csv')
print ('\n', dataframe)

dataframe.plot(x='NOMBRE',y='CALIFICACION', kind='bar')
plt.show()
