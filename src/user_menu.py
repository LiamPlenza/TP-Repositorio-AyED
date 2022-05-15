import os, time, input_validation
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar_reporte(dictionary: dict):
    if dictionary["camionesMaiz"] == 0:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto total correspondiente a la soja es: {pesoNetoTotalSoja}\nEl promedio del peso neto correspondiente a la soja por camión es: {promPesoNetoS}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}".format(totalCamiones=dictionary["camionesMaiz"] + dictionary["camionesSoja"], camionesSoja=dictionary["camionesSoja"], pesoNetoTotalSoja=dictionary["pesoNetoSoja"], promPesoNetoS=dictionary["promPesoNetoS"], patMayorSoja=dictionary["patMayorSoja"]))
        print("------------------------------\nNo se han ingresado camiones de Maiz...\n------------------------------")
    elif dictionary["camionesSoja"] == 0:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nEl peso neto total correspondiente al maiz es: {pesoNetoTotalMaiz}\nEl promedio del peso neto correspondiente al maíz por camión es: {promPesoNetoM}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}".format(totalCamiones=dictionary["camionesMaiz"] + dictionary["camionesSoja"], camionesMaiz=dictionary["camionesMaiz"], pesoNetoTotalMaiz=dictionary["pesoNetoMaiz"],promPesoNetoM=dictionary["promPesoNetoM"], patMenorMaiz=dictionary["patMenorMaiz"],))
        print("------------------------------\nNo se han ingresado camiones de Soja...\n------------------------------")
    else:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto total correspondiente al maiz es: {pesoNetoTotalMaiz}\nEl peso neto total correspondiente a la soja es: {pesoNetoTotalSoja}\nEl promedio del peso neto correspondiente al maíz por camión es: {promPesoNetoM}\nEl promedio del peso neto correspondiente a la soja por camión es: {promPesoNetoS}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}".format(totalCamiones=dictionary["camionesMaiz"] + dictionary["camionesSoja"], camionesMaiz=dictionary["camionesMaiz"], camionesSoja=dictionary["camionesSoja"], pesoNetoTotalMaiz=dictionary["pesoNetoMaiz"], pesoNetoTotalSoja=dictionary["pesoNetoSoja"],promPesoNetoM=dictionary["promPesoNetoM"], promPesoNetoS=dictionary["promPesoNetoS"], patMenorMaiz=dictionary["patMenorMaiz"], patMayorSoja=dictionary["patMayorSoja"]))
    input("Precione una tecla para continuar... ")
    #os.system("pause")

def menu_reportes(dictionary: dict):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            if dictionary["camionesMaiz"] == dictionary["camionesSoja"] == 0: # en caso de que no se hayan ingresado camiones aún
                print(f"{WARNING}Todavía no ingreso ningun camión{NORMAL}")
            else:
                mostrar_reporte(dictionary)
        else:
            print(f"{WARNING}Ingrese una opcion válida{NORMAL}")
        time.sleep(1.5)
        option = 0
        menu_reportes(dictionary)

def guardar_datos(dictionary, tipoCamion: str, patCamion: str, pesoNeto: float):
    if tipoCamion in ["S","SOJA"]:
            dictionary['camionesSoja'] += 1 
            dictionary['pesoNetoSoja'] += pesoNeto
            dictionary['promPesoNetoS'] = dictionary['pesoNetoSoja'] / dictionary['camionesSoja']
            if pesoNeto > dictionary['pesoMayorSoja']:
                dictionary['pesoMayorSoja'] = pesoNeto
                dictionary['patMayorSoja'] = patCamion
    else: 
        dictionary['pesoNetoMaiz'] += pesoNeto
        if dictionary['camionesMaiz'] == 0 or pesoNeto < dictionary['pesoMenorMaiz']:
            dictionary['pesoMenorMaiz'] = pesoNeto
            dictionary['patMenorMaiz'] = patCamion
        dictionary['camionesMaiz'] += 1
        dictionary['promPesoNetoM'] = dictionary['pesoNetoMaiz'] / dictionary['camionesMaiz']

def ingreso_de_datos(dictionary: dict): 
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
        guardar_datos(dictionary, tipoCamion, patCamion, pesoNeto = pesoBruto - tara)
        time.sleep(1.5)
    else:
        print("Ingrese un Proucto valido")
        time.sleep(2)
        ingreso_de_datos(dictionary)

def menu_recepcion(dictionary: dict) -> dict:
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation.check_int()
    while option != 0:
        if option == 1:
            dictionary = ingreso_de_datos(dictionary)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1)
        option = 0
        menu_recepcion(dictionary)
    return dictionary

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

def menu_principal(dictionary: dict):
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
                menu_recepcion(dictionary)
            elif option == 8:
                menu_reportes(dictionary)
            else:
                clear_shell()
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        option = 0 
        time.sleep(1.5)
        menu_principal(dictionary) 