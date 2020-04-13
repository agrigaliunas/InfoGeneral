def doble7(num):
    cont = 0
    while num > 0 :
        n = num%10
        if n == 7:
            cont +=1
        num = num//10
        if cont > 1:
            return True
   
def tiene_5(num):
    if "5" in str(num):
        return True
    else:
        return False
def sumaDig(num):
    suma = 0
    while num > 0:
        n = num%10
        suma+=n
        num = num//10
    return suma

def prodDig(num):
    prod= 1
    while num > 0:
        n = num%10
        prod*=n
        num = num//10
    return prod
def cumple(num):
    if not tiene_5(num) and not doble7(num) and sumaDig(num) >= prodDig(num) and num!=1:
        return True
    else:
        return False
def main():
    cont = 0
    num = int(input("Ingrese num enteros positivos o cero para salir: "))
    while num < 0:
        num = int(input("Error. Ingrese num postivos o cero para salir: "))
    if cumple(num):
        cont += 1
    while num != 0:
        num = int(input("Ingrese num enteros positivos o cero para salir: "))
        while num < 0:
            num = int(input("Error. Ingrese num postivos o cero para salir: "))
        if cumple(num):
            cont += 1
    print("Cantidad de numeros que cumple condicion: ",cont)
main()