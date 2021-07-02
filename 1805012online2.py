import matplotlib.pyplot as plt

def rel_error(new_val,old_val):
    return abs( (new_val-old_val) / new_val ) * 100.0

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
    
  #  print(b)
        
    
    yi = float(0.0)
    
    abs_rel_error = []
    abs_rel_error.append(float("NaN"))
    for i in range(n):
        temp_y = b[i][i]
        for j in range(i):
            temp_y = temp_y*(xi-x[j])
        if i != 0:
            abs_rel_error.append(rel_error(yi+temp_y,yi))
        yi = yi + temp_y
        
    return yi,abs_rel_error
    

def __main__():
    # input 
    mass = open("mass.txt",'r')
    mass_ = mass.readlines()
    
    mass_t = []
    mass_y = [] 
    mass_n = 0    
    for i in range(1,len(mass_)):
        input = mass_[i].split()
        mass_t.append( float(input[0]))
        mass_y.append( float(input[1]))
        mass_n += 1
    
    
    
    velocity_ = open("velocity.txt",'r').readlines()
    
    velocity_t= []
    velocity_y=[]
    velocity_n = 0
    for i in range(1,len(velocity_)):
        input = velocity_[i].split()
        velocity_t.append(float(input[0]))
        velocity_y.append(float(input[1]))
        velocity_n += 1
    
    
    m_t = []
    m_y = []
    
    v_t = [] 
    v_y = [] 
    
    
    T = 25.0
    N = 4;
    i = 0
    while i < mass_n and mass_t[i] < T :
        i += 1
    i-=N//2
  #  print(i)
    lim = i+N
    while i <= lim and i < mass_n :
        m_t.append(mass_t[i])
        m_y.append(mass_y[i])
        i+=1

    print(m_t)
    print(m_y)
    i = 0
    
    while i < velocity_n and velocity_t[i] < T:
        i += 1
    i-=N//2
   # print(i)
    lim = i+N
    while i <= lim and i < velocity_n:
        v_t.append(velocity_t[i])
        v_y.append(velocity_y[i])
        i+=1
   
    vi,error = interpolate_newton_divided_diff(v_t, v_y, T)
    print("Velocity = ",vi)
    print("Error : ")
    for x in error:
        print(x)
    print()
    
    mi,error2 = interpolate_newton_divided_diff(m_t, m_y, T)
    print("Mass = ", mi) 
    print("Error: ")
    for x in error:
        print(x)
    print()
    
    plt.plot(mass_t,mass_y)
    plt.annotate("Mass at T", (T,mi))
    plt.plot(T,mi,marker='.',markersize=30)
    plt.show()
    
    plt.plot(velocity_t,velocity_y)
    plt.annotate("Velocity at T",(T,vi))
    plt.plot(T,vi,marker='.',markersize=30)
    plt.show()
    
    
    p1 = mi*vi
    Del = -.0000001
    T2 = T+Del
    vi2,err = interpolate_newton_divided_diff(v_t, v_y, T2)
    mi2,err = interpolate_newton_divided_diff(m_t, m_y, T2)
    p2 = mi2*vi2
    F = (p2-p1)/Del
    print("Force = ", F)
__main__()