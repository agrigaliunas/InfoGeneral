def esVocal(l):
    if l == "a" or l == "A" or l == "e" or l == "E"  or l == "i"  or l == "I"  or l == "o"  or l == "O"  or l == "u" or  l == "U":
        return True
    else:
        return False

def EsLetra(l):
    if (l >= "a" and l <= "z") or (l >= "A" and l <= "Z"):
        return True
    else:
        return False

def comparar(palabra):
    i = 0
    while i < len(palabra)-1:

        if esVocal(palabra[i]) and esVocal(palabra[i+1]) and palabra[i] != palabra[i+1]:
            return True
        i+=1
    return False

def palabra(frase):
    i = 0
    cont = 0
    while i < len(frase):
        while i < len(frase) and not EsLetra(frase[i]):
            i += 1
        palabra = ""
        while i < len(frase) and EsLetra(frase[i]):
            palabra += frase[i]
            i+= 1
        if comparar(palabra):
            cont+= 1
    return cont


def main():
    frase = input("Ingrese frase: " )
    print(palabra(frase))
main()
