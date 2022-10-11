from datetime import datetime
import main_TP3, calendar, os, pickle, io, os.path, re, archivos_TP3, time

WARNING = '\033[1;31m'
NORMAL = '\033[0m'

# valido el formato de la patente, utilizando el modulo re -> [A-Z] corresponde a culquier letra y \d corresponde a cualquier dígito
def check_pat() -> str:
    patente = input("Ingrese la patente: ").upper()
    while True:
        if len(patente) == 6:
            while not re.match(r"[A-Z][A-Z][A-Z]\d\d\d", patente):
                print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                patente = input("Ingrese la patente: ").upper()
            return patente
        elif len(patente) == 7:
            while not re.match(r"[A-Z][A-Z]\d\d\d[A-Z][A-Z]", patente):
                print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                patente = input("Ingrese la patente: ").upper()
            return patente
        else:
            print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
            patente = input("Ingrese la patente: ").upper()

#valido el formato de la fecha
def check_fecha () -> str:
    año = check_int("Ingrese el año (yyyy): ")
    while año < int(datetime.today().year) or len(str(año)) != 4:# verifico si el año es a futuro, si es menor al año actual pido otra vez el año
        año = check_int(f"{WARNING}Ingrese un año valido (mayor o igual a {datetime.today().year} con el formato yyyy):{NORMAL}")
    
    mes = check_int("Ingrese el mes (formato númerico): ")# pido el mes
    
    if año == int(datetime.today().year):# si el año es el actual verifico que el mes sea entre el actual y el último  
        while int(datetime.today().month) > mes or mes > 13:
            mes = check_int(f"{WARNING}Ingrese un mes válido (entre {datetime.today().month} y 12): {NORMAL}")
        if mes == int(datetime.today().month):
            dia = check_int("Ingrese el número del día: ")    
            dias_del_mes = calendar.monthrange(año, mes)[1]# obento la cantidad de días del mes selección en el año correspondiente
            while int(datetime.today().day) > dia or dia > dias_del_mes:# verifico que el día 
                dia = check_int(f"{WARNING}Ingrese un día valido (entre {datetime.today().day} y {dias_del_mes}): {NORMAL}")
        else:
            dias_del_mes = calendar.monthrange(año, mes)[1]# obento la cantidad de días del mes selección en el año correspondiente
            while  1 > dia or dia > dias_del_mes:# verifico que el día 
                dia = check_int(f"{WARNING}Ingrese un día valido (entre 1 y {dias_del_mes}): {NORMAL}")
    else:
        while 0 > mes or mes > 13:# si no es el año actual la única restricción es que sea entre 1 y 12   
            mes = check_int(f"{WARNING}Ingrese un mes válido (entre 1 y 12): {NORMAL}")
        
        dia = check_int("Ingrese el número del día: ")
        dias_del_mes = calendar.monthrange(año, mes)[1]# obento la cantidad de días del mes selección en el año correspondiente
        while 0 > dia or dia > dias_del_mes: 
            dia = check_int(f"{WARNING}Ingrese un día valido (entre 1 y {dias_del_mes}): {NORMAL}")
            

    return str(dia)+"/"+str(mes)+"/"+str(año)

# valido que el ingreso de las opciones del menu sean numericos
def check_int(mensaje = "Seleccione una opción del menu: ")-> int:
    while True:
        try:
            option = int(input(mensaje))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")          

#valido que haya productos ingresados
def check_producto () -> bool:
    registros_activados = False    
    if os.path.exists("PRODUCTOS.dat"):
        archivo_logico = open("PRODUCTOS.dat", "r+b")
        longitud_archivo = os.path.getsize("PRODUCTOS.dat")
        #archivo_logico.seek(io.SEEK_SET) # linea no necesaria (probar)
        while archivo_logico.tell() < longitud_archivo:
            registro = pickle.load(archivo_logico)
            if registro.activo:
                registros_activados = True
        archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
        archivo_logico.close()# cierro el archivo
    return registros_activados

def check_producto_valido () -> int:
    # solo la llamo si es que existe el archivo asi que no hace falta comprobar aca
    archivo_logico_productos = open("PRODUCTOS.dat", "r+b")
    longitud_archivo_productos = os.path.getsize("PRODUCTOS.dat")
    registro_productos = main_TP3.Productos()
    
    archivo_logico_silos = open("SILOS.dat", "r+b")
    longitud_archivo_silos = os.path.getsize("SILOS.dat")
    registro_silos = main_TP3.Silos()
    
    while True:   
        archivos_TP3.consulta()# muestro los productos que hay
        archivo_logico_productos.seek(io.SEEK_SET) # me muevo al incio
        archivo_logico_silos.seek(io.SEEK_SET)
        producto_ingresado = input("Ingrese el nombre del producto que contiene el camion: ").capitalize().ljust(20)
        while archivo_logico_productos.tell() < longitud_archivo_productos:
            registro_productos = pickle.load(archivo_logico_productos)
            if producto_ingresado == registro_productos.nomprod and registro_productos.activo:
                while archivo_logico_silos.tell() < longitud_archivo_silos:
                    registro_silos = pickle.load(archivo_logico_silos)
                    if registro_productos.codprod == registro_silos.codprod:
                        codigo_producto = registro_productos.codprod
                        
                        archivo_logico_silos.flush()
                        archivo_logico_productos.flush() # me aseguro que no quede pendiente ningún registro en el bus
                        
                        archivo_logico_silos.close()
                        archivo_logico_productos.close()
                        return codigo_producto
        print(f"{WARNING}El producto ingresado no se encuentra entre los activos o no posee un silo asignado. Pruebe de nuevo{NORMAL}")
        time.sleep(2.5)