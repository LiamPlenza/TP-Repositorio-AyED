import os, time

def menu_principal():
    clear_shell()
    return print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1 :
            menu_opciones()
        elif 1 < option < 8:
            print("Esta Función está en desarrollo...")
            time.sleep(2)
            menu_administraciones()
        else:
            print("La opcion elegida no se encuentra entre las dadas imbecil. Rompiste todo ")  
            time.sleep(2)
            menu_administraciones()  

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if 1 <= option <= 4:
            print("Esta Función está en desarrollo...")
        else:
            print("La opcion elegida no se encuentra entre las dadas imbecil. Rompiste todo ")  
        time.sleep(2)
        menu_opciones()

def menu_recepcion(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja = ingreso_de_datos(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
        else:
            print("Ingrese una opción valida del menu... Imbecil")
            time.sleep(2) 
        menu_recepcion()
    return camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja
    
def ingreso_de_datos(camionMaiz, pesoNetoMai, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja): 
    tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()
    patCamion = input("Ingrese la patente: ").upper()
    pesoNeto = float(input("Ingrese el peso bruto del camión: ")) - float(input("Ingrese la tara del camión: "))
    
    #CAnt camion = camionsoja+ camion maiz
    print("El peso neto del camión ingresado es: ",pesoNeto)
    time.sleep(2)

    if tipoCamion == "SOJA":
        camionSoja= camionSoja + 1 
        pesoNetoSoja = pesoNetoSoja + pesoNeto
        #promPesoNetoS = pesoNetoSoja / camionSoja
        if pesoNetoSoja > pesoMayorSoja:
            pesoMayorSoja = pesoNetoSoja
            patMayorSoja = patCamion
    elif tipoCamion == "MAIZ":
        camionMaiz = camionMaiz + 1
        pesoNetoMaiz = pesoNetoSoja + pesoNeto
        #promPesoNetoM = pesoNetoMaiz / camionMaiz
        if pesoNetoMaiz < pesoMenorMaiz:
            pesoMenorMaiz = pesoNetoMaiz
            patMenorMaiz = patCamion
    else: 
        print("Ingrese un Proucto valido")
        ingreso_de_datos()
    return camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja

def menu_reportes(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    print("0 - Volver al menu anterior\n1 - Msotrar el reporte actual")
    
    option = int(input("Seleccione una opción del menu: "))
    if option == 0:
        menu_principal()
    elif option == 1:
        mostrar_reporte(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
    else:
        print("Ingrese una opcion válida")
        clear_shell()
        menu_reportes()

def mostrar_reporte(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja):
    return print(f"La cantidad total de camiones es: {camionMaiz + camionSoja}\nLa cantidad de camiones de maiz es: {camionMaiz}\nLa cantidad de camiones de soja es: {camionSoja}\nEl peso neto correspondiente al maiz es: {pesoNetoMaiz}\nEl peso neto correspondiente a la soja es: {pesoNetoSoja}\nEl promedio del peso neto correspondiente al maíz es: {pesoNetoMaiz/camionMaiz}\nEl promedio del peso neto correspondiente a la soja es: {pesoNetoSoja/camionSoja}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}")

# para determinar el sistema operativo y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

if __name__ == "__main__":
    camionMaiz = pesoNetoMaiz = pesoMenorMaiz = camionSoja = pesoNetoSoja = pesoMayorSoja = 0
    patMayorSoja = patMenorMaiz = ""
    menu_principal()
    option = int(input("Seleccione una opción del menu: "))
    
    #diccionario con las opciones y las funciones correspondientes
    #my_dict = {
    #    1: menu_administraciones,
    #    3: menu_recepcion,
    #    8: menu_reportes
    #}

    while option != 0:
        #busca la llave correspondiente a la opcion, si existe llama a la funcion sino ejecuta lambda -> reemplaza los if
        #my_dict.get(option, lambda: print("Esta funcionalidad está en construcción"))()

        if option == 1:
            menu_administraciones()
        elif option == 3:
            menu_recepcion(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
        elif option == 8:
            menu_reportes(camionMaiz, pesoNetoMaiz, patMenorMaiz, pesoMenorMaiz, camionSoja, pesoNetoSoja, patMayorSoja, pesoMayorSoja)
        else:
          print("Esta funcionalidad está en construcción \n")
        
        menu_principal()
        option = int(input("Seleccione una opción del menu: "))
    print("Salio")