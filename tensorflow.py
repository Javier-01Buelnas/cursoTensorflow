#sintaxis basica de tensorflow
import tensorflow as tf

mensaje1= tf.constant("Hola ")
mensaje2= tf.constant("Mundo")
 
with tf.Session() as sesion:
    resultado = sesion.run(mensaje1 + mensaje2)

print resultado

a = tf.constant(10)
b = tf.constant(5)

with tf.Session() as sesion:
    result = sesion.run(a + b)

print result

constant = tf.constant(15)
matriz1 = tf.file((6,6)10) 
matriz2 = tf.random_normal((5,5)) 
matriz3 = tf.random_uniform((4,4),minval=0, maxval=5) 
matriz_cero=tf.zeros((2,2))
matriz_unos = tf.ones((3,3))

operaciones = [constante, matriz1, matriz2, matriz3, matriz_cero, matriz_unos]

with tf.Session() as sesion:
    for op in operaciones:
        print(sesion.run(op))
        print("\n")
