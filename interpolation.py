def interpolate_lagrangian(x: list,y: list,xi: float):
    yi = float(0.0)
    
    if len(x) != len(y) :
        print("Invalid input")
        exit(-1)
    n = len(x)
    for i in range(n):
        temp_y = y[i]
        for j in range(n):
            if i == j :
                continue 
            temp_y = temp_y*(xi-x[j]) / (x[i]-x[j]) 
        yi = yi + temp_y
    return yi


def interpolate_newton_divided_diff(x: list,y: list,xi: float):
    b = []
    
    if len(x) != len(y):
        print("Invalid input")
        exit(-1)
    n = len(x)
    
    bi = []
    for i in range(n):
        bi.append(y[i])
    b.append(bi)
    b_p = bi
    for i in range(1,n):
        bi = [] 
        for j in range(0,i):
            bi.append(0)
        for j in range(i,n):
            b_ = (b_p[j]-b_p[j-1])/(x[j]-x[j-i])
            bi.append(b_)
        b_p = bi
        b.append(bi)
    
    print(b)
        
    
    yi = float(0.0)
    
    for i in range(n):
        temp_y = b[i][i]
        for j in range(i):
            temp_y = temp_y*(xi-x[j])
        yi = yi + temp_y
    return yi
    


n = None
data_x = [] 
data_y = [] 
def __main__():
    n = int(input("Size of data: "))
    
    print("Input data_x : ")
    for i in range(n):
        x = float(input())
        data_x.append(x)
    
    print("Input data_y: ")     
    for i in range(n):
        x = float(input())
        data_y.append(x)
    
    for x in data_x:
        print(x,end=' ')
    print()
    for y in data_y:
        print (y,end=' ')
    print()
    
    xi = float(input("Value to be interpolated at: "))
    yi = interpolate_lagrangian(data_x, data_y, xi)
   # print("Interpolated value at", xi, ":", yi)
   # yi = interpolate_newton_divided_diff(data_x, data_y, xi)  
    print(yi)
__main__()