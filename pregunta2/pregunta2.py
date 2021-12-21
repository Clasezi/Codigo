from auto import auto
from moto import moto

while True:
    num = int (input("\ningrese 1 si quiere crear un carro 2 si quiere crear una moto y 3 si quiere continuar\n-"))
    if num ==1 :
        auto1 = auto()
        continue
    elif num ==2:
        moto1 = moto()
        continue
    elif num == 3:
        break
    else :
       print("ingrese solo 1 ,2 o 3")
       break

while True:
    print("\nsolo te imprimira el ultimo auto o moto creado")
    num2 = int (input("\ningrese 1 si quiere mostrar el precio del auto o 2 si quiere el precio de la moto y 3 si quiere terminar el programa\n-"))
    try :
        if num2 == 1:
            print("Auto")
            print("Marca : {}".format(auto1.marca))
            print("precio : {}".format(auto1.obtener_precio()))
            continue
        elif num2 == 2:
            print("Moto")
            print("Marca : {}".format(moto1.marca))
            print("precio : {}".format(moto1.obtener_precio()))
            continue
        elif num2 == 3:
            break
        else:
            print("ingrese solo 1 o 2")
            pass
    except NameError:
        print("Error no se olvide de mostrar solo si ya lo creo ")
        pass