'''
def listaIndice(xs,s):
    listadetupla =[]
    i = 0
    bandera = False
    while i < len(xs)-len(s):
        h = buscarS(xs,s)
        if (h!=(0,0) and h!=(-1,-1)) and bandera == False:
            n1 = h[0]
            n2 = h[1]
            n = n1,n2
            listadetupla.append(n)
            bandera = True
            resto = h[0]
            
        elif (h!=(0,0) and h!=(-1,-1)) and bandera == True:
            n1 = h[0]+resto
            n2 = h[1]+resto
            n = n1,n2
            listadetupla.append(n)
            resto += h[0]
            
        xs = xs[h[0]+1:]
        i+=1

    return listadetupla

def buscarS(xs,s):
    Indini = -1
    Indfin = -1
    long_s = len(s) #1
    long_xs = len(xs) #61
    bandera = False
    i = 0

    while i < long_xs:
        if bandera == False and xs[i:i+long_s] == s :
            Indini = len(xs[0:i])
            Indfin = len(xs[0:i+long_s-1])
            bandera = True
        i+=1

    return (Indini,Indfin)

def main():
    Ind = input('Ingrese indice a buscar:')
    arch_texto = open('info.txt','r')
    linea_texto = arch_texto.readline()
    h = buscarS(linea_texto,Ind)
    print('Se encuentra en',h)
    m = listaIndice(linea_texto,Ind)
    print(m)
    arch_texto.close()

main()
'''
def buscarS(xs,s):
    tupla = tuple()
    if s not in xs:
        tupla = (-1,-1)
    else:
        bandera = True
        for i in range(len(xs)-1):
            if bandera and xs[i:i+len(s)]==s:
                tupla = (i,i+len(s)-1)
                bandera = False
    return tupla

def listaIndice(xs,s):
    lista = []
    if s not in xs:
        lista = []
    else:
        for i in range(len(xs)-1):
            if s == xs[i:i+len(s)]:
                tupla = (i,i+len(s)-1)
        lista.append(tupla)
    return lista





def main():
    s = input("Ingrese string a buscar: ")
    file = open("info.txt","r")
    xs = file.readline()
    print(xs)
    h = buscarS(xs,s)
    print("se encuentra en: ",h)
    print(listaIndice(xs,s))
    
    file.close()
main()



