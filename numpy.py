#Libreria numpy 
import numpy as np

numeros = [1,2,3,4]
array = np.array(numeros)
print (array)
num = np.arange(5,30)
print (num)

#Array multiplo de 4
multiploCuatro = np.arange(0,30,4)
print (multiploCuatro)

#array zeros
arrayCeros = np.zeros(5)
print (arrayCeros)

#array ones
arrayUnos = np.ones((3,2))
print (arrayUnos)

numAleatorios = np.linspace(0,50,5)
print (numAleatorios)

array = np.random.randint(0,100,10)
numMax = array.max()
numMin = array.min()
print (array)

print ('EL numero maximo del array es: ', numMax)
#pocicion del numero maximo
numPosition = array.argmax()
print ('La posision del numero maximo es: ', numPosition)
print ('El numero minimo del array es: ', numMin)

#array mayores a 30
filtro = array > 30
array2 = array[filtro]
print (array2)
