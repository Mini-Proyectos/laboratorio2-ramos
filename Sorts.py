import sys

def MergeSort(A,p,r):
	if p<r:
		medio=(p+r)//2
		MergeSort(A,p,medio)
		MergeSort(A,medio+1,r)
		merge(A,p,medio,r)

		
def merge(A,p,medio,r):
	L=A[p:medio+1]
	R=A[medio+1:r+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i=j=0
	for k in range(p,r+1):
		if L[i]<= R[j]:
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			j+=1

			
