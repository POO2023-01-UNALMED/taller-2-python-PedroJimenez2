class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        pass

class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados = cantidadCreados

    def cantidadAsientos(self):
        pass
    def verificarIntegridad(self):
        if self.registro.Asiento != self.registro.Auto and self.registro.Asiento != self.registro.motor and self.registro.Auto != self.registro.Motor:
            print("Las piezas no son originales")
        else:
            print("Auto original")

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,registro):
        pass
    def asignarTipo(self,tipo):
        if tipo == "electrico":
            print("electrico")
        elif tipo == "gasolina":
            print("gasolina")
        else:
            pass

if __name__ == "__main__":
    asiento1 = Asiento("Verde",20,509)
    auto1 = Auto("2018",25,[Asiento],"BMW",Motor,509,5) 
    motor1 = Motor(5,"cilindrado",509)
    print(auto1.asientos)
