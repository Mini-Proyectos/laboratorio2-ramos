import time
import random
import sys
from Sorts import MergeSort
from Busquedas import InsertionSort


A=[29,41,32,54,4,0,22,1,7,14]
n=10

random.shuffle(A)
inicio=time.time()

if sys.argv[1]== str(MergeSort):
		MergeSort(A,0,len(A)-1)
elif sys.argv[1]== str(InsertionSort):
		InsertionSort(A,0,len(A)-1)
		
fin=time.time()
tiempo = (fin-inicio) * 1000

print(sys.argv[1], n, tiempo)

