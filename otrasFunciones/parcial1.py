#Parcial 1
'''
def main():
    base = int(input("Ingrese longitud: "))
    while base < 5 or base%2 == 0:
         base = int(input("Error. Ingrese longitud mayor positiva mayor a 5 e impar: "))
    figura(base)
    
def figura(b):
    for fil in range(b):
        for col in range(b):
            if col == fil or fil + col == b-1 and fil <=b//2 and col >=b//2:
                print("*",end="")
            else:
                print(" ",end="")
        print("")


main()



def main():
    texto = input("Ingrese texto: ")
    if longitud(texto) == 0:
        print("No se ingresaron minusculas")
    else:
        print("Secuencia minima: ",longitud(texto))


def esMinus(l):
    if l >="a" and l <="z":
        return True
    else:
        return False


def esLetra(l):
    return l>="A" and l<="Z" or l>="a" and l<="z"


def longitud(txt):
    i = 0
    palMin = ""
    pal = ""
    primer_vuelta = True
    while i < len(txt):
        while i < len(txt) and not esMinus(txt[i]):
            i +=1
        pal = ""
        while i < len(txt) and esMinus(txt[i]):
            pal+=txt[i]
            i+=1
        if primer_vuelta:
            palMin = pal
            primer_vuelta = False
        else:
            if len(pal) < len(palMin):
                palMin=pal

    return len(palMin)
    
main()
'''


def main():
    numero = int(input("Ingrese numero a validar: "))
    if len(str(numero)) < 3:
        print("El numero no dispone de los digitos necesarios")
    else:
        pisano(numero)
            
def pisano(num):
    ultimo = num%10 ; sumaM = 0 ; sumaP = ultimo ; cont = 0 ; num = num//10
    while num > 0:
        n = num%10
        if num >=10:
            sumaM+=n
            cont +=1
        if num<10 and num > 0:
            sumaP+=n
        num = num//10
    if sumaP == sumaM//cont:
        print("Es un numero pisano")
    else:
        print("NO es un numero pisano")
        
main()