
#    ***** Algoritmo para ver si un numero posee digitos iguales *****    #

def digitosIguales(num):
    iguales = True
    ultimoDig = num%10   # num = 1234
    while num > 0:
        if ultimoDig != num%10:
            iguales = False
        num = num//10
    return iguales

def main():
    numero = int(input("Ingrese un numero: "))
    if digitosIguales(numero) == True:
        print("El numero posee todos los digitos iguales")
    else:
        print("El numero NO posee todos los digitos iguales")
        
main()

