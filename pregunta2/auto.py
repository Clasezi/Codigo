from vehiculo import vehiculo
class auto (vehiculo):
    def __init__(self) -> None:
        super().__init__()
        self.marca= input("ingrese marca : ")
        self.modelo= input("\ningrese modelo :")
        self.km = int(input("\ningrese kilometraje : "))
        self.precio = float (input("\ningrese precio : "))
        self.airbag = int(input("\ningrese uno si quiere aibrag y 2 si no quiere : "))
    def obtener_precio(self) -> float:
        if self.airbag == 1:
            return self.precio+300
        elif self.airbag ==2:
            return self.precio