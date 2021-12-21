from vehiculo import vehiculo

class moto(vehiculo):
    def __init__(self) -> None:
        super().__init__()
        self.marca=input("\ncual es su marca :")
        self.modelo=input("\ncual es su modelo :")
        self.km= int(input("\ncual es su kilometraje :"))
        self.precio=float(input("\ningrese precio :"))
        self.casco =int( input("\ningrese 1 si quiere casco 2 si no desea : "))
    
    def obtener_precio(self) -> float:
        if self.casco == 1:
            return self.precio+80
        elif self.casco==2:
            return self.precio