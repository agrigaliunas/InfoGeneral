#2
def main():
    num = int(input("Ingrese un numero: "))
    if iguales(num):
        print("El numero posee todos sus digitos iguales")
    else:
        print("El numero NO posee todos sus digitos iguales")

def iguales(num):
    n = num
    iguales = True
    while num > 0:
        resto = num%10
        num = num//10
        if resto != (n//10)%10:
            iguales = False
    return iguales

main()