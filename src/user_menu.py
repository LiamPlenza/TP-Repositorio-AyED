import os, time, input_validation
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar_reporte(Maiz,Soja):
    if Maiz.camionesMaiz == 0:
        print("------------------------------\nLa cantidad total de camiones es: ",Soja.camionesSoja,"\nLa cantidad de camiones de soja es: ",Soja.camionesSoja,"\nEl peso neto total correspondiente a la soja es: ",Soja.pesoNetoSoja,"\nEl promedio del peso neto correspondiente a la soja por camión es: ",Soja.promPesoNetoS,"\nLa patente correspondiente al camión que más soja descargo es:",Soja.patMayorSoja)
        print("------------------------------\nNo se han ingresado camiones de Maiz...\n------------------------------")
    elif Soja.camionesSoja == 0:
        print("------------------------------\nLa cantidad total de camiones es: ",Maiz.camionesMaiz,"\nLa cantidad de camiones de maiz es: ",Maiz.camionesMaiz,"\nEl peso neto total correspondiente al maiz es: ",Maiz.pesoNetoMaiz,"\nEl promedio del peso neto correspondiente al maíz por camión es: ",Maiz.promPesoNetoM,"\nLa patente correspondiente al camión que menos maíz descargo es: ",Maiz.patMenorMaiz)
        print("------------------------------\nNo se han ingresado camiones de Soja...\n------------------------------")
    else:
        print("------------------------------\nLa cantidad total de camiones es: ", Soja.camionesSoja+Maiz.camionesMaiz,"\nLa cantidad de camiones de maiz es: ",Maiz.camionesMaiz,"\nLa cantidad de camiones de soja es: ",Soja.camionesSoja,"\nEl peso neto total correspondiente al maiz es: ",Maiz.pesoNetoMaiz,"\nEl peso neto total correspondiente a la soja es: ",Soja.pesoNetoSoja,"\nEl promedio del peso neto correspondiente al maíz por camión es: ",Maiz.promPesoNetoM,"\nEl promedio del peso neto correspondiente a la soja por camión es: ",Soja.promPesoNetoS,"\nLa patente correspondiente al camión que menos maíz descargo es: ",Maiz.patMenorMaiz,"\nLa patente correspondiente al camión que más soja descargo es: ",Soja.patMayorSoja)
    input("Precione una tecla para continuar... ")
    #os.system("pause")

def menu_reportes(Maiz,Soja):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            if Maiz.camionesMaiz == Soja.camionesSoja == 0: # en caso de que no se hayan ingresado camiones aún
                print(f"{WARNING}Todavía no ingreso ningun camión{NORMAL}")
            else:
                mostrar_reporte(Maiz,Soja)
        else:
            print(f"{WARNING}Ingrese una opcion válida{NORMAL}")
        time.sleep(1.5)
        option = 0
        menu_reportes(Maiz,Soja)

def guardar_datos(Maiz,Soja , tipoCamion: str, patCamion: str, pesoNeto: float):
    if tipoCamion in ["S","SOJA"]:
            Soja.camionesSoja += 1 
            Soja.pesoNetoSoja += pesoNeto
            Soja.promPesoNetoS = Soja.pesoNetoSoja / Soja.camionesSoja
            if pesoNeto > Soja.pesoMayorSoja:
                Soja.pesoMayorSoja = pesoNeto
                Soja.patMayorSoja = patCamion
    else: 
        Maiz.pesoNetoMaiz += pesoNeto
        if Maiz.camionesMaiz == 0 or pesoNeto < Maiz.pesoMenorMaiz:
            Maiz.pesoMenorMaiz = pesoNeto
            Maiz.patMenorMaiz = patCamion
        Maiz.camionesMaiz += 1
        Maiz.promPesoNetoM = Maiz.pesoNetoMaiz / Maiz.camionesMaiz

def ingreso_de_datos(Maiz,Soja): 
    clear_shell()
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
        guardar_datos(Maiz,Soja, tipoCamion, patCamion, pesoNeto = pesoBruto - tara)
        time.sleep(1.5)
    else:
        print("Ingrese un Proucto valido")
        time.sleep(2)
        ingreso_de_datos(Maiz,Soja)

def menu_recepcion(Maiz,Soja) -> dict:
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            ingreso_de_datos(Maiz,Soja)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1)
        option = 0
        menu_recepcion(Maiz,Soja)
    return Maiz,Soja

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = input_validation.check_int()
    while option != 0:
        if 1 <= option <= 4:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        option = 0
        menu_opciones()

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = input_validation.check_int()
    while option != 0:
        if option == 1 :
            menu_opciones()
        elif 1 < option < 8:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        option = 0 
        time.sleep(1.5)
        menu_administraciones()

def menu_principal(Maiz,Soja):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = input_validation.check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 3:
                menu_recepcion(Maiz,Soja)
            elif option == 8:
                menu_reportes(Maiz,Soja)
            else:
                clear_shell()
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        option = 0 
        time.sleep(1.5)
        menu_principal(Maiz,Soja) 