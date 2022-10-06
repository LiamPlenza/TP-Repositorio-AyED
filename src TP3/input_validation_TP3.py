from datetime import datetime
import main_TP3, calendar, os, time, pickle, io, os.path, re

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
    while año < datetime.today().year or len(str(año)) != 4:# verifico si el año es a futuro, si es menor al año actual pido otra vez el año
        año = check_int(f"Ingrese un año valido (mayor o igual a {datetime.today().year} con el formato yyyy): ")
    
    mes = check_int("Ingrese el mes (formato númerico): ")# pido el mes
    
    if año == datetime.today().year:# si el año es el actual verifico que el mes sea entre el actual y el último  
        while not datetime.today().month <= mes < 13:
            mes = check_int(f"Ingrese un mes válido (entre {datetime.today().month} y 12): ")
            
        dia = check_int("Ingrese el número del día: ")    
        dias_del_mes = calendar.monthrange(año, mes)[1]# obento la cantidad de días del mes selección en el año correspondiente
        while not int(datetime.today().day) <= dia <= dias_del_mes:# verifico que el día 
            dia = check_int(f"Ingrese un día valido (entre {datetime.today().day} y {dias_del_mes}): ")
    else:
        while not 0 < mes < 13:# si no es el año actual la única restricción es que sea entre 1 y 12   
            mes = check_int(f"Ingrese un mes válido (entre {datetime.today().month} y 12): ")
        
        dia = check_int("Ingrese el número del día: ")
        dias_del_mes = calendar.monthrange(año, mes)[1]# obento la cantidad de días del mes selección en el año correspondiente
        while not 0 < dia < dias_del_mes: 
            dia = check_int(f"Ingrese un día valido (entre 1 y {dias_del_mes}): ")
            
    return str(dia)+"/"+str(mes)+"/"+str(año)
            
# valido que el ingreso de los datos del camion, peso y tara sean núnmero flotante
def check_float(mensaje: str)-> float:
    while True:
        try:
            option = float((input(mensaje)))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")

# valido que el ingreso de las opciones del menu sean numericos
def check_int(mensaje = "Seleccione una opción del menu: ")-> int:
    while True:
        try:
            option = int(input(mensaje))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")          

#valido si la patente se encuentra dentro del array cupos, es decir, que haya pedido un cupo previamente
def check_cupo_valido(matriz_camiones: list, patente: str) -> tuple:
    indice = 0
    while indice < len(matriz_camiones):
        if matriz_camiones[indice][0] == patente:
            return True, indice
        else:
            indice += 1
    return False, 0

#valido que haya productos ingresados
def check_producto () -> bool:
    if os.path.exists("PRODUCTOS.dat"):
        archivo_logico = open("PRODUCTOS.dat", "r+b")
        longitud_archivo = os.path.getsize("PRODUCTOS.dat")
        registros_activados = False    
        archivo_logico.seek(io.SEEK_SET)
        while archivo_logico.tell() < longitud_archivo:
            registro = pickle.load(archivo_logico)
            if registro.activo:
                registros_activados = True
        archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
        archivo_logico.close()# cierro el archivo
    else:
        registros_activados = False
    
    return registros_activados

def check_producto_valido () -> int:
    archivo_logico = open("PRODUCTOS.dat", "r+b")
    longitud_archivo = os.path.getsize("PRODUCTOS.dat")
    registro = main_TP3.Productos()   
    archivo_logico.seek(io.SEEK_SET)
    producto_ingresado = input("Ingrese el producto que contiene el camion:").capitalize().ljust(20)
    while archivo_logico.tell() < longitud_archivo:
        registro = pickle.load(archivo_logico)
        if producto_ingresado == registro.nomprod and registro.activo:
            aux = registro.codprod
            archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
            archivo_logico.close()
            return aux
    print(f"{WARNING}El producto ingresado no se encuentra entre los activos. Pruebe de nuevo{NORMAL}")
    archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo
    check_producto_valido()