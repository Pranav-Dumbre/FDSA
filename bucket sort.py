

def insertionSort(p):
	for i in range(1, len(p)):
		up = p[i]
		j = i - 1
		while j >= 0 and p[j] > up:
			p[j + 1] = p[j]
			j -= 1
		p[j + 1] = up	
	return p	
			
def bucketSort(x):
	arr = []
	slot_num = 10
	for i in range(slot_num):
		arr.append([])
		
	
	for j in x:
		index_p = int(slot_num * j)
		arr[index_p].append(j)
	
	
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])
		
	
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x

x = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())

	x.append(ele) 
	
print("Sorted Array is")
print(bucketSort(x))


