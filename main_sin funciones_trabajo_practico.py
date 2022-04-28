import os, time
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Plenza - Comisión 104
    Tomas Wardoloff - Comisión 108
"""
if __name__ == "__main__":
    # inicialización de las variables a mostrar
    camionesMaiz = pesoNetoMaiz = pesoMenorMaiz = camionesSoja = pesoNetoSoja = pesoMayorSoja = promPesoNetoM = promPesoNetoS= 0
    patMayorSoja = patMenorMaiz = ""
    
    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if 1 < option > 8:
            print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo a")
        else:
            if option == 1:
                os.system("clear")
                print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")

                option_administraciones = int(input("Seleccione una opción del menu: "))
                while option_administraciones != 0:
                    if option_administraciones == 1:
                        os.system("clear")
                        print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")

                        option_menu_terciario = int(input("Seleccione una opción del menu: "))
                        while option_menu_terciario != 0:
                            if 1 <= option_menu_terciario <= 4:
                                print("Esta funcionalidad está en construcción")
                            else:
                                print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")  
                            time.sleep(1)
                            os.system("clear")

                            print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
                            option_menu_terciario = int(input("Seleccione una opción del menu: "))
                    elif 1 < option_administraciones < 8:
                        print("Esta funcionalidad está en construcción")
                    else:
                        print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")  
                    time.sleep(1)
                    os.system("clear")

                    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
                    option_administraciones = int(input("Seleccione una opción del menu: "))
            elif option == 3:
                os.system("clear")
                print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")

                option_recepcion = int(input("Seleccione una opción del menu: "))
                while option_recepcion != 0:
                    if option_recepcion == 1:
                        os.system("clear")
                        tipoCamion = input("Ingrese si el camion contiene Soja o Maíz: ").upper()

                        if not (tipoCamion == "SOJA" or tipoCamion == "MAIZ"): # en caso de que se ingrese otro tipo de producto
                            print("Ingrese un Proucto valido")
                            
                            time.sleep(1)
                            os.system("clear")
                            print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
                            option_recepcion = int(input("Seleccione una opción del menu: "))
                        else:
                            patCamion = input("Ingrese la patente: ").upper()
                            pesoNeto = float(input("Ingrese el peso bruto del camión: ")) - float(input("Ingrese la tara del camión: "))

                            print("El peso neto del camión ingresado es: ",pesoNeto)
                            time.sleep(1)
                            if tipoCamion == "SOJA": # si se ingresa un camión de soja, mantengo los valores correspondientes al maíz sumandole cero para poder retornarlos
                                camionesSoja += 1 
                                pesoNetoSoja += pesoNeto
                                promPesoNetoS = pesoNetoSoja / camionesSoja
                                if pesoNetoSoja > pesoMayorSoja:
                                    pesoMayorSoja = pesoNetoSoja
                                    patMayorSoja = patCamion
                                camionesMaiz += 0
                                pesoNetoMaiz += 0
                            else: # si se ingresa un camión de maíz, mantengo los valores correspondientes al soja sumandole cero para poder retornarlos
                                camionesMaiz += 1
                                pesoNetoMaiz += pesoNeto
                                promPesoNetoM = pesoNetoMaiz / camionesMaiz
                                if pesoNetoMaiz < pesoMenorMaiz:
                                    pesoMenorMaiz = pesoNetoMaiz
                                    patMenorMaiz = patCamion
                                camionesSoja += 0
                                pesoNetoSoja += 0
                    else:
                        print("La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo ")
                    time.sleep(1)
                    os.system("clear")

                    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
                    option_recepcion = int(input("Seleccione una opción del menu: "))
            elif option == 8:
                os.system("clear")
                print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

                option_reportes = int(input("Seleccione una opción del menu: "))
                while option_reportes != 0:
                    if option_reportes == 1:
                        if camionesMaiz == camionesSoja == 0: # en caso de que no se hayan ingresado camiones aún
                            print("Todavía no ingreso ningun camión") 
                        else:
                            print(f"------------------------------\nLa cantidad total de camiones es: {camionesMaiz + camionesSoja}\nLa cantidad de camiones de maiz es: {camionesMaiz}\nLa cantidad de camiones de soja es: {camionesSoja}\nEl peso neto correspondiente al maiz es: {pesoNetoMaiz}\nEl peso neto correspondiente a la soja es: {pesoNetoSoja}\nEl promedio del peso neto correspondiente al maíz es: {promPesoNetoM}\nEl promedio del peso neto correspondiente a la soja es: {promPesoNetoS}\nLa patente correspondiente al camión que menos maíz descargo es: {patMenorMaiz}\nLa patente correspondiente al camión que más soja descargo es: {patMayorSoja}")
                            time.sleep(5)
                    else:
                        print("Ingrese una opcion válida")
                    time.sleep(1)
                    os.system("clear")

                    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
                    option_reportes = int(input("Seleccione una opción del menu: "))
            else:
                print("Esta funcionalidad está en construcción")
        time.sleep(1)
        os.system("clear")
        
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = int(input("Seleccione una opción del menu: "))