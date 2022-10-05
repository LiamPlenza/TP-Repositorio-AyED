import os, time, pickle, io, os.path, datetime
import input_validation_TP3, archivos_TP3, main_TP3
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
def entrega_de_cupos():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP3.check_int()
    bandera = 0
    while option != 0:
        if option == 1:
            if input_validation_TP3.check_producto:
                print(f"{WARNING}No hay productos activos.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                if os.path.exists("OPERACIONES.dat"):
                    archivo_logico = open("OPERACIONES.dat", "r+b")
                    longitud_archivo = os.path.getsize("OPERACIONES.dat")
                    patente_ingresada = input_validation_TP3.check_pat()
                    fecha_ingresada = input_validation_TP3.check_fecha(print("Ingrese la fecha deseada para el cupo"))
                    
                    while pickle.tell(archivo_logico) < longitud_archivo:
                        registro = pickle.load(archivo_logico)
                        if patente_ingresada == registro.patente and fecha_ingresada == registro.fecha:
                            print(f"{WARNING}Cupo ya otorgado.{NORMAL}")
                            bandera = 1
                    if bandera == 0:
                        producto_ingresado = input_validation_TP3.check_producto_valido() 
                        registro.patente = patente_ingresada
                        registro.fecha = fecha_ingresada
                        registro.estado = "P"
                        registro.codprod = producto_ingresado
                        registro.pesobruto = 0
                        registro.tara = 0
                else:
                    archivo_logico = open("OPERACIONES.dat", "w+b")
                    registro.patente = input_validation_TP3.check_pat()
                    registro.fecha = input_validation_TP3.check_fecha()
                    registro.codprod = input_validation_TP3.check_producto_valido() 
                    registro.estado = "P"
                    registro.pesobruto = 0
                    registro.tara = 0
                    pickle.dump(registro,"OPERACIONES.dat")
                pickle.flush()
                pickle.close(archivo_logico)

        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
             
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Solicitar cupo")
        option = input_validation_TP3.check_int()   

def registrar_calidad():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:
                archivo_logico = open ("OPERACIONES.dat")
                archivo_logico_r = open("RUBROS.dat", "r+b")
                archivo_logico_p= open("PRODUCTOS.dat", "r+b")
                archivo_logico_rxp = open ("RUBROS-X-PRODUCTO.dat")
                registro = main_TP3.Operaciones()
                registro_r = main_TP3.Rubros()
                registro_p = main_TP3.Productos()
                registro_rxp = main_TP3.RubrosxProducto
                longitud_archivo = os.path.getsize("OPERACIONES.dat")
                longitud_archivo_p = os.path.getsize("PRODUCTOS.dat")
                longitud_archivo_r = os.path.getsize("RUBROS.dat")
                longitud_archivo_rxp = os.path.getsize("RUBROS-X-PRODUCTO.dat")

                bandera = False
                print("Ingresar la patente del camión del cual desea ingresar")
                patente_ingresada = input_validation_TP3.check_pat()
                while pickle.tell(archivo_logico) < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    
                    if patente_ingresada == registro.patente and registro.estado == "A": #Chequeo si el estado del camion es el correcto
                        bandera = True
                        rubros = []
                        while pickle.tell(archivo_logico_rxp) < longitud_archivo_rxp:
                            registro_rxp = pickle.load("RUBROS-X-PRODUCTO.dat") 
                            if registro.codprod == registro_rxp.codprod: #Busco el producto del camion dentro del archivo rubro por producto
                               rubros.append(registro_rxp.codrub)
                        if len(rubros) > 0: 
                            while pickle.tell(archivo_logico_p) < longitud_archivo_p:
                                registro_p = pickle.load(archivo_logico_p)
                                if registro_p.codprod == registro_rxp.codprod:
                                    print(f"El camion contiene {registro_p.nomprod} ingrese la calidad correspondiente a los siguientes rubros:")
                                r=0
                                g=0
                                while g < len(rubros):
                                    while pickle.tell(archivo_logico_r) < longitud_archivo_r:
                                        registro_r = pickle.load(archivo_logico_r)
                                        if registro_r.codrub == rubros[g]:
                                            valor = int(input(f"Ingrese el valor para el rubro {registro_r.nomrub}:"))
                                            archivo_logico_rxp.seek(io.SEEK_SET) # me muevo al inicio del archivo
                                            while pickle.tell(archivo_logico_rxp) < longitud_archivo_rxp:
                                                registro_rxp = pickle.load("RUBROS-X-PRODUCTO.dat")
                                                if registro_rxp == rubros[g] and registro_p.codprod == registro_rxp.codprod:
                                                    if valor < registro_rxp.vmin or valor > registro_rxp.vmax:
                                                        r +=1
                                    if r == 2:
                                        registro.estado = "R"
                                    g += 1                            
                                if registro.estado != "R":
                                    registro.estado = "A" #Aceptado =  Con Calidad
                        else:
                            print(f"{WARNING}No hay Rubros ingresados para el producto del camion en cuestion, por lo tanto, no se puede realizar el control de calidad.{NORMAL}")
                if not bandera:
                    print(f"{WARNING}El camion no cumple con los requisitos para realizar esta acción{NORMAL}")    
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar el peso bruto de otro camion")
        option = input_validation_TP3.check_int()    

def registro_peso_bruto(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        if option == 1:
    
    
            print("Ingresar la patente del camión del cual desea registrar el peso")
            patente = input_validation_TP3.check_pat()
            
            cupo_es_valido, indice = input_validation_TP3.check_cupo_valido(matriz_camiones, patente)# verifico que la patente ingresada ya haya sacado su cupo    
            if cupo_es_valido:
                if estado[indice] == 'E':# si posee su cupo verifico su estado 
                    if pesos[indice][0] == 0:
                        peso_ingresado = input_validation_TP3.check_float("Ahora ingrese el peso bruto del camión: ")
                        
                        while 0 > peso_ingresado or peso_ingresado > 52500:
                            print(f"{WARNING}Peso fuera de los límites, ingrese un número entre 0 y 52500{NORMAL}")
                            peso_ingresado= input_validation_TP3.check_float("Ahora ingrese el peso bruto del camión: ")
                            
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
        option = input_validation_TP3.check_int()    

def registro_tara(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar tara")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        if option == 1:
    
            print("Ingresar la patente del camión del cual desea registrar la tara")
            patente = input_validation_TP3.check_pat()
            
            cupos_es_valido, indice = input_validation_TP3.check_cupo_valido(matriz_camiones ,patente)# verifico que la patente ingresada ya haya sacado su cupo   
            if cupos_es_valido:
                if estado[indice] == 'E':#si posee su cupo verifico su estado
                    if pesos[indice][0] != 0:# verifico que haya ingresado el peso bruto anteriormente
                        if pesos[indice][1] == 0:
                            tara_ingresada = input_validation_TP3.check_float("Ahora ingrese la tara del camión: ")
                            
                            while 0 >= tara_ingresada or tara_ingresada >= pesos[indice][0]:
                                print(f"{WARNING}Tara fuera de los límites, ingrese un número entre 0 y el peso bruto del camión {NORMAL}(",pesos[indice][0],")")
                                tara_ingresada = input_validation_TP3.check_float("Ahora ingrese la tara del camión: ")
                            
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
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   

        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar la tara de otro camion")
        option = input_validation_TP3.check_int()   

def menu_reportes(matriz_camiones: list, pesos: list, estado: list):
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
    total_camiones = 0
    may_men_pat = ["No se ingresaron camiones con este producto"]*2,["No se ingresaron camiones con este producto"]*2,["No se ingresaron camiones con este producto"]*2,["No se ingresaron camiones con este producto"]*2,["No se ingresaron camiones con este producto"]*2
    may_men = [0]*2,[0]*2,[0]*2,[0]*2,[0]*2
    total_productos = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    prom_peso_neto = [0]*5
    aux = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    option = input_validation_TP3.check_int()
    cupos_otorgados = 0
    
    while option != 0:
        if option == 1:
            for i in range(0,7):
                if matriz_camiones[i][0] != "":
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
                        if total_productos [0][0] == 1 or total_productos [0][2] > may_men[0][0]:
                            may_men[0][0] = total_productos [0][2]
                            may_men_pat[0][0] = matriz_camiones [i][0]

                        if total_productos [0][0] == 1 or total_productos [0][2] < may_men[0][1]:
                            may_men[0][1] = total_productos [0][2]
                            may_men_pat[0][1] = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "TRIGO":
                        total_camiones += 1
                        total_productos [1][0] += 1
                        total_productos [1][1] += pesos[i][0]
                        total_productos [1][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [1][0] == 1 or total_productos [1][2] > may_men[1][0]:
                            may_men[1][0] = total_productos [1][2]
                            may_men_pat[1][0] = matriz_camiones [i][0]
                        if total_productos [1][0] == 1 or total_productos [1][2] < may_men[1][1]:
                            may_men[1][1] = total_productos [1][2]
                            may_men_pat[1][1] = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "CEBADA":
                        total_camiones += 1
                        total_productos [2][0] += 1
                        total_productos [2][1] += pesos[i][0]
                        total_productos [2][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [2][0] == 1 or total_productos [2][2] > may_men[2][0]:
                            may_men[2][0] = total_productos [2][2]
                            may_men_pat[2][0] = matriz_camiones [i][0]
                        if total_productos [2][0] == 1 or total_productos [2][2] < may_men[2][1]:
                            may_men[2][1] = total_productos [2][2]
                            may_men_pat[2][1] = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "ARROZ":
                        total_camiones += 1
                        total_productos [3][0] += 1
                        total_productos [3][1] += pesos[i][0]
                        total_productos [3][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [3][0] == 1 or total_productos [3][2] > may_men[3][0]:
                            may_men[3][0] = total_productos [3][2]
                            may_men_pat[3][0] = matriz_camiones [i][0]
                        if total_productos [3][0] == 1 or total_productos [3][2] < may_men[3][1]:
                            may_men[3][1] = total_productos [3][2]
                            may_men_pat[3][1] = matriz_camiones [i][0]
                            
                    if matriz_camiones [i][1] == "SOJA":
                        total_camiones += 1
                        total_productos [4][0] += 1
                        total_productos [4][1] += pesos[i][0]
                        total_productos [4][2] += pesos[i][0] - pesos[i][1]
                        if total_productos [4][0] == 1 or total_productos [4][2] > may_men[4][0]:
                            may_men[4][0] = pesos[i][1]
                            may_men_pat[4][0] = matriz_camiones [i][0]
                        if total_productos [4][0] == 1 or total_productos [4][2] < may_men[4][1]:
                            may_men[4][1] = total_productos [4][2]
                            may_men_pat[4][1] = matriz_camiones [i][0]
            
            if total_productos[0][0] != 0:               
                prom_peso_neto[0] = total_productos[0][2] / total_productos [0][0]
            else:
                prom_peso_neto[0] = 0
            if total_productos[1][0] != 0:
                prom_peso_neto[1] = total_productos[1][2] / total_productos [1][0]
            else:
                prom_peso_neto[1] = 0
            if total_productos[2][0] != 0:
                prom_peso_neto[2] = total_productos[2][2] / total_productos [2][0]
            else:
                prom_peso_neto[2] = 0
            if total_productos[3][0] != 0:
                prom_peso_neto[3] = total_productos[3][2] / total_productos [3][0]
            else:
                prom_peso_neto[3] = 0
            if total_productos[4][0] != 0:
                prom_peso_neto[4] = total_productos[4][2] / total_productos [4][0]
            else:
                prom_peso_neto[4] = 0
            
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
                    print("--------------------\nEl peso neto promedio de los camiones de MAIZ que se ingresaron es: ",prom_peso_neto[0],"\n--------------------\nEl peso neto promedio de los camiones de TRIGO que se ingresaron es: ",prom_peso_neto[1],"\n--------------------\nEl peso neto promedio de los camiones de CEBADA que se ingresaron es: ",prom_peso_neto[2],"\n--------------------\nEl peso neto promedio de los camiones de ARROZ que se ingresaron es: ",prom_peso_neto[3],"\n--------------------\nEl peso neto promedio de los camiones de SOJA que se ingresaron es: ",prom_peso_neto[4])
                    input("Presione ENTER para continuar...")
                    print("--------------------\nLa patente del camion de MAIZ que mas producto descargó es: ",may_men_pat[0][0],"\n--------------------\nLa patente del camion de TRIGO que mas producto descargó es ",may_men_pat[1][0],"\n--------------------\nLa patente del camion de CEBADA que mas producto descargó es ",may_men_pat[2][0],"\n--------------------\nLa patente del camion de ARROZ que mas producto descargó es ",may_men_pat[3][0],"\n--------------------\nLa patente del camion de SOJA que mas producto descargó es ",may_men_pat[4][0])
                    input("Presione ENTER para continuar...")
                    print("--------------------\nLa patente del camion de MAIZ que menos producto descargó es: ",may_men_pat[0][1],"\n--------------------\nLa patente del camion de TRIGO que menos producto descargó es ",may_men_pat[1][1],"\n--------------------\nLa patente del camion de CEBADA que menos producto descargó es ",may_men_pat[2][1],"\n--------------------\nLa patente del camion de ARROZ que menos producto descargó es ",may_men_pat[3][1],"\n--------------------\nLa patente del camion de SOJA que menos producto descargó es ",may_men_pat[4][1],"\n--------------------")
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
            option = input_validation_TP3.check_int()
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Mostrar el reporte actual")
        option = input_validation_TP3.check_int()
    
def menu_recepcion():
    clear_shell()
    bandera = False
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:
                archivo_logico = open ("OPERACIONES.dat")
                registro = main_TP3.Operaciones()
                longitud_archivo = os.path.getsize("OPERACIONES.dat")

                print("Ingresar la patente del camión del cual desea ingresar")
                patente_ingresada = input_validation_TP3.check_pat()
                while pickle.tell(archivo_logico) < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente and registro.fecha == datetime.now() and registro.estado == "P":
                        registro.estado = "A"
                        pickle.dump(registro,archivo_logico)
                        pickle.flush()
                        bandera = True
                if bandera:
                    print(f"{SUCCESS}El camion ha sido ingresado con exito{NORMAL}")
                else:
                    print(f"{WARNING}El camión no ha podido ser recibido. Chequee los datos del mismo{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
        option = input_validation_TP3.check_int()

def menu_opciones(menu: str):
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        if 1 == option:
            archivos_TP3.alta(menu)
        elif 2 == option and menu == "productos":
            archivos_TP3.baja()
        elif option == 3 and menu == "productos":
            archivos_TP3.consulta()
        elif option == 4 and menu == "productos":
            archivos_TP3.modificacion()
        elif option not in [x for x in range(5)]:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
        option = input_validation_TP3.check_int()

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        if option == 2:
            menu_opciones("productos")
        elif option == 3:
            menu_opciones("rubros")
        elif option == 4:
            menu_opciones("rubros por productos")
        elif option == 5:
            menu_opciones("silos")
        elif option not in [x for x in range(8)]:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
        option = input_validation_TP3.check_int()

def menu_principal():
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
    option = input_validation_TP3.check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 2:
                pass
                #entrega_de_cupos()
            elif option == 3:
                pass
                #menu_recepcion()
            elif option == 4:
                pass
                #registrar_calidad()
            elif option == 5:
                pass
                #registro_peso_bruto()
            elif option == 7:
                pass
                #registro_tara()
            elif option == 8:
                pass
                #menu_reportes()
            else:
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = input_validation_TP3.check_int()