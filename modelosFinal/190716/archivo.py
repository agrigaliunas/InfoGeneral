def cargarVendedores():
    lista_vendedores = []
    archivoVendedores = open("vendedores.csv","r")
    for linea in archivoVendedores.readlines():
        linea = linea[:-1]
        
        linea = linea.split(",")
        
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        linea[3] = float(linea[3])
        lista_vendedores.append(linea)
    archivoVendedores.close()
    return lista_vendedores
def cargarTarjetas():
    lista_tarjetas = []
    archivoTarjetas = open("ventasTarjetas.csv","r")
    for linea in archivoTarjetas.readlines():
        linea = linea[:-1]
        linea = linea.split(",")
        
        linea[0] = int(linea[0])
        linea[2] = int(linea[2])
        lista_tarjetas.append(linea)
    archivoTarjetas.close()
    return lista_tarjetas
        
   
def liquidar():
    lista_tarjetas = cargarTarjetas()
    lista_vendedores = cargarVendedores()
    archLiq = open("liquidaciones.csv","w")
    for venta in lista_vendedores:
        totTarj = 0
        for ventaTarj in lista_tarjetas:
            if venta[0] == ventaTarj[0]:
                totTarj+=ventaTarj[2]
    
        com = comision(totTarj,venta[2],venta[3])
        comision_final = round(com,2)
        archLiq.write(str(venta[0])+","+str(comision_final)+"\n")
    archLiq.close()
        
def comision(totTarj,objTarj,sueldo):
    porMin = 0.8
    por3 = 0.03
    por10 = 0.1
    sueldoMin = 0
    if totTarj<(objTarj*porMin):
        comision = sueldoMin
    elif totTarj>=(objTarj*porMin) and totTarj<=objTarj:
        comision = sueldo*por3
    elif totTarj>=objTarj:
        comision = sueldo*por10
    return comision
    

def main():
    liquidar()
    #topCinco()
main()

























