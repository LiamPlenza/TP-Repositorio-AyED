import os, time
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás Maximiliano García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

def check_float(mensaje: str)-> float:
    while True:
        try:
            option = float((input(mensaje)))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")

# valido que el ingreso de las opciones del menu sean numericos
def check_int()-> int:
    while True:
        try:
            option = int((input("Seleccione una opción del menu: ")))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar_reporte(dict_data: dict):
    if dict_data["camionesMaiz"] == 0:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto total correspondiente a la soja es: {pesoNetoTotalSoja}\nEl promedio del peso neto correspondiente a la soja por camión es: {promPesoNetoS}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}".format(totalCamiones=dict_data["camionesMaiz"] + dict_data["camionesSoja"], camionesSoja=dict_data["camionesSoja"], pesoNetoTotalSoja=dict_data["pesoNetoSoja"], promPesoNetoS=dict_data["promPesoNetoS"], patMayorSoja=dict_data["patMayorSoja"]))
        print("------------------------------\nNo se han ingresado camiones de Maiz...\n------------------------------")
    elif dict_data["camionesSoja"] == 0:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nEl peso neto total correspondiente al maiz es: {pesoNetoTotalMaiz}\nEl promedio del peso neto correspondiente al maíz por camión es: {promPesoNetoM}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}".format(totalCamiones=dict_data["camionesMaiz"] + dict_data["camionesSoja"], camionesMaiz=dict_data["camionesMaiz"], pesoNetoTotalMaiz=dict_data["pesoNetoMaiz"],promPesoNetoM=dict_data["promPesoNetoM"], patMenorMaiz=dict_data["patMenorMaiz"],))
        print("------------------------------\nNo se han ingresado camiones de Soja...\n------------------------------")
    else:
        print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto total correspondiente al maiz es: {pesoNetoTotalMaiz}\nEl peso neto total correspondiente a la soja es: {pesoNetoTotalSoja}\nEl promedio del peso neto correspondiente al maíz por camión es: {promPesoNetoM}\nEl promedio del peso neto correspondiente a la soja por camión es: {promPesoNetoS}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}".format(totalCamiones=dict_data["camionesMaiz"] + dict_data["camionesSoja"], camionesMaiz=dict_data["camionesMaiz"], camionesSoja=dict_data["camionesSoja"], pesoNetoTotalMaiz=dict_data["pesoNetoMaiz"], pesoNetoTotalSoja=dict_data["pesoNetoSoja"],promPesoNetoM=dict_data["promPesoNetoM"], promPesoNetoS=dict_data["promPesoNetoS"], patMenorMaiz=dict_data["patMenorMaiz"], patMayorSoja=dict_data["patMayorSoja"]))
    input("Precione una tecla para continuar... ")
    #os.system("pause")

def menu_reportes(dict_data: dict):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = check_int()
    while option != 0:
        if option == 1:
            if dict_data["camionesMaiz"] == dict_data["camionesSoja"] == 0: # en caso de que no se hayan ingresado camiones aún
                print(f"{WARNING}Todavía no ingreso ningun camión{NORMAL}")
            else:
                mostrar_reporte(dict_data)
        else:
            print(f"{WARNING}Ingrese una opcion válida{NORMAL}")
        time.sleep(1.5)
        option = 0
        menu_reportes(dict_data)

def guardar_datos(tipoCamion: str, patCamion: str, pesoNeto: float):
    if tipoCamion in ["S","SOJA"]:
            dict_data['camionesSoja'] += 1 
            dict_data['pesoNetoSoja'] += pesoNeto
            dict_data['promPesoNetoS'] = dict_data['pesoNetoSoja'] / dict_data['camionesSoja']
            if pesoNeto > dict_data['pesoMayorSoja']:
                dict_data['pesoMayorSoja'] = pesoNeto
                dict_data['patMayorSoja'] = patCamion
    else: 
        dict_data['pesoNetoMaiz'] += pesoNeto
        if dict_data['camionesMaiz'] == 0 or pesoNeto < dict_data['pesoMenorMaiz']:
            dict_data['pesoMenorMaiz'] = pesoNeto
            dict_data['patMenorMaiz'] = patCamion
        dict_data['camionesMaiz'] += 1
        dict_data['promPesoNetoM'] = dict_data['pesoNetoMaiz'] / dict_data['camionesMaiz']

def ingreso_de_datos(dict_data: dict): 
    clear_shell()
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()

    if tipoCamion in ["SOJA", "S", "MAIZ", "MAÍZ", "M"]:
        patCamion = input("Ingrese la patente: ").upper()
        pesoBruto = check_float(mensaje="Ingrese el peso bruto del camión en kilogramos: ")
        while pesoBruto <= 0 or pesoBruto > 52500: 
            pesoBruto = check_float(mensaje=f"{WARNING}El peso bruto del camión es incorrecto{NORMAL}\nIngrese el peso bruto en kilogramos en kilogramos (debe ser un num positivo menor a 52500): ")

        tara = check_float(mensaje="Ingrese la tara del camión en kilogramos: ")
        while tara < 0 or tara > pesoBruto:
            tara = check_float(mensaje=f"{WARNING}La tara del camión es incorrecta{NORMAL}\nIngrese la tara del camión en kilogramos (debe ser un num positivo menor al peso bruto): ")
        
        print("El peso neto del camión ingresado es: ",pesoBruto - tara)
        guardar_datos(tipoCamion, patCamion, pesoNeto = pesoBruto - tara)
        time.sleep(1.5)
    else:
        print("Ingrese un Proucto valido")
        time.sleep(2)
        ingreso_de_datos(dict_data)

def menu_recepcion(dict_data: dict) -> dict:
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = check_int()
    while option != 0:
        if option == 1:
            dict_data = ingreso_de_datos(dict_data)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1)
        option = 0
        menu_recepcion(dict_data)
    return dict_data

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = check_int()
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
    
    option = check_int()
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

def menu_principal(dict_data: dict):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 3:
                menu_recepcion(dict_data)
            elif option == 8:
                menu_reportes(dict_data)
            else:
                clear_shell()
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        option = 0 
        time.sleep(1.5)
        menu_principal(dict_data) 

if __name__ == "__main__":
    # inicialización de las variables a mostrar
    dict_data = {"camionesMaiz": 0,"pesoNetoMaiz": 0, "pesoMenorMaiz": 0, "camionesSoja": 0, "pesoNetoSoja": 0, "pesoMayorSoja": 0, "promPesoNetoS": 0, "promPesoNetoM": 0, "patMayorSoja": "", "patMenorMaiz": ""}
    menu_principal(dict_data)