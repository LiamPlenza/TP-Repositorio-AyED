import input_validation_TP3, os, pickle, time, main_TP3
from datetime import datetime

WARNING = '\033[1;31m'
NORMAL = '\033[0m'
SUCCESS = '\033[1;32m'

def hoy():
    return str(datetime.today().day)+"/"+str(datetime.today().month)+"/"+str(datetime.today().year)

def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def mostrar():
    registro = main_TP3.Silos()
    archivo_logico = open("SILOS.dat", "rb")
    longitud_archivo = os.path.getsize("SILOS.dat")
    while archivo_logico.tell() < longitud_archivo: # recorro todo el archivo
        registro = pickle.load(archivo_logico)
        print(f"{registro.codsil}, {registro.nomsil}, {registro.codprod}, {registro.stock}")
    archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo       
    
def menu_recepcion():
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
                patente_ingresada = input_validation_TP3.check_pat()
                
                while archivo_logico.tell() < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente:
                        razon = 1 
                        fecha_de_entrega = registro.fecha
                        if registro.fecha == hoy(): # probar == hoy()
                            razon = 2
                            if registro.estado == "P":
                                razon = 3
                                posicion = archivo_logico.tell()

                if razon == 3:
                    archivo_logico.seek(posicion - 134) # me muevo al registro que tengo que tengo que actualizar, cada registro pesa 134 el tema que cuando hago el load ya avanza el registro
                    registro = pickle.load(archivo_logico)
                    registro.estado = "A" # no hace falta hacer el load primero y después nuevamente el seek para hacer el dump en el lugar correspondiente?
                    archivo_logico.seek(posicion - 134) # me muevo otra vez porque el load avanza solo
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
   
def entrega_de_cupos():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP3.check_int()
    while option != 0:
        cupo_ya_otorgado = False
        if option == 1:
            if not input_validation_TP3.check_producto():
                print(f"{WARNING}No hay productos activos.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                if os.path.exists("OPERACIONES.dat"): # veo si el archivo existe para ver como lo abro
                    archivo_logico = open("OPERACIONES.dat", "r+b")
                    longitud_archivo = os.path.getsize("OPERACIONES.dat")
                    
                    patente_ingresada = input_validation_TP3.check_pat()
                    
                    print("Ingrese la fecha deseada para el cupo:")
                    fecha_ingresada = input_validation_TP3.check_fecha()
                    
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
                    registro.patente = input_validation_TP3.check_pat()
                    print("Ingrese la fecha deseada para el cupo:")
                    registro.fecha = input_validation_TP3.check_fecha()

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
        
def registro_peso_bruto():
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
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente: # verifico que la pantente haya sido ingresada
                        razon = 1
                        if registro.estado == "A": # verifico el estado
                            razon = 2
                            #bandera = True
                            peso_bruto_ingresado = input_validation_TP3.check_int("Ingrese el peso bruto del camion: ")
                            posicion = archivo_logico.tell() # guardo la posicion del registro a modificar
                            
                    #else:
                            #bandera = False
                    #if bandera == False:
                if razon == 0:
                    print(f"{WARNING}La patente ingresada no coincide con una registrada{NORMAL}")
                elif razon == 1: 
                    print(f"{WARNING}El estado de del camion debe ser Con Calidad. Pase por recepcion previamente{NORMAL}")
                else: # 134 es el peso de un unico registro
                    archivo_logico.seek(posicion - 134) # me paro en el inicio del registro a modificar (no te enojes liam por el -134 es que sino no anda)
                    registro = pickle.load(archivo_logico)
                    registro.estado = "B"
                    registro.pesobruto = peso_bruto_ingresado
                    archivo_logico.seek(posicion - 134) # me muevo otra vez al inicio del registro porque el load se mueve solo
                    pickle.dump(registro,archivo_logico)
                    print(f"{SUCCESS}Peso bruto registrado con exito{NORMAL}")

                time.sleep(2.5)
                archivo_logico.flush()
                archivo_logico.close()
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
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
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente:
                        razon == 1
                        if registro.estado == "B":
                            razon = 2
                            tara_ingresada = input_validation_TP3.check_int(f"Ingrese la tara del camion. Esta debe ser menor a {registro.pesobruto}: ")
                            while tara_ingresada > registro.pesobruto:
                                tara_ingresada = input_validation_TP3.check_int(f"La tara debe ser menor a {registro.pesobruto}. Pruebe nuevamente: ")
                            posicion = archivo_logico.tell()
                
                if razon == 0:
                    print(f"{WARNING}La patente ingresada no coincide con una registrada{NORMAL}")
                elif razon == 1:
                    print(f"{WARNING}El estado de del camion debe ser 'Bruto'. Pase por 'Registrar Peso Bruto' previamente{NORMAL}")
                else:     
                    archivo_logico.seek(posicion - 135) # me paro en el inicio del registro a modificar (no te enojes liam por el -134 es que sino no anda)
                    registro = pickle.load(archivo_logico)
                    registro.estado = "F"
                    registro.tara = tara_ingresada
                    
                    # guardo el stock en el silo
                    registro_silo = main_TP3.Silos()
                    archivo_logico_silos = open("SILOS.dat", "r+b")
                    longitud_archivo_silos = os.path.getsize("SILOS.dat")
                    while archivo_logico_silos.tell() < longitud_archivo_silos:
                        registro_silo = pickle.load(archivo_logico_silos)
                        if registro_silo.codprod == registro.codprod:
                            posicion_silo = archivo_logico_silos.tell()
                            
                    archivo_logico_silos.seek(posicion_silo - 106)
                    registro_silo =  pickle.load(archivo_logico_silos)
                    registro_silo.stock = registro.pesobruto - registro.tara
                    
                    archivo_logico_silos.seek(posicion_silo - 106)
                    archivo_logico.seek(posicion - 135) # me muevo otra vez al inicio del registro porque el load se mueve solo
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
        
registro_tara()
mostrar()