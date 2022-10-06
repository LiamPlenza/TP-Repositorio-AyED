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
    dia = datetime.today().day
    mes = datetime.today().month
    año = datetime.today().year
    dia = str(dia)
    mes = str(mes)
    año = str(año)
    fecha = dia+"/"+mes+"/"+año
    return fecha

def entrega_de_cupos():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Solicitar cupo")
    option = input_validation_TP3.check_int()
    bandera = 0
    while option != 0:
        if option == 1:
            if not input_validation_TP3.check_producto():
                print(f"{WARNING}No hay productos activos.{NORMAL}")
            else:
                registro = main_TP3.Operaciones()
                if os.path.exists("OPERACIONES.dat"):
                    archivo_logico = open("OPERACIONES.dat", "r+b")
                    longitud_archivo = os.path.getsize("OPERACIONES.dat")
                    patente_ingresada = input_validation_TP3.check_pat()
                    print("Ingrese la fecha deseada para el cupo:")
                    fecha_ingresada = input_validation_TP3.check_fecha()
                    archivo_logico.seek(io.SEEK_SET)
                    while archivo_logico.tell() < longitud_archivo:
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
                        print(f"{SUCCESS}El cupo ha sido otorgado con éxito.{NORMAL}")
                        pickle.dump(registro,archivo_logico)
                        archivo_logico.flush()
                        archivo_logico.close()
                    

                else:
                    archivo_logico = open("OPERACIONES.dat", "w+b")
                    registro.patente = input_validation_TP3.check_pat()
                    registro.fecha = input_validation_TP3.check_fecha()
                    registro.codprod = input_validation_TP3.check_producto_valido() 
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

def registrar_calidad():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar calidad")
    option = input_validation_TP3.check_int()
    
    while option != 0:
        if option == 1:
            if not(os.path.exists("OPERACIONES.dat") and os.path.exists("RUBROS.dat") and os.path.exists("PRODUCTOS.dat") and os.path.exists("RUBROS-X-PRODUCTO.dat")):
                print(f"{WARNING}No se cumplen todos los requerimientos para llevar a cabo este registro.{NORMAL}")
            else:
                archivo_logico = open ("OPERACIONES.dat", "r+b")
                archivo_logico_r = open("RUBROS.dat", "r+b")
                archivo_logico_p= open("PRODUCTOS.dat", "r+b")
                archivo_logico_rxp = open ("RUBROS-X-PRODUCTO.dat", "r+b")
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
                while archivo_logico.tell() < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    
                    if patente_ingresada == registro.patente and registro.estado == "A": #Chequeo si el estado del camion es el correcto
                        bandera = True
                        rubros = []
                        while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                            registro_rxp = pickle.load(archivo_logico_rxp) 
                            if registro.codprod == registro_rxp.codprod: #Busco el producto del camion dentro del archivo rubro por producto
                               rubros.append(registro_rxp.codrub)
                        if len(rubros) > 0: 
                            while archivo_logico_p.tell() < longitud_archivo_p:
                                registro_p = pickle.load(archivo_logico_p)
                                if registro_p.codprod == registro_rxp.codprod:
                                    print(f"El camion contiene {registro_p.nomprod} ingrese la calidad correspondiente a los siguientes rubros:")
                                r=0
                                g=0
                                while g < len(rubros):
                                    while archivo_logico_r.tell() < longitud_archivo_r:
                                        registro_r = pickle.load(archivo_logico_r)
                                        if registro_r.codrub == rubros[g]:
                                            valor = int(input(f"Ingrese el valor para el rubro {registro_r.nomrub}:"))
                                            archivo_logico_rxp.seek(io.SEEK_SET) # me muevo al inicio del archivo
                                            while archivo_logico_rxp.tell() < longitud_archivo_rxp:
                                                registro_rxp = pickle.load(archivo_logico_rxp)
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
                archivo_logico.flush()
                archivo_logico_p.flush()
                archivo_logico_r.flush()
                archivo_logico_rxp.flush()
                archivo_logico_p.close()
                archivo_logico_r.close()
                archivo_logico_rxp.close()
                archivo_logico.close()
                if not bandera:
                    print(f"{WARNING}El camion no cumple con los requisitos para realizar esta acción{NORMAL}")    
        else:
            print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
            
        time.sleep(2.5)
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar el peso bruto de otro camion")
        option = input_validation_TP3.check_int()    


def registro_peso_bruto():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
    option = input_validation_TP3.check_int()
    bandera = False
    while option != 0:
        razon = 0
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:
                archivo_logico = open("OPERACIONES.dat", "r+b")
                registro = main_TP3.Operaciones()
                longitud_archivo = os.path.getsize("OPERACIONES.dat")
                patente_ingresada = input_validation_TP3.check_pat()
                
                while archivo_logico.tell() < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    if patente_ingresada == registro.patente:
                        razon = 1
                        if registro.estado == "A":
                            razon = 2
                            bandera = True
                            print("Ingrese el peso bruto del camion")
                            peso_bruto = input_validation_TP3.check_int()
                            print(f"{SUCCESS}Peso bruto registrado con exito{NORMAL}")
                            registro.estado = "B"
                            registro.pesobruto = peso_bruto
                            time.sleep(2.5)
                    else:
                        bandera = False
                if bandera == False:
                    if razon == 0:
                        print(f"{WARNING}La patente ingresada no coincide con una registrada{NORMAL}")
                        if razon == 1: 
                            print(f"{WARNING}El estado de del camion debe ser Con Calidad{NORMAL}")
                    time.sleep(2.5)
                archivo_logico.flush()
                archivo_logico.close()
        clear_shell()
        print("0 - Volver al menu anterior\n1 - Registrar peso bruto")
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

def menu_reportes():
    pass
    
def menu_recepcion():
    clear_shell()
    bandera = False
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = input_validation_TP3.check_int()
    while option != 0:
        razon = 0
        if option == 1:
            if not os.path.exists("OPERACIONES.dat"):
                print(f"{WARNING}Aún no hay operaciones registradas.{NORMAL}")
            else:
                archivo_logico = open ("OPERACIONES.dat", "r+b")
                registro = main_TP3.Operaciones()
                longitud_archivo = os.path.getsize("OPERACIONES.dat")

                print("Ingresar la patente del camión del cual desea ingresar")
                patente_ingresada = input_validation_TP3.check_pat()
                archivo_logico.seek(io.SEEK_SET)
                while archivo_logico.tell() < longitud_archivo:
                    registro = pickle.load(archivo_logico)
                    fecha = hoy()
                    if patente_ingresada == registro.patente:
                        razon = 1 
                        if registro.fecha == fecha:
                            razon = 2
                            if registro.estado == "P":
                                razon = 3
                                pos = archivo_logico.tell()
                                bandera = True

                if bandera and razon == 3:
                    archivo_logico.seek(pos)
                    registro.estado = "A"
                    pickle.dump(registro,archivo_logico)
                    archivo_logico.flush()
                    archivo_logico.close()
                    print(f"{SUCCESS}El camion ha sido ingresado con exito{NORMAL}")
                    bandera = False
                else:
                    if razon == 0:
                        print(f"{WARNING}La patente ingresada no coincide con un camion registrado{NORMAL}")
                    if razon == 1:
                        print(f"{WARNING}El camion tiene un cupo asignado para un dia que no es hoy{NORMAL}")
                    if razon == 2:
                        print(f"{WARNING}Para poder recepcionar un camion, el mismo debe tener estado Pendiente{NORMAL}")    
                    archivo_logico.flush()
                    archivo_logico.close()
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