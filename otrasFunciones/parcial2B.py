def descompuesto(num):
    if suma(num) >= mult(num):
        return True
    else:
        return False

def mult(num):
    mult_total = 1
    while num > 0:
        mult_total = num%10 * mult_total
        num = num//10
    return mult_total

def suma(num):
    suma_total = 0
    while num > 0:
        suma_total += num%10
        num = num//10
    return suma_total


def tiene_7(num):
    if "7" in str(num):
        return True
    else:
        return False
def tiene_5(num):
    if "5" in str(num):
        return True
    else:
        return False
def main():
    cont = 0
    num = int(input("Ingrese numeros positivos o cero para salir: "))
    if (tiene_7(num) and not tiene_5(num)) and descompuesto(num):
        cont +=1
    while num < 0:
        num = int(input("Error. Ingrese lo pedido: "))
    while num != 0:
        num = int(input(">> "))
        while num < 0:
            num = int(input("Error. Ingrese lo pedido: "))
        if (tiene_7(num) and not tiene_5(num)) and descompuesto(num):
            cont +=1
    print("Cantidad de numeros que cumple condicion: ", cont)

main()
