import os, time
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Plenza - Comisión 104
    Tomas Wardoloff - Comisión 108
"""

# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar_reporte(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    print(f"La cantidad total de camiones es: {camionesMaiz + camionesSoja}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto correspondiente al maiz es: {pesoNetoMaiz}\nEl peso neto correspondiente a la soja es: {pesoNetoSoja}\nEl promedio del peso neto correspondiente al maíz es: {pesoNetoMaiz/camionesMaiz}\nEl promedio del peso neto correspondiente a la soja es: {pesoNetoSoja/camionesSoja}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}")
    time.sleep(5)

def menu_reportes(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            if camionesMaiz == camionesSoja == 0: # en caso de que no se hayan ingresado camiones aún
                print("Todavía no ingreso ningun camión") 
            else:
                mostrar_reporte(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
        else:
            print("Ingrese una opcion válida")
        time.sleep(1)
        option = 0 # ver porque no funciona el flujo de código, esta linea no deberia ser necesaria
        menu_reportes(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)

def ingreso_de_datos(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja): 
    clear_shell()
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()
    print(tipoCamion)

    if not tipoCamion == "SOJA" or tipoCamion == "MAIZ": # en caso de que se ingrese otro tipo de producto
        print("Ingrese un Proucto valido")
        time.sleep(1)
        ingreso_de_datos(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
    else:
        patCamion = input("Ingrese la patente: ").upper()
        pesoNeto = float(input("Ingrese el peso bruto del camión: ")) - float(input("Ingrese la tara del camión: "))

        print("El peso neto del camión ingresado es: ",pesoNeto)
        time.sleep(1)
        if tipoCamion == "SOJA": # si se ingresa un camión de soja, mantengo los valores correspondientes al maíz sumandole cero para poder retornarlos
            camionesSoja =+ 1 
            pesoNetoSoja =+ pesoNeto
            promPesoNetoS = pesoNetoSoja / camionesSoja
            if pesoNetoSoja > pesoMayorSoja:
                pesoMayorSoja = pesoNetoSoja
                patMayorSoja = patCamion
            camionesMaiz =+ 0
            pesoNetoMaiz =+ 0
        else: # si se ingresa un camión de maíz, mantengo los valores correspondientes al soja sumandole cero para poder retornarlos
            camionesMaiz =+ 1
            pesoNetoMaiz =+ pesoNeto
            promPesoNetoM = pesoNetoMaiz / camionesMaiz
            if pesoNetoMaiz < pesoMenorMaiz:
                pesoMenorMaiz = pesoNetoMaiz
                patMenorMaiz = patCamion
            camionesSoja =+ 0
            pesoNetoSoja =+ 0
    return camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja

def menu_recepcion(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja = ingreso_de_datos(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
        else:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")
        time.sleep(1)
        option = 0 # ver porque no funciona el flujo de código, esta linea no deberia ser necesaria
        menu_recepcion(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
    return camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = int(input("Seleccione una opción del menu: "))
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
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1 :
            menu_opciones()
        elif 1 < option < 8:
            print("Esta funcionalidad está en construcción")
        else:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")  
        option = 0 # ver porque no funciona el flujo de código, esta linea no deberia ser necesaria
        time.sleep(1)
        menu_administraciones()

def menu_principal(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if 1 < option > 8:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo a")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 3:
                camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja = menu_recepcion(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
            elif option == 8:
                menu_reportes(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
            else:
                print("Esta funcionalidad está en construcción \n")
        option = 0 # ver porque no funciona el flujo de código, esta linea no deberia ser necesaria
        time.sleep(1)
        menu_principal(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja) 

if __name__ == "__main__":
    # inicialización de las variables a mostrar
    camionesMaiz = pesoNetoMaiz = pesoMenorMaiz = camionesSoja = pesoNetoSoja = pesoMayorSoja = 0
    patMayorSoja = patMenorMaiz = ""
    
    menu_principal(camionesMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionesSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)