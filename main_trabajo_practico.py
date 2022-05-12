import os, time
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás Maximiliano García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""

# valido que el ingreso de las opciones del menu sean numericos
def checkeonum():
    validacion = False
    while not validacion:
        try:
            option = int((input("Seleccione una opción del menu: ")))
            validacion = True
        except ValueError:
            print("Ingrese un valor numérico")
    return option

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar_reporte(dict_data):
    print("------------------------------\nLa cantidad total de camiones es: {totalCamiones}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto total correspondiente al maiz es: {pesoNetoTotalMaiz}\nEl peso neto total correspondiente a la soja es: {pesoNetoTotalSoja}\nEl promedio del peso neto correspondiente al maíz por camión es: {promPesoNetoM}\nEl promedio del peso neto correspondiente a la soja por camión es: {promPesoNetoS}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}".format(totalCamiones=dict_data["camionesMaiz"] + dict_data["camionesSoja"], camionesMaiz=dict_data["camionesMaiz"], camionesSoja=dict_data["camionesSoja"], pesoNetoTotalMaiz=dict_data["pesoNetoMaiz"], pesoNetoTotalSoja=dict_data["pesoNetoSoja"],promPesoNetoM=dict_data["promPesoNetoM"], promPesoNetoS=dict_data["promPesoNetoS"], patMenorMaiz=dict_data["patMenorMaiz"], patMayorSoja=dict_data["patMayorSoja"]))
    input("Precione una tecla para continuar... ")
    #os.system("pause")

def menu_reportes(dict_data):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = checkeonum()
    while option != 0:
        if option == 1:
            if dict_data["camionesMaiz"] == dict_data["camionesSoja"] == 0: # en caso de que no se hayan ingresado camiones aún
                print("Todavía no ingreso ningun camión")
            else:
                mostrar_reporte(dict_data)
        else:
            print("Ingrese una opcion válida")
        time.sleep(1)
        option = 0
        menu_reportes(dict_data)

def ingreso_de_datos(dict_data): 
    clear_shell()
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()

    if tipoCamion in ["SOJA", "S", "MAIZ", "MAÍZ", "M"]:
        patCamion = input("Ingrese la patente: ").upper()
        pesoBruto = float(input("Ingrese el peso bruto del camión en kilogramos: "))
        while pesoBruto <= 0 or pesoBruto > 52500: 
            pesoBruto = float(input("El peso bruto del camión es incorrecto\nIngrese el peso bruto en kilogramos en kilogramos (debe ser un num positivo menor a 52500): "))

        tara = float(input("Ingrese la tara del camión en kilogramos: "))
        while tara < 0 or tara > pesoBruto:
            tara = float(input("La tara del camión es incorrecta\nIngrese la tara del camión en kilogramos (debe ser un num positivo menor al peso bruto): "))
        
        pesoNeto = pesoBruto - tara
        print("El peso neto del camión ingresado es: ",pesoNeto)
        time.sleep(1)
        if tipoCamion == "SOJA": # si se ingresa un camión de soja, mantengo los valores correspondientes al maíz sumandole cero para poder retornarlos
            dict_data['camionesSoja'] += 1 
            dict_data['pesoNetoSoja'] += pesoNeto
            dict_data['promPesoNetoS'] = dict_data['pesoNetoSoja'] / dict_data['camionesSoja']
            if pesoNeto > dict_data['pesoMayorSoja']:
                dict_data['pesoMayorSoja'] = pesoNeto
                dict_data['patMayorSoja'] = patCamion
        else: # si se ingresa un camión de maíz, mantengo los valores correspondientes al soja sumandole cero para poder retornarlos
            dict_data['pesoNetoMaiz'] += pesoNeto
            if dict_data['camionesMaiz'] == 0 or pesoNeto < dict_data['pesoMenorMaiz']:
                dict_data['pesoMenorMaiz'] = pesoNeto
                dict_data['patMenorMaiz'] = patCamion
            dict_data['camionesMaiz'] += 1
            dict_data['promPesoNetoM'] = dict_data['pesoNetoMaiz'] / dict_data['camionesMaiz']
    else:
        print("Ingrese un Proucto valido")
        time.sleep(1)
        ingreso_de_datos(dict_data)

def menu_recepcion(dict_data):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = checkeonum()
    while option != 0:
        if option == 1:
            dict_data = ingreso_de_datos(dict_data)
        else:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")
        time.sleep(1)
        option = 0
        menu_recepcion(dict_data)
    return dict_data

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = checkeonum()
    while option != 0:
        if 1 <= option <= 4:
            print("Esta funcionalidad está en construcción")
        else:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")  
        time.sleep(1)
        option = 0 # ver porque no funciona el flujo de código, esta linea no deberia ser necesaria
        menu_opciones()

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = checkeonum()
    while option != 0:
        if option == 1 :
            menu_opciones()
        elif 1 < option < 8:
            print("Esta funcionalidad está en construcción")
        else:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")  
        option = 0 
        time.sleep(1)
        menu_administraciones()

def menu_principal(dict_data):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = checkeonum()
    while option != 0:
        if option < 1 or option > 8:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo a")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 3:
                menu_recepcion(dict_data)
            elif option == 8:
                menu_reportes(dict_data)
            else:
                clear_shell()
                print("Esta funcionalidad está en construcción \n")
        option = 0 
        time.sleep(1)
        menu_principal(dict_data) 

if __name__ == "__main__":
    # inicialización de las variables a mostrar
    dict_data = {"camionesMaiz": 0,"pesoNetoMaiz": 0, "pesoMenorMaiz": 0, "camionesSoja": 0, "pesoNetoSoja": 0, "pesoMayorSoja": 0, "promPesoNetoS": 0, "promPesoNetoM": 0, "patMayorSoja": "", "patMenorMaiz": ""}
    menu_principal(dict_data)