import numpy as np

# naive gaussian elimination
def NaiveGaussianElimination(A,B,d = True):
    n = np.size(A,axis=0)
    if n != np.size(A,axis=1) :
        print("Invalid Input")
        return 
    if n != np.size(B,axis=0):
        print("Invalid Input")
        return 
    
    for i in range(n-1):
        for j in range(i+1,n):
            multiplier = A[j][i]/A[i][i]
            A[j] = A[j]-multiplier*A[i]
            B[j] = B[j]-multiplier*B[i]
        
        if d == True:
            print("After Step %d:" %(i+1))
            print(A)
            print()
            print(B)
            print()
            print()

    X = np.zeros([n,1])
    
    for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                B[i] = B[i] - X[j]*A[i][j]
            X[i] = B[i]/A[i][i]
    return X    

# gaussian elimination with partial pivoting 
def GaussianElimination(A,B,d=True):
    n = np.size(A,axis=0)
    if n != np.size(A,axis=1):
        print("Invalid Input")
        return 
    if n != np.size(B,axis=0):
        print("Invalid Input")
        return
    
    for i in range(n-1):
        maximum_pivot_element_id = i
        for j in range(i+1,n):
            if abs(A[j][i]) > abs(A[maximum_pivot_element_id][i] ):
                maximum_pivot_element_id = j
        A[[i,maximum_pivot_element_id]] = A[[maximum_pivot_element_id,i]]
        B[[i,maximum_pivot_element_id]] = B[[maximum_pivot_element_id,i]]
        
        for j in range(i+1,n):
            mul = A[j][i]/A[i][i]
            A[j] = A[j] - A[i]*mul
            B[j] = B[j] - B[i]*mul
        if d == True :
            print("After Step %d: "%(i+1))
            print(A)
            print()
            print(B)
            print()
    
    X = np.zeros([n,1])
    
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            B[i] = B[i] - X[j]*A[i][j]
        X[i] = B[i]/A[i][i]
    return X
                
                
def __main__():
    n = int(input())
    array = []
    for i in range(n):
        ln = input().split()
        for x in ln:
            array.append(float(x))
    A = np.array(array)
    A = A.reshape(n,n)
    
    array = []
    for i in range(n):
        x = float(input())
        array.append(x)
    B = np.array(array)
    B = B.reshape(n,1) 

    Solution = np.round(GaussianElimination(A,B),4)
    print("Value of the unknowns: \n",Solution)


__main__()

