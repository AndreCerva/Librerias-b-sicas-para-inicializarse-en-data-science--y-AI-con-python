# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 23:42:01 2021

@author: andre
"""
import numpy as np #Numeric+Python=NumPy libreria para trabajar con array
from datetime import datetime #Importamos libreria para el tiempo local
#vectores
lista=[1,2,3,2,1,2]
vector=np.array(lista)
#¿Diferencia entre vector y lista?
#El vector al estar hecho en np nos permite
# realizarle operaciones de forma más sencilla
print("Vector original")
print(vector)
print("Sumarle a cada valor del vector un 3")
print(vector+3)
print("Multiplicar a cada valor del vector por 5")
print(vector*5)
print("Sumar todos los elementos del vector")
print(np.sum(vector))
print("Promediar los elementos del vector")
print(np.mean(vector))
print("El vector sumandose a si mismo")
print(vector+vector)
print("Suma de dos vectores distintos entre ellos, mismo tamaño")
print("También se puede acceder a algun valor en especifico del vector"
      "\ntal cual se hace en una lista")
print(vector[:])
print(vector[5])
print(vector[2:5])
print(vector[0:6])
print(vector[-1])
print("Vector de ceros")
ceros=np.zeros(5)
print("Vector de unos")
unos=np.ones(5)
print("Vector con todos los elementos (5) con valor 2")
vector2=np.ones(5)*2
print(vector2)
#Matrices
#Para vectores se utilizan listas
#Para matrices se utilizan listas de listas
print("Matriz creada de una lista de listas")
listadelista=[[1,2,3],[2,4,5],[6,5,4],[8,2,0]]
matriz=np.array(listadelista)
print(matriz)
print("Matriz creada con numpy,zeros")
matriz_ceros=np.zeros((2,3),dtype=int)
print(matriz_ceros)
#Crear copias de otra matriz con np.copy
#print(np.__version__)Ver versión de un elemento
#Array colección de elementos, todos del mismo tipo de dato
#Array de numpy más rápido que las listas de python y consume menos memoria
arreglo=np.array([1,2,3,4,5,6,7,8,9,1])#Se crea un arreglo de 10 numeros con el metodo array
arreglo*10 #Cuando se realiza una operación básica, se le realiza a cada elemento del arreglo
#help(np.array) para ver ayuda acerca de como utilizar el metodo array de numpy
arreglo2D=np.array([[1,2,3],
                   [4,5,6]]) #Se separa la dimención entre corchetes
#así para n cantidad de dimensiones
arreglo3D = np.array([[[1,2,3],[4,5,6]],[[10,2,3],[4,5,6]]]) 
#arreglox.ndim para ver el numero de dimensiones del array
#num de corchetes antes de los numeros define la n dimensión del arrelgo
#Tamaño de elementos en un array array.size
print(arreglo[0])#Primer ubicación del arreglo
print(arreglo[-10])#Comienza a contar desde el final cuando es un numero negativo
print(arreglo[0]-arreglo[-10])#Se pueden realizar operaciones entre ubicaciones
print(arreglo2D[0,1])#Accedemos a la ubicación 0,1 del arreglo2D 
#arreglo[inicio : final]
print(arreglo[0:5])
#Si no se pone un numero o el inicio o final, toma todos los valores antes o despues de ese
print(arreglo[:])
#arreglo[inicio : final : cadacuanto]
print(arreglo[:6:2])
print(arreglo2D[0:2, 0:2])#arreglo[ #rango de filas , #rango de columnas]
lista=[i for i in range(1000000)]#Creamos una lista de 1M de elementos
inicio=datetime.now()#Capturamos el tiempo en el que se creo la lista
lista=[i+3 for i in lista]#añadimos 3 a cada elemento de la lista
final=datetime.now()#Capturamos el tiempo en el que realizo la operacion
tiempo=(final-inicio)#Diferencia de tiempos
print(tiempo)
arreglo1=np.array([i for i in range(1000000)])#Creamos un arreglo de 1M de elementos
inicio=datetime.now()#Capturamos el tiempo en el que se creo el arreglo
arreglo1 +=3 #Sumamos 3 en cada elemento del arreglo
final=datetime.now()#Capturamos el tiempo en el que se realizó esta operación
tiempo=(final-inicio)#Diferencia de tiempos
print(tiempo)
print(f'La dimensión del primer arreglo es: {arreglo.shape}')
print(f'La dimension del segundo arreglo es: {arreglo2D.shape}')#Shape metodo para la dimension
print(f'La dimensión del tercer arreglo es: {arreglo3D.shape}')
array2to1=arreglo2D.reshape(-1) #reshape para cambiar dimension, -1 para hacer cualq a 1 dim
busqueda=np.where(arreglo==1)#Buscar donde se encuentra dentro de x arreglo un x valor
adesordenado=np.array([1,7,3,4,2,2,3,2,2,4,4,97,542,45563,235,0,6,2,42,2])
aarreglado=np.sort(adesordenado)#metodo sort para ordenar un array
anombresd=np.array(['Alexandra','María','Ivonne','Azula','Alma'])
anombresa=np.sort(anombresd)#También ordena strings
adesordenado2d=np.array([[1,6,2],[7,4,1]])
aordenados2d=np.sort(adesordenado2d)#También ordena arrays de varias dimensiones
filtro=arreglo>3#Regresa verdadero en la posicion en donde se cumple
arraynew=arreglo[filtro]#Se crea un vector donde este verdadero
arange=np.arange(10)#arange para crear un array de una n cantidad de elementos
arange2=np.arange(5,10)#primer parametro es inicio, el segundo es stop
arange3=np.arange(0,20,2)#start,stop,step
#Recordar el help, help(np.arange)
ceros=np.zeros(5,dtype=int)#Crear arrays de cualquier dimension de ceros
unos=np.ones((2,4),dtype=int)#También se puede de 1 en lugar de 0
randuniform=np.random.rand(10)#Distribución de valores muy uniformemente
randnormal=np.random.randn(10)#Distribución de valores normal, en forma de campana
array1=np.array([1,2,3,4])
array2=np.array([5,6,7,8])
array3=np.concatenate((array1,array2))#Se unen dos arrays en la misma fila
array12d=np.array([[2,3,4],[1,2,7]])
array22d=np.array([[5,6,74],[1,112,27]])
arrayfinal=np.concatenate((array12d,array22d))#Se unen dos matrices una sobre la otra
stackk=np.stack((array1,array2))#Se unen dos arrays uno sobre el otro
#puede ser o vertical o horizontal
dividirarr=np.array_split(arreglo,2)#Divide arreglo en un determinado numero que se le de
divarreglo2=np.array_split(arreglo2D,2)#También divide por dimensiones
np.insert(arreglo,3,33)#Añade un valor en el arreglo x la posicion x el valor x
np.append(arreglo,666)#añade un valor al final del arreglo
np.delete(arreglo,-1)#Borrar un valor cualquiera de un arreglo
