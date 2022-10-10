import os, time, pickle, io, os.path
from datetime import datetime

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

def hoy():
    return str(datetime.today().day)+"/"+str(datetime.today().month)+"/"+str(datetime.today().year)

# TERMINADO
def entrega_de_cupos(): 
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP3.check_int()
    while option != 0:
        cupo_ya_otorgado = False
        if option == 1:
            if not (input_validation_TP3.check_producto() and os.path.exists("SILOS.dat")):
                print(f"{WARNING}No hay productos activos o el registro de silos se encuentra vacio.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                if os.path.exists("OPERACIONES.dat"): # veo si el archivo existe para ver como lo abro
                    archivo_logico = open("OPERACIONES.dat", "r+b")
                    longitud_archivo = os.path.getsize("OPERACIONES.dat")
                    
                    patente_ingresada = input_validation_TP3.check_pat().ljust(7)
                    
                    print("Ingrese la fecha deseada para el cupo:")
                    fecha_ingresada = input_validation_TP3.check_fecha().ljust(8)
                    
                    #archivo_logico.seek(io.SEEK_SET) # linea no necesaria (probar)
                    while archivo_logico.tell() < longitud_archivo:
                        registro = pickle.load(archivo_logico) # verifico si ya tengo el cupo entregado para ese camion y ese dia
                        if patente_ingresada == registro.patente and fecha_ingresada == registro.fecha:
                            print(f"{WARNING}Cupo ya otorgado.{NORMAL}")
                            cupo_ya_otorgado = True
                            
                    if not cupo_ya_otorgado:
                        registro.patente = patente_ingresada
                        registro.fecha = fecha_ingresada   
                else:
                    archivo_logico = open("OPERACIONES.dat", "w+b")
                    registro.patente = input_validation_TP3.check_pat().ljust(7)
                    print("Ingrese la fecha deseada para el cupo:")
                    registro.fecha = input_validation_TP3.check_fecha().ljust(8)

                if not cupo_ya_otorgado:
                    clear_shell()
                    print(f"Patente ingresada: {registro.patente}, fecha ingresada: {registro.fecha}")
                    registro.codprod = input_validation_TP3.check_producto_valido() # verifico que se elija un producto activado y existente para el camion
                    registro.estado = "P"
                    registro.pesobruto = 0
                    registro.tara = 0
                    pickle.dump(registro,archivo_logico)
                    print(f"{SUCCESS}El cupo ha sido otorgado con éxito.{NORMAL}")
                    
                archivo_logico.flush()
                archivo_logico.close()
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
             
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Solicitar cupo")
        option = input_validation_TP3.check_int()  

# TERMINADO
def menu_recepcion():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        razon = 0 # para dar un mensaje mas descriptivo del error
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:   
                registro = main_TP3.Operaciones()
                archivo_logico = open("OPERACIONES.dat", "r+b")
                longitud_archivo = os.path.getsize("OPERACIONES.dat")

                print("Ingresar la patente del camión del cual desea ingresar")
                patente_ingresada = input_validation_TP3.check_pat().ljust(7)
                
                while archivo_logico.tell() < longitud_archivo:
                    posicion = archivo_logico.tell()
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente:
                        razon = 1 
                        fecha_de_entrega = registro.fecha
                        if registro.fecha == hoy(): # probar == hoy()
                            razon = 2
                            if registro.estado == "P":
                                razon = 3
                                posicion_final = posicion

                if razon == 3:
                    archivo_logico.seek(posicion_final) # me muevo al registro que tengo que tengo que actualizar, cada registro pesa 134 el tema que cuando hago el load ya avanza el registro
                    registro = pickle.load(archivo_logico)
                    registro.estado = "A" # no hace falta hacer el load primero y después nuevamente el seek para hacer el dump en el lugar correspondiente?
                    archivo_logico.seek(posicion_final) # me muevo otra vez porque el load avanza solo
                    pickle.dump(registro,archivo_logico)
                    print(f"{SUCCESS}El camion ha sido ingresado con exito{NORMAL}")
                elif razon == 0:
                    print(f"{WARNING}La patente ingresada no coincide con un camion registrado{NORMAL}")
                elif razon == 1:
                    print(f"{WARNING}El camion tiene un cupo asignado para un dia que no es hoy. Fecha de entrega: {fecha_de_entrega}{NORMAL}")
                else:
                    print(f"{WARNING}Para poder recepcionar un camion, el mismo debe tener estado Pendiente{NORMAL}") 
                           
                archivo_logico.flush()
                archivo_logico.close()
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
        option = input_validation_TP3.check_int() 

def registrar_calidad():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar calidad")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        if option == 1: # verifico que existen todos los archivos necesarios
            if not (os.path.exists("OPERACIONES.dat") and os.path.exists("RUBROS.dat") and os.path.exists("PRODUCTOS.dat") and os.path.exists("RUBROS-X-PRODUCTO.dat")):
                print(f"{WARNING}No se cumplen todos los requerimientos para llevar a cabo este registro.{NORMAL}")
            else:# abro todos los archivos necesarios
                archivo_logico_operaciones = open ("OPERACIONES.dat", "r+b")
                archivo_logico_rubros = open("RUBROS.dat", "r+b")
                archivo_logico_productos= open("PRODUCTOS.dat", "r+b")
                archivo_logico_rxp = open ("RUBROS-X-PRODUCTO.dat", "r+b")
                # inicio todos los objetos
                registro_operaciones = main_TP3.Operaciones()
                registro_rubros = main_TP3.Rubros()
                registro_productos = main_TP3.Productos()
                registro_rxp = main_TP3.RubrosxProducto
                # guardo la longitud de los archivos
                longitud_archivo_operaciones = os.path.getsize("OPERACIONES.dat")
                longitud_archivo_productos = os.path.getsize("PRODUCTOS.dat")
                longitud_archivo_rubros = os.path.getsize("RUBROS.dat")
                longitud_archivo_rxp = os.path.getsize("RUBROS-X-PRODUCTO.dat")

                bandera = False
                print("Ingresar la patente del camión del cual desea ingresar")
                patente_ingresada = input_validation_TP3.check_pat()
                while archivo_logico_operaciones.tell() < longitud_archivo_operaciones:
                    registro_operaciones = pickle.load(archivo_logico_operaciones)
                    
                    if patente_ingresada == registro_operaciones.patente and registro_operaciones.estado == "A": #Chequeo si el estado del camion es el correcto
                        bandera = True
                        rubros = []
                        
                        while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                            registro_rxp = pickle.load(archivo_logico_rxp) 
                            if registro_operaciones.codprod == registro_rxp.codprod: #Busco el producto del camion dentro del archivo rubro por producto
                               rubros.append(registro_rxp.codrub)
                               
                        if len(rubros) != 0: 
                            while archivo_logico_productos.tell() < longitud_archivo_productos:
                                registro_productos = pickle.load(archivo_logico_productos)
                                print(f"El camion contiene {registro_productos.nomprod.strip()} \nIngrese la calidad correspondiente a los siguientes rubros:")
                                r=0
                                g=0
                                #for codrubro in rubros:
                                #    while archivo_logico_rubros.tell() < longitud_archivo_rubros:
                                #        registro_rubros = pickle.load(archivo_logico_rubros)
                                #        if registro_rubros.codrub == codrubro:
                                #            pass
                                        
                                while g < len(rubros):
                                    x = True
                                    while archivo_logico_rubros.tell() < longitud_archivo_rubros:
                                        registro_rubros = pickle.load(archivo_logico_rubros)
                                        if registro_rubros.codrub == rubros[g]:
                                            while x == True:
                                                valor = input_validation_TP3.check_int(f"{registro_rubros.nomrub.strip()}:") 
                                                if valor <= 100 and valor >= 0 :
                                                    archivo_logico_rxp.seek(io.SEEK_SET) # me muevo al inicio del archivo
                                                    while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                                                        registro_rxp = pickle.load(archivo_logico_rxp)
                                                        if registro_rxp == rubros[g] and registro_productos.codprod == registro_rxp.codprod:
                                                            if valor < registro_rxp.vmin or valor > registro_rxp.vmax:
                                                                r +=1
                                                    x = False
                                                else:
                                                    print("El valor ingresado debe estar entre 0 y 100, ingrese nuevamente.")
                                    if r == 2:
                                        registro_operaciones.estado = "R"
                                    g += 1                            
                                if registro_operaciones.estado != "R":
                                    registro_operaciones.estado = "A" #Aceptado =  Con Calidad
                        else:
                            print(f"{WARNING}No hay Rubros ingresados para el producto del camion en cuestion, por lo tanto, no se puede realizar el control de calidad.{NORMAL}")
                archivo_logico_operaciones.flush()
                archivo_logico_productos.flush()
                archivo_logico_rubros.flush()
                archivo_logico_rxp.flush()
                archivo_logico_productos.close()
                archivo_logico_rubros.close()
                archivo_logico_rxp.close()
                archivo_logico_operaciones.close()
                if not bandera:
                    print(f"{WARNING}El camion no cumple con los requisitos para realizar esta acción{NORMAL}")    
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar el peso bruto de otro camion")
        option = input_validation_TP3.check_int()    

# TERMINADO
def registro_peso_bruto():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
    option = input_validation_TP3.check_int()
    #bandera = False
    while option != 0:
        razon = 0 # para dar indicar porque no se puede registrar el peso bruto
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                archivo_logico = open("OPERACIONES.dat", "r+b")
                longitud_archivo = os.path.getsize("OPERACIONES.dat")
                
                patente_ingresada = input_validation_TP3.check_pat()
                
                while archivo_logico.tell() < longitud_archivo:
                    posicion = archivo_logico.tell()
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente: # verifico que la pantente haya sido ingresada
                        razon = 1
                        if registro.estado == "A": # verifico el estado
                            razon = 2
                            #bandera = True
                            peso_bruto_ingresado = input_validation_TP3.check_int("Ingrese el peso bruto del camion: ")
                            while peso_bruto_ingresado < 0 or peso_bruto_ingresado > 52500:
                                peso_bruto_ingresado = input_validation_TP3.check_int("Ingrese el peso bruto del camion (tiene que ser un numero entre 0 y 52500): ")
                            posicion_final = posicion # guardo la posicion del registro a modificar
                            
                    #else:
                            #bandera = False
                    #if bandera == False:
                if razon == 0:
                    print(f"{WARNING}La patente ingresada no coincide con una registrada{NORMAL}")
                elif razon == 1: 
                    print(f"{WARNING}El estado de del camion debe ser Con Calidad. Pase por recepcion previamente{NORMAL}")
                else: # 134 es el peso de un unico registro
                    archivo_logico.seek(posicion_final) # me paro en el inicio del registro a modificar (no te enojes liam por el -134 es que sino no anda)
                    registro = pickle.load(archivo_logico)
                    registro.estado = "B"
                    registro.pesobruto = peso_bruto_ingresado
                    archivo_logico.seek(posicion_final) # me muevo otra vez al inicio del registro porque el load se mueve solo
                    pickle.dump(registro,archivo_logico)
                    print(f"{SUCCESS}Peso bruto registrado con exito{NORMAL}")

                archivo_logico.flush()
                archivo_logico.close()
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
        option = input_validation_TP3.check_int()
    
def registro_tara():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar tara")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        razon = 0
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            elif not os.path.exists("SILOS.dat"):
                print(f"{WARNING}Aún no hay silos registradas.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                archivo_logico = open("OPERACIONES.dat", "r+b")
                longitud_archivo = os.path.getsize("OPERACIONES.dat")
                
                patente_ingresada = input_validation_TP3.check_pat()
                
                while archivo_logico.tell() < longitud_archivo:
                    posicion = archivo_logico.tell()
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente:
                        razon == 1
                        if registro.estado == "B":
                            razon = 2
                            tara_ingresada = input_validation_TP3.check_int(f"Ingrese la tara del camion. Esta debe ser menor a {registro.pesobruto}: ")
                            while tara_ingresada > registro.pesobruto:
                                tara_ingresada = input_validation_TP3.check_int(f"La tara debe ser menor a {registro.pesobruto}. Pruebe nuevamente: ")
                            posicion_final = posicion
                
                if razon == 0:
                    print(f"{WARNING}La patente ingresada no coincide con una registrada{NORMAL}")
                elif razon == 1:
                    print(f"{WARNING}El estado de del camion debe ser 'Bruto'. Pase por 'Registrar Peso Bruto' previamente{NORMAL}")
                else:     
                    archivo_logico.seek(posicion_final) # me paro en el inicio del registro a modificar (no te enojes liam por el -134 es que sino no anda)
                    registro = pickle.load(archivo_logico)
                    registro.estado = "F"
                    registro.tara = tara_ingresada
                    
                    # guardo el stock en el silo
                    registro_silo = main_TP3.Silos()
                    archivo_logico_silos = open("SILOS.dat", "r+b")
                    longitud_archivo_silos = os.path.getsize("SILOS.dat")
                    while archivo_logico_silos.tell() < longitud_archivo_silos:
                        posicion_silo = archivo_logico_silos.tell()
                        registro_silo = pickle.load(archivo_logico_silos)
                        if registro_silo.codprod == registro.codprod:
                            posicion_silo_final = posicion_silo
                            
                    archivo_logico_silos.seek(posicion_silo_final)
                    registro_silo =  pickle.load(archivo_logico_silos)
                    registro_silo.stock = registro.pesobruto - registro.tara
                    
                    archivo_logico_silos.seek(posicion_silo_final)
                    archivo_logico.seek(posicion_final) # me muevo otra vez al inicio del registro porque el load se mueve solo
                    pickle.dump(registro,archivo_logico)
                    pickle.dump(registro_silo, archivo_logico_silos)
                    
                    archivo_logico_silos.flush()
                    archivo_logico_silos.close()
                    
                    print(f"{SUCCESS}Tara registrada con exito{NORMAL}")
                
                archivo_logico.flush()
                archivo_logico.close()
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
        
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar la tara de otro camion")
        option = input_validation_TP3.check_int()   
 

def menu_reportes():
    pass
          
# TERMINADO
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
            input("Precione enter para continuar... ")
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

# TERMINADO
def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        if option == 2:
            if os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Ya se han registrado camiones. Ya no es posible modificar los productos{NORMAL}")
            else:
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

# TERMINADO
def menu_principal():
    clear_shell()

    print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n9 - Listado de Silos y Rechazos \n0 - Salir del programa \n")
    option = input_validation_TP3.check_int()
    while option != 0:
        if option < 1 or option > 8:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        else:
            if option == 1:
                menu_administraciones()
            elif option == 2:
                entrega_de_cupos()
            elif option == 3:
                menu_recepcion()
            elif option == 4:
                registrar_calidad()
            elif option == 5:
                registro_peso_bruto()
            elif option == 7:
                registro_tara()
            elif option == 8:
                menu_reportes()
            else:
                print(f"{WARNING}Esta funcionalidad está en construcción{NORMAL}")
        time.sleep(2.5)
        clear_shell()
        print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")
        option = input_validation_TP3.check_int()