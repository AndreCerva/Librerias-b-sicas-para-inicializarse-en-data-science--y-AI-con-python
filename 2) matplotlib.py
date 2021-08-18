# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 23:52:19 2021

@author: andre
"""
import matplotlib.pyplot as plt
import numpy as np
edad_ejex=[20,25,30,35,40,45,50,55,60,65]
salario_cdejey=[20000,30000,40000,50000,60000,70000,80000,90000,95000,99000]
salario_fedejey=[10000,20000,30000,35000,40000,50000,60000,70000,75000,79000]
salario_medio=np.sum([salario_cdejey,salario_fedejey],axis=0)/2
plt.style.use('ggplot')
plt.plot(edad_ejex,salario_cdejey,label='Cientifico de datos',linewidth=3,marker='*',markersize=12,linestyle='dotted',color='#23454232')#Crear una grafica apartir de dos listas x y y
plt.plot(edad_ejex,salario_fedejey,label='Salario front end developer',linewidth=3,marker='+',markersize=12,color='#000000')
plt.plot(edad_ejex,salario_medio,label='Salario medio',linewidth=3,color='r')
plt.fill_between(edad_ejex,salario_cdejey,salario_medio,interpolate=True, where=(salario_cdejey>salario_fedejey),
                 alpha=0.4,color='g',label='Salarios por arriba de 50 años')
plt.fill_between(edad_ejex,salario_cdejey,salario_medio,interpolate=True, where=(salario_cdejey>salario_fedejey),
                 alpha=0.4,color='y',label='Salarios por abajo de 40 años')
plt.title('Relación de salario en $USD con respecto a su edad')#Titulo a mi grafico
plt.xlabel('Edad')#Etiqueta en los valores x
plt.ylabel("$USD")#Etiqueta en los valores y
plt.legend()#Para poder poner las label en los plots
plt.grid()#Cuadricula
plt.show()#Mostrar una grafica
#Histograma

Edad=[20,20,20,21,23,24,23,21,24,52,25,22,21,34,45,56,75,33,55,66,43,55,33,55,66,77,43,43,23,
      45,66,54,33,45,33,24,29,68,78,65,49,76]
plt.hist(Edad,bins=[10,20,30,40,50,60,70,80,90],color='b')
plt.xlabel('Edades')
plt.ylabel('Cantidad')
plt.title('Histograma de las edades de los cientificos de datos')
plt.show()
#plt.style.available
#plt.savefig('Nombre.png')
#Sacar promedio con numpy
xeje=np.arange(len(edad_ejex))
plt.bar(xeje,salario_cdejey,0.2,label='Salario Cientifico de datos',color='r')
plt.bar(xeje+0.25,salario_fedejey,0.2,label='Salario front end developer',color='b')
plt.bar(xeje-0.25,salario_medio,0.2,label='Salario promedio',color='#000000')
plt.xticks(xeje,edad_ejex)
plt.title('Relación de salario en $USD con respecto a su edad')#Titulo a mi grafico
plt.xlabel('Edad')#Etiqueta en los valores x
plt.ylabel("$USD")#Etiqueta en los valores y
plt.legend()#Para poder poner las label en los plots
plt.grid()#Cuadricula
plt.show()#Mostrar una grafica
#Para barras horizontales solo usar plt.barh

plt.pie(salario_cdejey,labels=edad_ejex,shadow=True,wedgeprops={'edgecolor':'black'},autopct='%1.3f%%')
plt.title('Porcentaje de salarios de un cientifico de datos')

#Diagrama de disperción
xran=np.random.rand(100)
yran=np.random.rand(100)
fig,ax=plt.subplots()
fig.suptitle('Diagrama de dispersión')
ax.scatter(xran,yran)
plt.show()

