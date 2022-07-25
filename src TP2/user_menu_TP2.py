import os, time, input_validation_TP2, abm_productos_TP2
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
def entrega_de_cupos(matriz_camiones: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP2.check_int()
    
    while option != 0:
        if option == 1:
            if matriz_camiones[7][0] != "":
                print(f"{WARNING}Se han acabado los cupos por el día de hoy, vuelva mañana. Saludos.{NORMAL}")
            else:
                indice = 0
                print("Ingrese la patente del camión para el que desea hacer cupo")
                patente_ingresada = input_validation_TP2.check_pat()
                
                for camion in matriz_camiones:
                    if patente_ingresada in camion:
                        print(f"{WARNING}La patente ya se ingreso el día de hoy.{NORMAL}")
                        patente_ingresada = input_validation_TP2.check_pat()
                
                while indice < len(matriz_camiones):# busco el primer espacio en blanco dentro de cupos
                    if matriz_camiones[indice][0] == "":
                        matriz_camiones[indice][0] = patente_ingresada
                        estado[indice] = 'P'
                        print(f"{SUCCESS}Se ha otorgado el cupo con éxito{NORMAL}")
                        indice = 8# hago que salga del ciclo
                    indice += 1
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
             
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Solicitar cupo")
        option = input_validation_TP2.check_int()   

"""

    Hacemos corresponder el indice de la patente en cupos con el peso bruto
    *--------------------*       *---------------* 
    | peso bruto[indice] |  -->  | cupos[indice] |
    *--------------------*       *---------------* 

"""
def registro_peso_bruto(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
    option = input_validation_TP2.check_int()
    
    while option != 0:
        if option == 1:
    
    
            print("Ingresar la patente del camión del cual desea registrar el peso")
            patente = input_validation_TP2.check_pat()
            
            cupo_es_valido, indice = input_validation_TP2.check_cupo_valido(matriz_camiones, patente)# verifico que la patente ingresada ya haya sacado su cupo    
            if cupo_es_valido:
                if estado[indice] == 'E':# si posee su cupo verifico su estado 
                    if pesos[indice][0] == 0:
                        peso_ingresado = input_validation_TP2.check_float("Ahora ingrese el peso bruto del camión: ")
                        
                        while 0 > peso_ingresado or peso_ingresado > 52500:
                            print(f"{WARNING}Peso fuera de los límites, ingrese un número entre 0 y 52500{NORMAL}")
                            peso_ingresado= input_validation_TP2.check_float("Ahora ingrese el peso bruto del camión: ")
                            
                        pesos[indice][0] = peso_ingresado
                        pesos[indice][2] = indice+1 #guardo el identificador
                        print(f"{SUCCESS}Peso registrado con éxito{NORMAL}")
                    else:
                        print(f"{WARNING}El camión ya tiene un peso bruto asignado{NORMAL}")
                else:
                    print(f"{WARNING}El estado del camión debe ser 'En proceso' para poder registrar su peso bruto.\nDirijase a recepción antes de ingresar el peso bruto correspondiente{NORMAL}")
            else:
                print(f"{WARNING}El camión no tiene asignado un cupo válido{NORMAL}")
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar el peso bruto de otro camion")
        option = input_validation_TP2.check_int()    

def registro_tara(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar tara")
    option = input_validation_TP2.check_int()
    
    while option != 0:
        if option == 1:
    
            print("Ingresar la patente del camión del cual desea registrar la tara")
            patente = input_validation_TP2.check_pat()
            
            cupos_es_valido, indice = input_validation_TP2.check_cupo_valido(matriz_camiones ,patente)# verifico que la patente ingresada ya haya sacado su cupo   
            if cupos_es_valido:
                if estado[indice] == 'E':#si posee su cupo verifico su estado
                    if pesos[indice][0] != 0:# verifico que haya ingresado el peso bruto anteriormente
                        if pesos[indice][1] == 0:
                            tara_ingresada = input_validation_TP2.check_float("Ahora ingrese la tara del camión: ")
                            
                            while 0 >= tara_ingresada or tara_ingresada >= pesos[indice][0]:
                                print(f"{WARNING}Tara fuera de los límites, ingrese un número entre 0 y el peso bruto del camión {NORMAL}(",pesos[indice][0],")")
                                tara_ingresada = input_validation_TP2.check_float("Ahora ingrese la tara del camión: ")
                            
                            pesos[indice][1] = tara_ingresada   
                            estado[indice] = 'F'
                            print(f"{SUCCESS}Tara registrado con éxito{NORMAL}")
                        else:
                            print(f"{WARNING}El camión ya tiene una tara asignada{NORMAL}")
                    else:
                        print(f"{WARNING}Debe registrar el peso bruto del camión antes de poder registrar su tara{NORMAL}")
                else:
                    print(f"{WARNING}El estado del camión debe ser 'En proceso' para poder registrar su tara.\nDirijase a recepción antes de ingresar la tara correspondiente{NORMAL}")
            else:
                print(f"{WARNING}El camión no tiene asignado un cupo válido{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar la tara de otro camion")
        option = input_validation_TP2.check_int()   

def menu_reportes(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
    total_camiones = menor_arroz = menor_cebada = menor_trigo = menor_soja = menor_maiz = 0
    mayor_arroz = mayor_cebada = mayor_trigo = mayor_soja = mayor_maiz = menor_maiz = menor_trigo = menor_arroz = menor_cebada = menor_soja = 0
    mayor_maiz_pat = mayor_trigo_pat = mayor_arroz_pat = mayor_cebada_pat = mayor_soja_pat = menor_maiz_pat = menor_trigo_pat = menor_arroz_pat = menor_cebada_pat = menor_soja_pat = "No se ingresaron camiones con este producto"
    total_productos = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    aux = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    option = input_validation_TP2.check_int()
    cupos_otorgados = 0
    
    while option != 0:
        if option == 1:
            for cupo in matriz_camiones:
                if cupo[0] != "":
                    cupos_otorgados += 1
                """
                Dentro de la matriz total producto le asignamos una fila a cada producto donde vamos a cargar sus datos
                MAIZ = Fila 0
                TRIGO = Fila 1
                CEBADA = Fila 2
                ARROZ = Fila 3
                SOJA = Fila 4
                """
            for i in range(0,7):
                if estado[i] == 'F':
                    if matriz_camiones [i][1] == "MAIZ":
                        total_productos [0][0] += 1
                        total_camiones += 1
                        total_productos [0][1] += pesos[i][0]
                        total_productos [0][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [0][0] == 1 or total_productos [0][2] > mayor_maiz:
                            mayor_maiz = total_productos [0][2]
                            mayor_maiz_pat = matriz_camiones [i][0]

                        if total_productos [0][0] == 1 or total_productos [0][2] < menor_maiz:
                            menor_maiz = total_productos [0][2]
                            menor_maiz_pat = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "TRIGO":
                        total_camiones += 1
                        total_productos [1][0] += 1
                        total_productos [1][1] += pesos[i][0]
                        total_productos [1][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [1][0] == 1 or total_productos [1][2] > mayor_trigo:
                            mayor_trigo = total_productos [1][2]
                            mayor_trigo_pat = matriz_camiones [i][0]
                        if total_productos [1][0] == 1 or total_productos [1][2] < menor_trigo:
                            menor_trigo = total_productos [1][2]
                            menor_trigo_pat = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "CEBADA":
                        total_camiones += 1
                        total_productos [2][0] += 1
                        total_productos [2][1] += pesos[i][0]
                        total_productos [2][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [2][0] == 1 or total_productos [2][2] > mayor_cebada:
                            mayor_cebada = total_productos [2][2]
                            mayor_cebada_pat = matriz_camiones [i][0]
                        if total_productos [2][0] == 1 or total_productos [2][2] < menor_cebada:
                            menor_cebada = total_productos [2][2]
                            menor_cebada_pat = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "ARROZ":
                        total_camiones += 1
                        total_productos [3][0] += 1
                        total_productos [3][1] += pesos[i][0]
                        total_productos [3][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [3][0] == 1 or total_productos [3][2] > mayor_arroz:
                            mayor_arroz = total_productos [3][2]
                            mayor_arroz_pat = matriz_camiones [i][0]
                        if total_productos [3][0] == 1 or total_productos [3][2] < menor_arroz:
                            menor_arroz = total_productos [3][2]
                            menor_arroz_pat = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "SOJA":
                        total_camiones += 1
                        total_productos [4][0] += 1
                        total_productos [4][1] += pesos[i][0]
                        total_productos [4][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [4][0] == 1 or total_productos [4][2] > mayor_soja:
                            mayor_soja = pesos[i][1]
                            mayor_soja_pat = matriz_camiones [i][0]
                        if total_productos [4][0] == 1 or total_productos [4][2] < menor_soja:
                            menor_soja = total_productos [4][2]
                            menor_soja_pat = matriz_camiones [i][0]
            
            if total_productos[0][0] != 0:               
                prom_peso_neto_maiz = total_productos[0][2] / total_productos [0][0]
            else:
                prom_peso_neto_maiz = 0
            if total_productos[1][0] != 0:
                prom_peso_neto_trigo = total_productos[1][2] / total_productos [1][0]
            else:
                prom_peso_neto_trigo = 0
            if total_productos[2][0] != 0:
                prom_peso_neto_cebada = total_productos[2][2] / total_productos [2][0]
            else:
                prom_peso_neto_cebada = 0
            if total_productos[3][0] != 0:
                prom_peso_neto_arroz = total_productos[3][2] / total_productos [3][0]
            else:
                prom_peso_neto_arroz = 0
            if total_productos[4][0] != 0:
                prom_peso_neto_soja = total_productos[4][2] / total_productos [4][0]
            else:
                prom_peso_neto_soja = 0
            
            if cupos_otorgados == 0:
                print(f"{WARNING}No se han entregado cupos por lo tanto, no hay camiones ingresados{NORMAL}")
                time.sleep(0.5)
            else:
                if total_camiones == 0:
                    print("--------------------\nLa cantidad de cupos es: ",cupos_otorgados)
                    print(f"--------------------\n{WARNING}No hay camiones recibidos{NORMAL}\n--------------------")
                    time.sleep(0.5)

                else:
                    print("--------------------\nLa cantidad de cupos es: ",cupos_otorgados,"\n--------------------\nLa cantidad de camiones recibidos es: ",total_camiones,"\n--------------------\nLa cantidad de camiones de MAIZ que se ingresaron es: ",total_productos[0][0],"\n--------------------\nLa cantidad de camiones de TRIGO que se ingresaron es: ",total_productos[1][0],"\n--------------------\nLa cantidad de camiones de CEBADA que se ingresaron es: ",total_productos[2][0],"\n--------------------\nLa cantidad de camiones de ARROZ que se ingresaron es: ",total_productos[3][0],"\n--------------------\nLa cantidad de camiones de SOJA que se ingresaron es: ",total_productos[4][0])
                    input("Presione ENTER para continuar...")
                    print("--------------------\nEl peso neto total de camiones de MAIZ que se ingresaron es: ",total_productos[0][2],"\n--------------------\nEl peso neto total de camiones de TRIGO que se ingresaron es: ",total_productos[1][2],"\n--------------------\nEl peso neto total de camiones de CEBADA que se ingresaron es: ",total_productos[2][2],"\n--------------------\nEl peso neto total de camiones de ARROZ que se ingresaron es: ",total_productos[3][2],"\n--------------------\nEl peso neto total de camiones de SOJA que se ingresaron es: ",total_productos[4][2])
                    input("Presione ENTER para continuar...")
                    print("--------------------\nEl peso neto promedio de los camiones de MAIZ que se ingresaron es: ",prom_peso_neto_maiz,"\n--------------------\nEl peso neto promedio de los camiones de TRIGO que se ingresaron es: ",prom_peso_neto_trigo,"\n--------------------\nEl peso neto promedio de los camiones de CEBADA que se ingresaron es: ",prom_peso_neto_cebada,"\n--------------------\nEl peso neto promedio de los camiones de ARROZ que se ingresaron es: ",prom_peso_neto_arroz,"\n--------------------\nEl peso neto promedio de los camiones de SOJA que se ingresaron es: ",prom_peso_neto_soja)
                    input("Presione ENTER para continuar...")
                    print("--------------------\nLa patente del camion de MAIZ que mas producto descargó es: ",mayor_maiz_pat,"\n--------------------\nLa patente del camion de TRIGO que mas producto descargó es ",mayor_trigo_pat,"\n--------------------\nLa patente del camion de CEBADA que mas producto descargó es ",mayor_cebada_pat,"\n--------------------\nLa patente del camion de ARROZ que mas producto descargó es ",mayor_arroz_pat,"\n--------------------\nLa patente del camion de SOJA que mas producto descargó es ",mayor_soja_pat)
                    input("Presione ENTER para continuar...")
                    print("--------------------\nLa patente del camion de MAIZ que menos producto descargó es: ",menor_maiz_pat,"\n--------------------\nLa patente del camion de TRIGO que menos producto descargó es ",menor_trigo_pat,"\n--------------------\nLa patente del camion de CEBADA que menos producto descargó es ",menor_cebada_pat,"\n--------------------\nLa patente del camion de ARROZ que menos producto descargó es ",menor_arroz_pat,"\n--------------------\nLa patente del camion de SOJA que menos producto descargó es ",menor_soja_pat,"\n--------------------")
                    input("Presione ENTER para continuar...")
            i=0
            co=1
            while i < total_camiones:
                aux[i][0] = matriz_camiones[i][0]
                aux[i][1] = matriz_camiones[i][1]
                aux[i][2] = pesos[i][0]-pesos[i][1]
                i+=1
            while co < total_camiones:
                if aux[co][2] > aux[co - 1][2]:
                    aux2 = aux[co - 1][2]
                    aux[co - 1][2] = aux [co][2]
                    aux[co][2] = aux2
                    
                    aux2 = aux[co - 1][0]
                    aux[co - 1][0] = aux [co][0]
                    aux[co][0] = aux2
                    
                    aux2 = aux[co - 1][1]
                    aux[co - 1][1] = aux [co][1]
                    aux[co][1] = aux2

                    if co == 1:
                        co = co + 1
                    else:
                        co = co - 1
                else:
                    co = co + 1
                
            co=0
            print("La lista de camiones ingresados ordenada por peso neto descendente quedaria asi:")
            while co <total_camiones:
                print(co+1," - El camion de patente ",aux[co][0]," que llevaba",aux[co][2],"kilogramos de ",aux[co][1])

                co+=1
            input("Presione ENTER para continuar...")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
            time.sleep(2.5)

            clear_shell()
            print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
            option = input_validation_TP2.check_int()
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
        option = input_validation_TP2.check_int()


    
def menu_recepcion(matriz_camiones,estado,productos):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation_TP2.check_int()
    while option != 0:
        if option == 1:
            if productos[0] == "":
                print(f"{WARNING}Aún no has cargado ningun producto. No vas a poder recepcionar un camion sin antes hacerlo{NORMAL}")
            else:
                print("Ingresar la patente del camión del cual desea registrar")
                patente = input_validation_TP2.check_pat()
                cupos_es_valido, indice = input_validation_TP2.check_cupo_valido(matriz_camiones, patente)

                if cupos_es_valido:# si el camion ya posee un cupo, verifico su estado
                    if estado[indice] == 'P':
                        print("Que producto contiene el camion?")           
                        producto_ingresado = input_validation_TP2.check_producto()# le pido que ingrese el producto correspondiente al camión ingresado
                        while producto_ingresado not in productos:# si el producto ya fue ingresado hago que ingrese otro hasta que no se encuentre en la lista
                            print(f"{WARNING}El producto no ha sido ingresado anteriormente.{NORMAL}")
                            producto_ingresado = input_validation_TP2.check_producto()
                        
                        estado[indice] = 'E'# modifico su estado 
                        matriz_camiones[indice][0] = patente
                        matriz_camiones[indice][2] = indice + 1#guardo el identificador
                        matriz_camiones[indice][1] = producto_ingresado
                        #Guardo la patente y el producto, el identificador ya lo tengo
                        print(f"{SUCCESS}El camión se encuentra en proceso de recepción, ya puede cargar los datos faltantes.{NORMAL}")
                    elif estado[indice] == 'E':
                        print(f"{WARNING}El camion ingresado ya ha sido recepcionado (se debe aclarar aún Peso Bruto y/o tara{NORMAL}")
                    else:
                        print(f"{WARNING}El camion ingresado ya ha cumplido el proceso completo de ingreso{NORMAL}")
                else:
                    print(f"{WARNING}El camión no tiene asignado un cupo válido{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
        option = input_validation_TP2.check_int()


def menu_opciones(productos: list):
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
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
        option = input_validation_TP2.check_int()

def menu_administraciones(productos: list):
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
        time.sleep(2.5)
        clear_shell()
        print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
        option = input_validation_TP2.check_int()

def menu_principal(productos: list, matriz_camiones: list, pesos: list, estado: list):
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
                entrega_de_cupos(matriz_camiones, estado)
            elif option == 3:
                menu_recepcion(matriz_camiones, estado, productos)
            elif option == 5:
                registro_peso_bruto(matriz_camiones, pesos, estado)
            elif option == 7:
                registro_tara(matriz_camiones, pesos, estado)
            elif option == 8:
                menu_reportes(matriz_camiones,pesos,estado)
            else:
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = input_validation_TP2.check_int()