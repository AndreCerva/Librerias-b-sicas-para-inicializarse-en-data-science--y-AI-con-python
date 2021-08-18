# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 22:03:33 2021

@author: andre
"""
import pandas as pd
print(pd.__version__)
serie=pd.Series([55,32,52],index=('a','b','c'))#Se crea una serie con un indice por defecto del 0 hasta n
serie.values#ver los valores de la serie
serie.index#index de la serie
serie2=pd.Series({'a':10,'b':11,'c':12})#Otra forma de crear una serie
serie2.values#Valores de mi serie
serie2.index#Indices de mi serie
dataframe=pd.DataFrame({'Serie 1': serie,'Serie 2':serie2})#Dataframe 
dataframe.T #Transponer o conmutar los indices y columnas
dataframe['Total de la suma ']=dataframe['Serie 1']+dataframe['Serie 2']#Añadir una columna a mi
del dataframe['Total de la suma ']#Borrar columna de mi dataframe
dataframe.loc['a']#localizar todos los elementos del data en la fila a
dataframe.loc['a':'c']#todos los elementos de la fila a a la c
dataframe.loc[['c','a']]#elemento c y a 
dataframe.iloc[0:1]#del 0 a 1
dataframe.iloc[0]#elementos de la columna 0
dataframebusqueda=dataframe[dataframe['Serie 1']>35] #Crear un datafrme condicional de otro dfr
#Ejercicio
minutos=pd.Series([60,45,30,45,45,4500],index=[0,1,2,3,4,5])
rate=pd.Series([4,4,8,7,10],index=[0,1,3,4,5])
asks=pd.Series([1,'cero',2,2,3],index=[1,2,3,4,5])
dataframe2=pd.DataFrame({'Time':minutos,'Rate':rate,'Asks':asks})
dataframe2=dataframe2.dropna() #Elimina los valores que contengan valores nulos, útil solo cuando son muchos valores
dataframe2=dataframe2.fillna(333)#Pone un numero x en los valores nulos
dataframe2['Rate'].fillna(7,inplace=True)#Actualizar el valor nulo de una columna especifica
mean=dataframe2['Rate'].mean()#Promedio el valor de la media
median=dataframe2.median()#Mediana, el valor de ordenar los valores y tomar el del medio
mode=dataframe2.mode()#El numero que se repite mas
dataframe2.Asks[dataframe2.Asks=='cero']=0#buscar dentro de Asks algo que se llame cero y rempla
dataframe2.loc[5,'Time']=45#localizar el elemento de la fila 5 columna Time
dataframe2.duplicated()#Saber si se encuentra duplicado o no una fila completa
dataframe2.loc[6,'Time']=dataframe2.loc[4,'Time']
dataframe2.loc[6,'Rate']=dataframe2.loc[4,'Rate']
dataframe2.loc[6,'Asks']=dataframe2.loc[4,'Asks']
dataframe2.drop_duplicates(inplace=True)















