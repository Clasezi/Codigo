from Pila import Pila

print("La cantidad de discos debe ser mayor o igual a 3")
cantidad = int(input("Ingrese el numero de discos: "))

TorreInicial = Pila()
TorreMedio = Pila()
TorreFinal = Pila()

def Llenar_torreInicial():
    for i in range(cantidad):
        disco = int(input("Numero del disco {}:".format(i+1)))
        TorreInicial.items.append(disco)

def Llenar_torreFinalconInicial():    
    disco_retirar = TorreInicial.pop()
    TorreFinal.items.append(disco_retirar)

def Llenar_TorreMedioconInicial():
    disco_retirar = TorreInicial.pop()
    TorreMedio.items.append(disco_retirar)

def Llenar_TorreMedioconFinal():
    disco_retirar = TorreFinal.pop()
    TorreMedio.items.append(disco_retirar)

def Llenar_TorreInicialconFinal():
    disco_retirar = TorreFinal.pop()
    TorreInicial.items.append(disco_retirar)



if cantidad == 3: 
    Llenar_torreInicial()
    print("La torre incial tiene : ", TorreInicial.items)
    Llenar_torreFinalconInicial()
    print("La torre inicial tiene: ",TorreInicial.items)
    print("La torre final tiene: ", TorreFinal.items)
    Llenar_TorreMedioconInicial()
    print("La torre Medio tiene: ",TorreMedio.items)
    print("La torre inicial tiene: ", TorreInicial.items)
    