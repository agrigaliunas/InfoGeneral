def generarT1(a,b):
    ini = 0 ; fin = 0 ; cont = 0
    if a > b:
        ini = b
        fin = a
    else:
        ini = a
        fin = b
    for n in range(ini,fin+1):
        while cont < 3:
            if fin%n == 0:
                cont += 1
                print("[{}]: {}".format(cont,n))
generarT1(4,90)