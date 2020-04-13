def cargarAbonados():
    dicAbonados = {}
    archAbonados = open("abonados.csv","r")
    for linea in archAbonados:
        lista = linea.split(",")  # KEY = ID_ABONADO
        dicAbonados[int(lista[0])]=[lista[1],lista[2],int(lista[3])]
    archAbonados.close()
    return dicAbonados  

def cargarCategorias():
    dicCat = {}
    archCategorias = open("categorias.csv","r")
    for linea in archCategorias:
        lista = linea.split(",") # KEY = ID_categoria
        dicCat[int(lista[0])]=[float(lista[1]),float(lista[2])]
    archCategorias.close()
    return dicCat

def cargarListaConexiones():
    lista_conexiones = []
    archConexiones = open("conexiones.csv","r")
    for linea in archConexiones.readlines():
        if linea[-1] == "\n":
            linea = linea[:-1]
        linea = linea.split(",")
        linea[0] = int(linea[0])
        linea[1] = int(linea[1])
        lista_conexiones.append(linea)
    archConexiones.close()
    return lista_conexiones

def factura(ID_abonado):
    dicCat = cargarCategorias()
    dicAbonados = cargarAbonados()
    listaConex = cargarListaConexiones()
    nombre = "" ; abono = 0 ; domicilio = "" ; suma_importe = 0
    claves = list(dicCat.keys())
    for clave in dicAbonados:
        if clave == ID_abonado:
            nombre = dicAbonados[clave][0]
            domicilio = dicAbonados[clave][1]
        ID_categoria = dicAbonados[clave][2]
        
        if ID_categoria == claves[0]:
            abono = dicCat[clave][0]
            
    for sl in listaConex:
        ID_categoria = dicAbonados[ID_abonado][2] 
        if ID_abonado == sl[0]:
            suma_importe+= sl[1]
    importe = suma_importe*dicCat[ID_categoria][1]

            
    print("Nombre: {}\n Domicilio: {}\n Abono: {}\n Importe: {}\n Total: {}\n".format(nombre,domicilio,abono,importe,(abono+importe)))



def duracionMaxima():
    dicCat = cargarCategorias()
    dicAbonados = cargarAbonados()
    listaConex = cargarListaConexiones()
    maxi = 0 ; primera = True ; suma_min = 0
    
    repetido = []
    mayor = 0
    for k in range(0,len(listaConex)):
        if listaConex[k][0] not in repetido:
            minutos = 0
            repetido.append(listaConex[k][0])
            for h in range(0,len(listaConex)):
                if listaConex[h][0]==listaConex[k][0]:
                    minutos+=int(listaConex[h][1])
            if minutos>mayor:
                mayor = minutos
                ID_abonado = listaConex[k][0]
        
        
    print("ID_abonado: {}\n Nombre: {}\n Categoria: {}\n Duracion total en minutos: {}".format(ID_abonado,dicAbonados[ID_abonado][0],dicAbonados[ID_abonado][2],mayor))
    

def main():
    dicAbonados = cargarAbonados()
    IDS = list(dicAbonados.keys())
    
    ID_abonado = int(input("Ingrese ID de abonado: <<({})>>: ".format(IDS)))
    factura(ID_abonado)
    duracionMaxima()
main()