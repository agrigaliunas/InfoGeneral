#5
'''
def principioFin(texto):
    i = 0
    ultima = "" ; primera = ""
    while not (texto[i]>="A" and texto[i]<="Z" or texto[i]>="a" and texto[i]<="z"):
        i +=1
    while i < len(texto) and (texto[i]>="A" and texto[i]<="Z" or texto[i]>="a" and texto[i]<="z"):
        primera += texto[i]
        i+=1


    i = -1
    while not (texto[i]>="A" and texto[i]<="Z" or texto[i]>="a" and texto[i]<="z"):
        i -=1
    while i < len(texto) and (texto[i]>="A" and texto[i]<="Z" or texto[i]>="a" and texto[i]<="z"):
        ultima += texto[i]
        i-=1
    if primera == ultima[::-1]:
        return True
    else:
        return False





def main():
    texto = input("Ingrese un texto: ")
    if principioFin(texto):
        print("El texto cumple la condicion")
    else:
        print("El texto no cumple la condicion")

main()



#6
def main():
    frase = input("Ingrese una frase: ")
    if palindroma(frase):
        print("La frease es palindroma")
    else:
        print("La frase no es palindroma")

    palindroma(frase)
def palindroma(t):
    texto_min=""
    for i in range(len(t)):
        if (t[i]>="A" and t[i]<='Z'):
            texto_min+=chr(ord(t[i])+32) #Convertir mayúsculas a minúsculas
        else:
            texto_min+=t[i]

    i = 0
    txtSE = ""
    while i < len(texto_min):
        while i < len(texto_min) and not (texto_min[i] >="A" and texto_min[i]<="Z" or texto_min[i] >="a" and texto_min[i] <="z"):
            i+=1
        while i < len(texto_min) and (texto_min[i] >="A" and texto_min[i]<="Z" or texto_min[i] >="a" and texto_min[i] <="z"):
            txtSE+=texto_min[i]
            i+=1
    invertido = txtSE[::-1]
    if invertido == txtSE:
        return True
    else:
        return False


main()

#7

def main():
    txtLargo = input("Ingrese el texto largo: ")
    txtCorto = input("Ingrese el texto corto: ")
    print("El texto se encontro {} veces en el texto largo".format(seRepite(txtLargo,txtCorto)))

def seRepite(txtLargo,txtCorto):
    i = 0 ; cont = 0
    while i < len(txtLargo):
        while i < len(txtLargo) and not (txtLargo[i] >="A" and txtLargo[i] <="Z" or txtLargo[i] >="a" and txtLargo[i] <="z"):
            i +=1
        pal = ""

        while i < len(txtLargo) and (txtLargo[i] >="A" and txtLargo[i] <="Z" or txtLargo[i] >="a" and txtLargo[i] <="z"):
            pal += txtLargo[i]
            i +=1
        if pal == txtCorto:
            cont +=1
            return cont
main()
'''
