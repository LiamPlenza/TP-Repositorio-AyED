import os, time, input_validation
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

class ObjetoMaiz:
    def __init__(self):
        self.camiones = self.pesoNeto = self.pesoMenor = self.promPesoNeto = 0
        self.patMenor = ""

    def actualizar_datos(self, patente, pesoNeto):
        self.camiones += 1
        self.pesoNeto += pesoNeto
        self.promPesoNeto = self.pesoNeto / self.camiones
        
        if self.camiones == 0 or pesoNeto < self.pesoMenor:
            self.pesoMenor = pesoNeto
            self.patMenor = patente

    def mostrar_datos(self):
        return f"La cantidad de camiones de soja es: {self.camiones}\nEl peso neto total correspondiente a la soja es: {self.pesoNeto}\nEl promedio del peso neto correspondiente a la soja por camión es: {self.promPesoNeto}\nLa patente correspondiente al camión que más soja descargo es: {self.patMenor}"

class ObjetoSoja:
    def __init__(self):
        self.camiones = self.pesoNeto = self.pesoMayor = self.promPesoNeto = 0
        self.patMayor = ""

    def actualizar_datos(self, patente, pesoNeto):
        self.camiones += 1
        self.pesoNeto += pesoNeto
        self.promPesoNeto = self.pesoNeto / self.camiones
        
        if pesoNeto > self.pesoMayor:
            self.pesoMayor = pesoNeto#pesoNeto
            self.patMayor = patente#patente

    def mostrar_datos(self):
        return f"La cantidad de camiones de soja es: {self.camiones}\nEl peso neto total correspondiente a la soja es: {self.pesoNeto}\nEl promedio del peso neto correspondiente a la soja por camión es: {self.promPesoNeto}\nLa patente correspondiente al camión que más soja descargo es: {self.patMayor}"

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def menu_reportes(Maiz: ObjetoMaiz, Soja: ObjetoSoja):
    clear_shell()

    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            if Maiz.camiones == Soja.camiones == 0: # en caso de que no se hayan ingresado camiones aún
                print(f"{WARNING}Todavía no ingreso ningun camión{NORMAL}")
            else: 
                print(f"------------------------------\nLa cantidad total de camiones es: {Maiz.camiones+Soja.camiones}\n------------------------------\n")
                if Maiz.camiones == 0:
                    print(f"{Soja.mostrar_datos()}\n------------------------------\nNo se han ingresado camiones de Maiz...\n------------------------------")
                elif Soja.camiones == 0: 
                    print(f"{Maiz.mostrar_datos()}\n------------------------------\nNo se han ingresado camiones de Soja...\n------------------------------")
                else:
                    print(f"{Soja.mostrar_datos()}\n------------------------------\n{Maiz.mostrar_datos()}")
                input("Precione una tecla para continuar... ")
        else:
            print(f"{WARNING}Ingrese una opcion válida{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
        option = input_validation.check_int()


def ingreso_de_datos(Maiz: ObjetoMaiz, Soja: ObjetoSoja): 
    clear_shell()
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()

    while tipoCamion not in ["SOJA", "S", "MAIZ", "MAÍZ", "M"]:
            print(f"{WARNING}Ingrese un Proucto valido{NORMAL}")
            tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()
    
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
        Maiz.actualizar_datos(patCamion, pesoNeto= pesoBruto - tara)
    time.sleep(1.5)

def menu_recepcion(Maiz: ObjetoMaiz, Soja: ObjetoSoja) -> dict:
    clear_shell()

    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            ingreso_de_datos(Maiz,Soja)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
        option = input_validation.check_int()
    return Maiz,Soja

def alta(titulares):
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Ingresar un nuevo titular")
    option = input_validation.check_int()
    i=0
    while option != 0:
        if option == 1:
            if i == 0:
                titulares.append(input("Ingrese el nombre del titular en cuestión: "))
                time.sleep(1.5)
                i = i + 1
                alta(titulares)
            elif titulares[i] == 0:
                titulares.append(input("Ingrese el nombre del titular en cuestión: "))
                time.sleep(1.5)
                i = i + 1
                alta(titulares)
            else: 
                i+=1
                
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
            time.sleep
            (1.5)
            alta(titulares)
    menu_opciones(titulares)

def baja(titulares):
    clear_shell()
    i = 0
    if titulares == []:
        print("No hay titulares ingresados")
        time.sleep(1.5)
        menu_opciones(titulares)
    else:
        print("La actual lista de titulares es:")
        for x,i in enumerate(titulares):
            print(x+1," - ",i)
    print("0 - Volver al menu anterior ")
    option = input_validation.check_int()
    i = option-1
    x = len(titulares)
    while option != 0:
        if i > x:    
            print(f"{WARNING}Ingrese un titular existente{NORMAL}")
            time.sleep(1.5)
            baja(titulares)
        elif x == i:
            titulares[i] == NULL
        else:
            while x < i:
                titulares[i] = titulares[i+1]
                i+=1
            titulares.pop()
        print("El titular ha sido borrado")
        option = 0
        os.system("pause")

def consulta(titulares):
    clear_shell()
    if titulares == []:
        print("No hay titulares ingresados")
        time.sleep(1.5)
        menu_opciones(titulares)
    else:
        print("La actual lista de titulares es:")
        for x,i in enumerate(titulares):
            print(x+1," - ",i)
    os.system("pause")

def modificacion(titulares):
    clear_shell()
    i = 0
    if titulares == []:
        print("No hay titulares ingresados")
        time.sleep(1.5)
        menu_opciones(titulares)
    else:
        print("La actual lista de titulares es:")
        for x,i in enumerate(titulares):
            print(x+1," - ",i)
    print("0 - Volver al menu anterior ")
    option = input_validation.check_int()
    i = option-1
    x= len(titulares)
    while option != 0:
        if x > i:    
            print(f"{WARNING}Ingrese un titular existente{NORMAL}")
            time.sleep(1.5)
            modificacion(titulares)
        else:
            titulares[i] = input("Ingrese el nombre del nuevo titular: ")
            print("El titular ha sido modificado")
            option = 0
            os.system("pause")
    
def menu_opciones(titulares):
    clear_shell()

    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    option = input_validation.check_int()
    while option != 0:
        if 1 == option:
            alta(titulares)
        elif 2 == option:
            baja(titulares)
        elif option == 3:
            consulta(titulares)
        elif option == 4:
            modificacion(titulares)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
        option = input_validation.check_int()

def menu_administraciones(titulares):
    clear_shell()
    
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    option = input_validation.check_int()
    while option != 0:
        if option == 1 :
            menu_opciones(titulares)
        elif 1 < option < 8:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
        option = input_validation.check_int()

def menu_principal(Maiz: ObjetoMaiz, Soja: ObjetoSoja,titulares):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = input_validation.check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones(titulares)
            elif option == 3:
                menu_recepcion(Maiz,Soja)
            elif option == 8:
                menu_reportes(Maiz,Soja)
            else:
                clear_shell()
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = input_validation.check_int()