
R = int(input("enter number of rows"))
C = int(input("enter number of colunms"))

# code for matrix_1
matrix1 = []
for i in range(R):	   
   row = []
   for j in range(C):	     
      element = int(input("enter elements for matrix1\n"))
      row.append(element)	  
   matrix1.append(row)
   
print("matrix_1 = ",matrix1)
print("\n")
X = matrix1

# code for matrix_2
matrix2 = []
for i in range(R):	   
   row = []
   for j in range(C):	     
      element = int(input("enter elements for matrix2 \n"))
      row.append(element)	  
   matrix2.append(row)
   
print("matrix_2 = ",matrix2)
print("\n")
Y = matrix2

print('''
       1] Addition
       2] Subtraction
       3] Multiplication
       4] Transpose of Matrix1
       5] Transpose of Matrix2
       6] Exit ''')


result = [[0,0,0],
	 [0,0,0],
         [0,0,0],]

def add():
	for i in range(len(X)):
	   for j in range(len(X[0])):
	       result[i][j] = X[i][j] + Y[i][j]
	print("Addition is")
	for r in result:
		print(r)
	print("\n")
	
def sub():
	for i in range(len(X)):
	   for j in range(len(X[0])):
	       result[i][j] = X[i][j] - Y[i][j]
	print("Substraction is")
	for r in result:
		print(r)
	print("\n")
def mul():
	for i in range(len(X)):
	   for j in range(len(Y[0])):
	       for k in range(len(Y)):
		        result[i][j]+=X[i][k]*Y[k][j]
	print("Multiplication is")
	for r in result:
	   print(r)
def transpose1():
	print("\nTranspose of matrix1 is : ")
	for i in range (len(X)):
		for j in range (len(X[0])):
			result[j][i]=X[i][j]
	for r in result:
		print(r)	
def transpose2():
	print("\nTranspose of matrix2 is : ")	
	for i in range (len(Y)):
		for j in range (len(Y[0])):
			result[j][i]=Y[i][j]
	for r in result:
		print(r)
			   	
while True:
	ch=int(input("Enter your choice : "))
	if (ch==1):
		add()
	elif (ch==2):
		sub()
	elif (ch==3):
		mul()		
	elif (ch==4):
		transpose1()		
	elif (ch==5):
		transpose2()		
	elif (ch==6):
		print("Process Exited")
		break
