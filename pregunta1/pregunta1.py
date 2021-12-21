from estructuras import Pila 
from estructuras import disc2

p1 = Pila.pila()
p2 = Pila.pila()
p3 = Pila.pila()

def disco3():
    disc2.disco2(p1,p2,p3)
    x =p1.pop()
    p2.push(x)
    print(p1.items)
    print(p2.items)
    print(p3.items,"\n")
    x =p3.pop()
    p1.push(x)
    print(p1.items)
    print(p2.items)
    print(p3.items,"\n")
    x =p3.pop()
    p2.push(x)
    print(p1.items)
    print(p2.items)
    print(p3.items,"\n")
    x =p1.pop()
    p2.push(x)
    print(p1.items)
    print(p2.items)
    print(p3.items,"\n")

while True:
    try:
        valor = int(input("Ingrese discos : "))
        suma = valor
        if valor> 1 and valor < 4:
            if valor==2:
                for i in range(valor):
                    p1.push(suma)
                    suma -=1
                disc2.disco2(p1,p2,p3)
                break
            elif valor==3:
                for i in range(valor):
                    p1.push(suma)
                    suma -=1
                disco3()
                break
        else:
            print("ingrese solo 2 y 3")  
            pass
    except ValueError:
        print("se detecto un valor incorrecto")
        pass