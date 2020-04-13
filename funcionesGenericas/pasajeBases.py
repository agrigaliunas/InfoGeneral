
#    ***** Algoritmo para pasaje a cualquier base *****    #

def aBase(num,bas):
    p = 1
    convertido = 0
    while num != 0:
        resto = num%bas
        num = num//bas
        convertido = convertido + resto*p
        p=p*10
    return convertido

    
def main():
    numero_a_pasar = int(input("Ingrese numero a pasar: "))
    base = int(input("Ingrese la base que quiere usar: "))
    print("{} en base {} es {}".format(numero_a_pasar,base,aBase(numero_a_pasar,base)))
    
    
main()