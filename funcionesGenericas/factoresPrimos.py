
#    ***** Algoritmo para encontrar factores primos *****    #

def factoresPrimos(num):
    divisores = 0 ; cont = 0
    for div in range(1,num+1):
        for i in range(1,div+1):
            if div%i == 0:
                cont +=1
        if cont == 2 and num%div == 0 or div == 1:
            divisores = div
            print(divisores)
        cont = 0
factoresPrimos(37)
