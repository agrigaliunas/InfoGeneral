#Parcial 2
'''
def main():
    numero = int(input("Ingrese un numero: "))
    if iguales(numero):
        print("El numero posee todos sus digitos iguales")
    else:
        print("El numero NO posee todos sus digitos iguales")
def iguales(num):
    iguales = True ; ultima = num%10
    while num > 0:
        if ultima != num%10:
            iguales = False
        num = num//10
    return iguales
main()
'''

def main():
    texto  = input("Ingrese texto: ")
    print("La palabras mas extensa posee {} caracteres".format(extensa(texto)))
    
def extensa(texto):
    i = 0 ; masLarga = ""
    while i < len(texto):
        while i < len(texto) and not esLetra(texto[i]):
            i +=1
        pal = ""
        while i < len(texto) and esLetra(texto[i]):
            pal+=texto[i]
            i+=1
        if len(pal) > len(masLarga):
            masLarga = pal
    return len(masLarga)
    
def esLetra(l):
    return l>="A" and l <="Z" or l>="a" and l<"z"


main()