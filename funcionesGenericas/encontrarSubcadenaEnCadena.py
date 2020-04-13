
#    ***** Algoritmo que cuenta la cantidad de veces que se repite una sub-string en un string *****    #

def repitSub(cad,subCad):
    cont = 0
    for i in range(len(cad)):
        if len(cad) == 0 or len(subCad) == 0:
            cont == 0
        elif cad[i:len(subCad)+i] == subCad:
            cont += 1
    return cont
            
        
def main():
    c = input("Cadena: ")
    s = input("Subcadena: ")
    print(repitSub(c,s))
    
main()
