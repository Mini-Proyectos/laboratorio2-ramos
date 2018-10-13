#Alumnas: Allison Centeno y Wuidiana Ramos


import time
import random
import sys
from Sorts import MergeSort
from Busquedas import InsertionSort



n= int(sys.argv[2])				#esta línea guarda cual sera el tamaño del arreglo
A=[]

for i in range(n):							#generamos nuestro arreglo de numeros aleatorios
	A.append(random.randint(1,1000))

inicio=time.time()							#comenzamos a tomar el tiempo que durara el respectivo algoritmo escogido

if sys.argv[1]== str(MergeSort):				#verificamos cual algoritmo de ordenamiento se eligio
		MergeSort(A,0,len(A)-1)
elif sys.argv[1]== str(InsertionSort):
		InsertionSort(A,0,len(A)-1)
		
fin=time.time()								#tiempo de finalizacion
tiempo = (fin-inicio) * 1000				#colocamos el tiempo en milisegundos

print(A)								#nuestro arreglo con numeros aleatorios
print(sys.argv[1], n, tiempo)			#las respectivas salidas pedidas	

