'''
Ejercicio 2:
Realizar un programa que solicite al usuario que se ingrese un texto hasta ingresar 'ENTER'. El programa debe indicar la longitud de la secuencia mas larga de mayúsculas consecuentes. 

Ej: 
Ingrese texto:
SDM drTYUJfghay DYchaj 
Secuencia mas larga: 4.

El próximo examen es: JUEVES 8:30hs.
Secuencia mas larga: 6.

para despejarse es bueno salir a caminar.
No se ingresaron mayúsculas.



def main():
    texto = input("Ingrese texto: ")
    if largaMayus(texto) == 0:
        print("No se ingresaron mayusculas.")
    else:
        print("Secuencia mas larga: {}".format(largaMayus(texto)))
        
def esMayus(l):
    return l >= "A" and l <= "Z"

def largaMayus(texto):
    i = 0 ; maxima = ""
    while i < len(texto):
        while i < len(texto) and not esMayus(texto[i]):
            i +=1
        pal = ""
        while i < len(texto) and esMayus(texto[i]):
            pal += texto[i]
            i+=1
        if len(pal) > len(maxima):
            maxima = pal
    return len(maxima)

main()
*************************************************
def main():
    numero = int(input("Ingrese el numero: "))
    if len(str(numero)) < 3:
        print("El numero no dispone de los digitos necesarios.")
    else:
        penco(numero)

def penco(numero):
    ultimo = numero%10 ; primero = numero//(10**len(str(numero))//10)
    promedio = (ultimo+primero)//2
    if promedio != ultimo and promedio != primero and str(promedio) in str(numero):
        print("Es un numero penco")
    else:
        print("No es un numero penco")

    
    
main()
'''