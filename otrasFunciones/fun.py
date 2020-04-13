def fun(a,b,c,d,m,x):
    intA = a - (a-a//1)
    intB = b - (b-b//1)
    intC = c - (c-c//1)
    intD = d - (d-d//1)
    mayorCerrado = 0 ; menorCerrado = 0
    mayorAbierto = 0 ; menorAbierto = 0
    if a > b:
        mayorCerrado = a+1
        menorCerrado = b
    else:
        mayorCerrado = b+1
        menorCerrado = a
    if c > d:
        mayorAbierto = c-1
        menorAbierto = d+1
    else:
        mayorAbierto = d-1
        menorAbierto = c+1
        
    if x in range(menorCerrado,mayorCerrado) and x in range(menorAbierto,mayorAbierto) and m%x==0:
        resultado = 3
        
    if x in range(menorCerrado,mayorCerrado) and x in range(menorAbierto,mayorAbierto) and m%x!=0:
        resultado = 2
        
    if (x in range(menorCerrado,mayorCerrado) and x not in range(menorAbierto,mayorAbierto) and m%x!=0) or (x not in range(menorCerrado,mayorCerrado) and x  in range(menorAbierto,mayorAbierto) and m%x!=0):
        resultado = 1
       
    if x not in range(menorCerrado,mayorCerrado) and x not in range(menorAbierto,mayorAbierto):
        resultado = 0
        
    print(resultado)
    
fun(5,15,7,30,28,4)
        
    