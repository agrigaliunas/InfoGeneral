
#    ***** Algoritmo para encontrar palabra mas larga dentro de un string *****    #

def esLetra(l):
    if l <= "z" and l >= "a" or l <= "Z" and l >= "A":
        return True
    else:
        return False

def encontrarMasLarga(t):
    i = 0
    pal_larga = ""
    while i < len(t):
        pal = ""
        while i < len(t) and esLetra(t[i]) == True:
            pal = pal + t[i]
            i+=1
        while i < len(t) and esLetra(t[i]) == False:
            i+=1
        if len(pal) > len(pal_larga):
            pal_larga = pal
        
    print("La palabra mas extensa posee", len(pal_larga), "caracteres.")


def main():
    texto = input("Ingrese texto: ")
    encontrarMasLarga(texto)
main()