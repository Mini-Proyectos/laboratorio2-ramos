# Busquedas.py
# Autor: Ivette C. Martinez
# Modificado por: Allison Centeno y Wuidiana Ramos
# Descripcion: Implementacion de los algoritmos de busqueda lineal y BusquedaBinaria





def BusquedaLineal(arreglo, x):
	for i in range(len(arreglo)):
		if arreglo[i] == x:
			return i
	return None 


def BusquedaBinaria(arreglo, x, n):
	start= 0
	end= n-1
	while start < end:
		mid= (start + end) / 2
		if arreglo[mid] == x:
			return mid
		elif arreglo[mid] < x:
			start == mid + 1  	
		else:
			end == mid - 1
	if arreglo[start]==x:
		return start
	else:
		return None


def InsertionSort(arreglo,p,r):   	#Algoritmo de ordenamiento

	for j in range(p+1,r+1):
		key= arreglo[j]

		i= j-1
		while (i >= p) and (arreglo[i]> key):
			arreglo[i+1]= arreglo[i]
			i= i -1
		
		arreglo[i+1]=key
