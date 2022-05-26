import os, time, abm_titulares, input_validation
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

class ObjetoMaiz:
    def __init__(self):
        self.camiones = self.pesoNeto = self.pesoMenor = self.promPesoNeto = 0
        self.patMenor = ""

def get_data(self):
        return self.camiones, self.pesoNeto, self.pesoMenor, self.promPesoNeto, self.patMenor

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

    def get_data(self):
        return self.camiones, self.pesoNeto, self.pesoMayor, self.promPesoNeto, self.patMayor

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
                print(f"------------------------------\nLa cantidad total de camiones es: {Maiz.camiones+Soja.camiones}")

                print("*------------------------------------------------------------------------------------------------*")
                print("|{:^28}|{:^20}|{:^20}|{:^25}|".format("TOTAL DE CAMIONES DE SOJA", "PESO NETO TOTAL", "PROMEDIO PESO NETO", "CAMIÓN QUE MÁS DESCARGÓ"))
                print("*------------------------------------------------------------------------------------------------*")
                print("|{:^28}|{:^20}|{:^20}|{:^25}|".format(Soja.get_data()[0], Soja.get_data()[1], Soja.get_data()[2], Soja.get_data()[3], Soja.get_data()[4]))
                print("*------------------------------------------------------------------------------------------------*")

                print("*------------------------------------------------------------------------------------------------*")
                print("|{:^28}|{:^20}|{:^20}|{:^25}|".format("TOTAL DE CAMIONES DE MAIZ", "PESO NETO TOTAL", "PROMEDIO PESO NETO", "CAMIÓN QUE MENOS DESCARGÓ"))
                print("*------------------------------------------------------------------------------------------------*")
                print("|{:^28}|{:^20}|{:^20}|{:^25}|".format(Maiz.get_data()[0], Maiz.get_data()[1], Maiz.get_data()[2], Maiz.get_data()[3], Maiz.get_data()[4]))
                print("*------------------------------------------------------------------------------------------------*")
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

def menu_opciones(titulares):
    clear_shell()

    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    option = input_validation.check_int()
    while option != 0:
        if 1 == option:
            abm_titulares.alta(titulares)
        elif 2 == option:
            abm_titulares.baja(titulares)
        elif option == 3:
            abm_titulares.consulta(titulares)
        elif option == 4:
            abm_titulares.modificacion(titulares)
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