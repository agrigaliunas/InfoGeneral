def cargarHabitantes():
    dic_habitantes = {}
    archivoHabitantes = open("habitantes.csv","r")
    for linea in archivoHabitantes:
        lista = linea.split(",")
        dic_habitantes[int(lista[0])]=[lista[1],int(lista[2]),int(lista[3])]
    archivoHabitantes.close()
    return dic_habitantes
    
def cargarListaHabitantes():
    lista_habitantes = []
    archivoHabitantes = open("habitantes.csv","r")
    for linea in archivoHabitantes.readlines():
        linea = linea[:-1]
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        linea[3] = int(linea[3])
        lista_habitantes.append(linea)
    archivoHabitantes.close()
    return lista_habitantes
    
def cargarLocalidades():
    dic_localidades = {}
    archivoLocalidades = open("localidades.csv","r")
    for linea in archivoLocalidades:
        lista = linea.split(",")
        dic_localidades[int(lista[0])]=[lista[1],int(lista[2])]
    archivoLocalidades.close()
    return dic_localidades

def cargarHabXLoc():
    dic_habXloc = {}
    archivoHabXLoc = open("habitantesXlocalidad.csv","r")
    for linea in archivoHabXLoc:
        lista = linea.split(",")
        dic_habXloc[int(lista[1])]=int(lista[0])
    archivoHabXLoc.close()
    return dic_habXloc

def cantHabitantes(nombreLocalidad, hijos):
    dic_local = cargarLocalidades()
    #dic_hab = cargarHabitantes()
    dic_habXloc = cargarHabXLoc()
    lista_hab = cargarListaHabitantes()
    lista_final = []
    idLoc = -1
    i = 0
    
    claves = list(dic_local.keys())
    while i<=len(claves) and idLoc==-1:
        if dic_local[claves[i]][0]== nombreLocalidad:
            idLoc = claves[i]
        i+=1
        
        
    if idLoc!=-1:
        for habitante in lista_hab:
            valorLoc = dic_habXloc.get(habitante[0])
            
            if habitante[2]==hijos and valorLoc == idLoc:
                lista_final.append((habitante[0],habitante[1]))
    return lista_final     
    
def edadXlocalidad():
    dic_loc = cargarLocalidades()
    dic_habXloc = cargarHabXLoc()
    dic_hab = cargarHabitantes()
    dic_edadXloc = {}
    for ID_loc in dic_loc:
        edad = 0 ; cont = 0
        for ID_hab in dic_habXloc:
            if dic_habXloc[ID_hab] == ID_loc:
                edad+=dic_hab[ID_hab][2]
                cont+=1
        if cont>0:
            dic_edadXloc[ID_loc] = (edad/cont)
    imprimirDiccionarioOrdenado(dic_edadXloc)
                
def imprimirDiccionarioOrdenado(dic):
    claves = list(dic.keys())
    ordenar(claves)
    print("{:15}{:15}".format("Id localidad","Promedio Edad"))
    for clave in claves:
        print("{:<15}{:<15}\n".format(clave,dic[clave]))
def ordenar(lst):
    
    i = 0 ; j = 0 ; aux = 0
    while i<len(lst):
        j = i+1
        while j<len(lst):
            if lst[i]>lst[j]:
                aux = lst[i]
                lst[i]=lst[j]
                lst[j] = aux
            j+=1
        i+=1
    return lst
    '''
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]<lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
    '''
def main():
    print("LOCALIDADES:\n ADOLFO ALSINA\n CARLOS CASARES\n MARCOS PAZ\n LUJAN\n EZEIZA")
    localidad = input("Ingrese localidad: ")
    hijos = int(input("Ingrese cantidad hijos: "))
    print(cantHabitantes(localidad,hijos))
    edadXlocalidad()
main()