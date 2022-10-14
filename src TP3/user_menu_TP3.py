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
            if input_validation_TP3.check_producto() and os.path.exists("SILOS.dat"):
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
                print(f"{WARNING}No hay productos activos o el registro de silos se encuentra vacio.{NORMAL}")
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
    razon = 0
    while option != 0:
        if option == 1: # verifico que existen todos los archivos necesarios
            if not (os.path.exists("OPERACIONES.dat")):
                print(f"{WARNING}Deben haber camiones ingresados para realizar esta tarea.{NORMAL}")
            else:    
                if not (os.path.exists("PRODUCTOS.dat")):
                    print(f"{WARNING}Deben haber Productos ingresados para realizar esta tarea.{NORMAL}")
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
                    print("Ingresar la patente del camión del cual desea ingresar")
                    patente_ingresada = input_validation_TP3.check_pat().ljust(7)
                    while archivo_logico_operaciones.tell() < longitud_archivo_operaciones:
                        pos = archivo_logico_operaciones.tell()
                        registro_operaciones = pickle.load(archivo_logico_operaciones)
                        if patente_ingresada == registro_operaciones.patente:
                            razon = 1
                            if registro_operaciones.estado == "A": #Chequeo si el estado del camion es el correcto
                                razon = 2
                                rubros = []
                                producto_camion = registro_operaciones.codprod
                                posicion_final = pos

                                while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                                    registro_rxp = pickle.load(archivo_logico_rxp) 
                                    if registro_operaciones.codprod == registro_rxp.codprod: #Busco el producto del camion dentro del archivo rubro por producto
                                        rubros.append(registro_rxp.codrub)
                                    
                                if len(rubros) != 0: 
                                    while archivo_logico_productos.tell() < longitud_archivo_productos:
                                        registro_productos = pickle.load(archivo_logico_productos)
                                        if registro_productos.codprod == producto_camion:
                                            print(f"El camion contiene {registro_productos.nomprod.strip()} \nIngrese la calidad correspondiente a los siguientes rubros:")
                                            r=0
                                            g=0
                                            #for codrubro in rubros:
                                            #    while archivo_logico_rubros.tell() < longitud_archivo_rubros:
                                            #        registro_rubros = pickle.load(archivo_logico_rubros)
                                            #        if registro_rubros.codrub == codrubro:
                                            #            pass
                                                    
                                            while g < len(rubros):
                                                archivo_logico_rubros.seek(io.SEEK_SET)
                                                while archivo_logico_rubros.tell() < longitud_archivo_rubros:
                                                    registro_rubros = pickle.load(archivo_logico_rubros)
                                                    if registro_rubros.codrub == rubros[g]:
                                                        valor = input_validation_TP3.check_int(f"{registro_rubros.nomrub.strip()}:") 
                                                        while valor > 100 or valor < 0 :
                                                            valor = input_validation_TP3.check_int("Ingrese un valor entre 0 y 100:") 
                                                        archivo_logico_rxp.seek(io.SEEK_SET) # me muevo al inicio del archivo
                                                        while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                                                            registro_rxp = pickle.load(archivo_logico_rxp)
                                                            if registro_rxp.codrub == rubros[g] and registro_productos.codprod == registro_rxp.codprod:
                                                                if valor < registro_rxp.vmin or valor > registro_rxp.vmax:
                                                                    r +=1
                                                                    print(f"{WARNING}El valor ingresado se encuentra fuera del rango{NORMAL}")    

                                                if r == 2:
                                                    archivo_logico_operaciones.seek(posicion_final)
                                                    registro_operaciones = pickle.load(archivo_logico_operaciones)
                                                    registro_operaciones.estado = "R"
                                                    archivo_logico_operaciones.seek(posicion_final)
                                                    pickle.dump(registro_operaciones,archivo_logico_operaciones)
                                                    g = len(rubros)
                                                    print(f"{WARNING}El camion ha sido rechazado{NORMAL}")    

                                                g += 1                            
                                            if registro_operaciones.estado != "R":
                                                archivo_logico_operaciones.seek(posicion_final)
                                                registro_operaciones = pickle.load(archivo_logico_operaciones)
                                                registro_operaciones.estado = "C"
                                                archivo_logico_operaciones.seek(posicion_final)
                                                pickle.dump(registro_operaciones,archivo_logico_operaciones)
                                                g = len(rubros)
                                                print(f"{SUCCESS}El camion ha sido aceptado{NORMAL}") 
                                else:
                                    print(f"{WARNING}No hay Rubros ingresados para el producto del camion en cuestion, por lo tanto, no se puede realizar el control de calidad.{NORMAL}")
                    if razon == 0:
                        print(f"{WARNING}No hay camiones ingresados para el producto del camion en cuestion, por lo tanto, no se  puede realizar el control de calidad.{NORMAL}")
                    elif razon == 1:
                        print(f"{WARNING}El estado del camion en cuestion no es el correcto, por lo tanto, no se  puede realizar el control de calidad.{NORMAL}")

                    archivo_logico_operaciones.flush()
                    archivo_logico_productos.flush()
                    archivo_logico_rubros.flush()
                    archivo_logico_rxp.flush()
                    archivo_logico_productos.close()
                    archivo_logico_rubros.close()
                    archivo_logico_rxp.close()
                    archivo_logico_operaciones.close()  
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Registrar la calidad de otro camion")
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
                
                patente_ingresada = input_validation_TP3.check_pat().ljust(7)                
                while archivo_logico.tell() < longitud_archivo:
                    posicion = archivo_logico.tell()
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente: # verifico que la pantente haya sido ingresada
                        razon = 1
                        print(f"{registro.patente} {registro.estado}")

                        if registro.estado == "C": # verifico el estado
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
                
                patente_ingresada = input_validation_TP3.check_pat().ljust(7)                
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
    clear_shell()
    print("0 - Volver al menu anterior \nEl reporte actual es: ")
    
    codprod = [[],[],[],[],[]] # nombre del silo, codigo del producto, cantidad de camiones, cantidad de stock
    cant_cupos_otorgados = 0
    cant_camiones_recibidos = 0
    mayor_stock = 0
    nombre_silo_mayor_stock = ""
    patentes_rechazadas = []
    
    fecha_ingresada = input_validation_TP3.check_fecha("reportes").ljust(8)
        
    if os.path.exists("OPERACIONES.dat"):
        registro_silos = main_TP3.Silos()
        registro_operaciones = main_TP3.Operaciones()
        archivo_logico_silos = open("SILOS.dat", "rb") # no verifico la existencia del archivo silos porque si se ingresa un camion al menos un silo debe existir
        archivo_logico_operaciones = open("OPERACIONES.dat", "rb")
        longitud_silos = os.path.getsize("SILOS.dat")
        longitud_operaciones = os.path.getsize("OPERACIONES.dat")
        
        while archivo_logico_silos.tell() < longitud_silos:
            registro_silos = pickle.load(archivo_logico_silos)
            if registro_silos.stock > mayor_stock:
                nombre_silo_mayor_stock = registro_silos.nomsil
                mayor_stock = registro_silos.stock
                
            if registro_silos.codprod not in codprod[0]:
                codprod[0].append("")
                codprod[1].append(registro_silos.codprod)
                codprod[2].append(0)
                codprod[3].append(0 + registro_silos.stock)
                codprod[4].append(0)
        
        while archivo_logico_operaciones.tell() < longitud_operaciones:
            cant_cupos_otorgados += 1
            registro_operaciones = pickle.load(archivo_logico_operaciones)
            
            for x in codprod[1]:
                menor = 100000000000
                if registro_operaciones.codprod == x:
                    indice = codprod[1].index(x)
                    codprod[2][indice] += 1
                    codprod[4][indice] = registro_operaciones.pesobruto - registro_operaciones.tara
                    if registro_operaciones.pesobruto < menor:
                        codprod[0][indice] = registro_operaciones.patente.strip()
                    
            if registro_operaciones.estado == "A":
                cant_camiones_recibidos += 1
            elif registro_operaciones.estado == "R" and registro_operaciones.fecha == fecha_ingresada:
                patentes_rechazadas.append(registro_operaciones.patente)
                
        archivo_logico_operaciones.flush()
        archivo_logico_silos.flush()
        archivo_logico_silos.close()
        archivo_logico_operaciones.close()

    print(f"Cantidad de cupos otorgados: {cant_cupos_otorgados}")
    print(f"Cantidad de camiones recibidos: {cant_camiones_recibidos}")
    
    if os.path.exists("PRODUCTOS.dat"):
        registro_productos = main_TP3.Productos()
        archivo_logico_productos = open("PRODUCTOS.dat", "rb")
        longitud_productos = os.path.getsize("PRODUCTOS.dat")
        for prod in codprod[1]:
            while archivo_logico_productos.tell() < longitud_productos:
                registro_productos = pickle.load(archivo_logico_productos)
                if registro_productos.codprod == prod:
                    indice = codprod[1].index(prod)
                    print(f"la cantidad de camiomnes del producto {registro_productos.nomprod.strip()}, de codigo {registro_productos.codprod}, es: {codprod[2][indice]}")
                    if codprod[2][indice] == 0:
                        print("No se registraron camiones de este producto")
                    else: 
                        print(f"La pantente del camión que menos descargó de ese producto es: {codprod[0][indice]}")
                        print(f"El promedio del peso neto por camión de este producto es: {codprod[4][indice]/codprod[2][indice]}")
                    print(f"El peso neto del stock del mismo producto es: {codprod[3][indice]}")
                    print("----------------------------------------------")
            archivo_logico_productos.seek(io.SEEK_SET)
        archivo_logico_productos.flush()
        archivo_logico_productos.close()
    else:
        print("No se han ingresados productos aún")
        
    if mayor_stock == 0:
        print(f"No existen silos creados para los productos existentes o no existen productos")
    else:
        print(f"El nombre del silo con mayor stock es: {nombre_silo_mayor_stock.strip()}, con un stock de: {mayor_stock}")
    
    print(f"Listado de las patentes rechazadas el día {fecha_ingresada} es: {patentes_rechazadas}")
    
    option = input_validation_TP3.check_int()
    if option != 0:
        print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
                 
# TERMINADO
def menu_opciones(menu: str):
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        if 1 == option:
            archivos_TP3.alta(menu)
        elif 2 == option and menu == "productos":
            if os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Ya se han registrado camiones. Ya no es posible dar de baja los productos{NORMAL}")
            else:
                archivos_TP3.baja()
        elif option == 3:
            archivos_TP3.consulta(menu)
            input("Precione enter para continuar... ")
        elif option == 4 and menu == "productos":
            if os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Ya se han registrado camiones. Ya no es posible dar de baja los productos{NORMAL}")
            else:
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