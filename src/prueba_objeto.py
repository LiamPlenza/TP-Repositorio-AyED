import input_validation
from user_menu import ObjetoSoja
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

class ObejtoSoja:
    def __init__(self):
        self.camiones = self.pesoNeto = self.pesoMayor = self.promPesoNeto = 0
        self.patMayor = ""

    def actualizar_datos(self, patente, pesoNeto):
        self.camiones += 1
        self.pesoNeto += pesoNeto
        self.promPesoNeto = self.pesoNeto / self.camiones
        
        if pesoNeto[0] > self.pesoMayor:
            self.pesoMayor = pesoNeto[0]#pesoNeto
            self.patMayor = patente#patente

    def mostrar_datos(self):
        return f"------------------------------\nLa cantidad total de camiones es: {self.camiones}\nLa cantidad de camiones de soja es: {self.camiones}\nEl peso neto total correspondiente a la soja es: {self.pesoNeto}\nEl promedio del peso neto correspondiente a la soja por camión es: {self.promPesoNeto}\nLa patente correspondiente al camión que más soja descargo es: {self.patMayor}"


def ingreso_de_datos(Soja: ObejtoSoja):
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()

    if tipoCamion in ["SOJA", "S", "MAIZ", "MAÍZ", "M"]:
        patCamion = input_validation.check_pat()
        pesoBruto = input_validation.check_float(mensaje="Ingrese el peso bruto del camión en kilogramos: ")
        while pesoBruto <= 0 or pesoBruto > 52500: 
            pesoBruto = input_validation.check_float(mensaje=f"{WARNING}El peso bruto del camión es incorrecto{NORMAL}\nIngrese el peso bruto en kilogramos en kilogramos (debe ser un num positivo menor a 52500): ")

        tara = input_validation.check_float(mensaje="Ingrese la tara del camión en kilogramos: ")
        while tara < 0 or tara > pesoBruto:
            tara = input_validation.check_float(mensaje=f"{WARNING}La tara del camión es incorrecta{NORMAL}\nIngrese la tara del camión en kilogramos (debe ser un num positivo menor al peso bruto): ")
        
        print("El peso neto del camión ingresado es: ",pesoBruto - tara)
        if tipoCamion in ["S", "SOJA"]:
            Soja.actualizar_datos(patCamion, pesoNeto= pesoBruto - tara)
        else:
            pass

def check(Soja: ObjetoSoja):
    if Soja.camiones == 0:
        print("No hay camiones")

if __name__ == "__main__":
    # inicialización de las variables a mostrar
    soja = ObejtoSoja()
    check(soja)
