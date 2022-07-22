import os, time, input_validation_TP2 , abm_productos_TP2, main_TP2
WARNING = '\033[1;31m'
NORMAL = '\033[0m'
SUCCESS = '\033[1;32m'


# para determinar el sistema operativo donde se ejecuta el programa y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")
    
"""
    Ver el uso del metodo index para evitar la salida forzada del ciclo
"""
def entrega_de_cupos(cupos: list, identificador: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP2.check_int()
    
    while option != 0:
        if option == 1:
            if cupos[7] != "":
                print(f"{WARNING}Se han acabado los cupos por el día de hoy, vuelva mañana. Saludos.{NORMAL}")
            else:
                indice = 0
                print("Ingrese la patente del camión para el que desea hacer cupo")
                patente_ingresada = input_validation_TP2.check_pat()
                
                while patente in cupos:
                    print(f"{WARNING}La patente ya se ingreso el día de hoy.{NORMAL}")
                    patente_ingresada = input_validation_TP2.check_pat()
                
                while indice < len(cupos):# busco el primer espacio en blanco dentro de cupos
                    if cupos[indice] == "":
                        cupos[indice] = patente_ingresada
                        estado[indice] = 'P'
                        identificador[indice] = indice + 1
                        print(f"{SUCCESS}Se ha otorgado el cupo con éxito{NORMAL}")
                        indice = 8# hago que salga del ciclo
                    indice += 1
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
             
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Solicitar cupo")
        option = input_validation_TP2.check_int()   

"""
    Hacemos corresponder el indice de la patente en cupos con el peso bruto
    *--------------------*       *---------------* 
    | peso bruto[indice] |  -->  | cupos[indice] |
    *--------------------*       *---------------* 
"""
def registro_peso_bruto(pesos: list, estado: list, cupos: list):
    print("Ingresar la patente del camión del cual desea registrar el peso")
    patente = input_validation_TP2.check_pat()
    
    cupo_es_valido, indice = input_validation_TP2.check_cupo_valido(cupos, patente)# verifico que la patente ingresada ya haya sacado su cupo    
    if cupos_es_valido:
        if estado[indice] == 'E':# si posee su cupo verifico su estado 
            if pesos[indice] == 0:
                print("Ahora ingrese el peso bruto del camión")
                pesos[indice] = input_validation_TP2.check_int()
                
                while 0 > pesos[indicec] > 52500:
                    print(f"{WARNING}Peso fuera de los límites, ingrese un número entre 0 y 52500{NORMAL}")
                    pesos[indice]= input_validation_TP2.check_int()
                print(f"{SUCCESS}Peso registrado con éxito{NORMAL}")
            else:
                print(f"{WARNING}El camión ya tiene un peso bruto asignado{NORMAL}")
        else:
            print(f"{WARNING}El estado del camión debe ser 'En proceso' para poder registrar su peso bruto{NORMAL}")
    else:
        print(f"{WARNING}El camión no tiene asignado un cupo válido{NORMAL}")
            

def registro_tara(pesos: list, estado: list, tara: list):
    print("Ingresar la patente del camión del cual desea registrar la tara")
    patente = input_validation_TP2.check_pat()
    
    cupos_es_valido, indice = input_validation_TP2.check_cupo_valido(cupos ,patente)# verifico que la patente ingresada ya haya sacado su cupo   
    if cupos_es_valido:
        if estado[indice] == 'E':#si posee su cupo verifico su estado
            if pesos[indice] != 0:# verifico que haya ingresado el peso bruto anteriormente
                if tara[indice] == 0:
                    print("Ahora ingrese la tara del camión")
                    tara[indice] = input_validation_TP2.check_int()
                    
                    while 0 < tara[indice] < pesos[indice]:
                        print(f"{WARNING}Tara fuera de los límites, ingrese un número entre 0 y el peso bruto del camión{NORMAL}")
                        tara[indice] = input_validation_TP2.check_int()     
                    print(f"{SUCCESS}Tara registrado con éxito{NORMAL}")
                else:
                    print(f"{WARNING}El camión ya tiene una tara asignada{NORMAL}")
            else:
                print(f"{WARNING}Debe registrar el peso bruto del camión antes de poder registrar su tara{NORMAL}")
        else:
            print(f"{WARNING}El estado del camión debe ser 'En proceso' para poder registrar su tara{NORMAL}")
    else:
        print(f"{WARNING}El camión no tiene asignado un cupo válido{NORMAL}")

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

def menu_reportes(Maiz,Soja):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")

    option = input_validation_TP2.check_int()
    while option != 0:
        if option == 1:
            if Maiz.camionesMaiz == Soja.camionesSoja == 0: # en caso de que no se hayan ingresado camiones aún
                print(f"{WARNING}Todavía no ingreso ningun camión{NORMAL}")
            else:
                mostrar_reporte(Maiz,Soja)
        else:
            print(f"{WARNING}Ingrese una opcion válida{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
        option = input_validation_TP2.check_int()

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
    pass      
        
def menu_recepcion(cupos, identificador,estado, productos):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation_TP2.check_int()
    while option != 0:
        if option == 1:
            cupoValido, aux = chequeo_cupo_valido(cupos)
            if cupoValido:
                if estado[aux] == 'P':
                    
                    estado[aux] = 'E'
                    print(f"{SUCCESS}El camión se encuentra en proceso de recepción, ya puede cargar los datos faltantes.{NORMAL}")
                    if productos[0] == "":
                        time.sleep(0.7)
                        print(f"{WARNING}Aún no has cargado ningun producto. No vas a poderyy")
                    ingreso_de_datos()
                elif estado[aux] == 'E':
                    print(f"{WARNING}El camion ingresado ya ha sido recepcionado (se debe aclarar aún Peso Bruto y/o tara{NORMAL}")
                else:
                    print(f"{WARNING}El camion ingresado ya ha cumplido el proceso completo de ingreso{NORMAL}")

        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(0.7)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar otro camion")
        option = input_validation_TP2.check_int()

def menu_opciones(productos):
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = input_validation_TP2.check_int()
    while option != 0:
        if 1 == option:
            abm_productos_TP2.alta(productos)
        elif 2 == option:
            abm_productos_TP2.baja(productos)
        elif option == 3:
            abm_productos_TP2.consulta(productos)
        elif option == 4:
            abm_productos_TP2.modificacion(productos)
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
        option = input_validation_TP2.check_int()

def menu_administraciones(productos):
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = input_validation_TP2.check_int()
    while option != 0:
        if option == 2:
            menu_opciones(productos)
        elif 1 == option or 2 < option < 8:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
        option = input_validation_TP2.check_int()

def menu_principal(productos: list, cupos: list, identificador: list, pesos: list, estado: list, tara: list):
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = input_validation_TP2.check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones(productos)
            elif option == 2:
                entrega_de_cupos(cupos)
            elif option == 3:
                menu_recepcion(Maiz,Soja)
            elif option == 5:
                registro_peso_bruto(pesos, estados, cupos)
            elif option == 7:
                registro_tara(pesos, estados, tara)
            elif option == 8:
                menu_reportes(Maiz,Soja)
            else:
                clear_shell()
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(1.5)
        clear_shell()
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = input_validation_TP2.check_int()