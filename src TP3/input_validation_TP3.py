import re
import os, time, pickle, io, os.path, datetime
import input_validation_TP3, user_menu_TP3, main_TP3


WARNING = '\033[1;31m'
NORMAL = '\033[0m'

# valido el formato de la patente, utilizando el modulo re -> [A-Z] corresponde a culquier letra y \d corresponde a cualquier dígito
def check_pat() -> str:
    patente = input("Ingrese la patente: ").upper()
    while not re.match(r"[A-Z][A-Z][A-Z]\d\d\d", patente) and not re.match(r"[A-Z][A-Z]\d\d\d[A-Z][A-Z]", patente):
        print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
        patente = input("Ingrese la patente: ").upper()
    return patente

#valido el formato de la fecha
def check_fecha () -> str:
    año = int(input("Ingrese el año:"))
    while año < datetime.now().year:
        año = int(input(f"Ingrese un año valido (mayor o igual a {datetime.now().year}"))
    if año == datetime.now().year:  
        mes = int(input("Ingrese el mes (formato númerico): "))
        while 12 < mes or mes < datetime.now().month:
            mes = int(input(f"Ingrese un mes válido (entre {datetime.now().month} y 12): "))
            if mes == datetime.now().month:
                if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
                    dia = int(input("Ingrese el dia:"))
                    while dia < datetime.now().day or dia > 30:
                        dia = int(input(F"Ingrese un dia válido (entre {datetime.now().day} y 30): "))
                elif mes == 2:
                    dia = int(input("Ingrese el dia:"))
                    while dia > 28 or dia < datetime.now().day:
                        dia = int(input(F"Ingrese un dia válido (entre {datetime.now().day} y 28): "))
                else:
                    dia = int(input("Ingrese el dia:"))
                    while dia > 31 or dia < {datetime.now().day}:
                        dia = int(input(f"Ingrese un dia válido (entre {datetime.now().day} y 31): "))
            else:
                if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
                    dia = int(input("Ingrese el dia:"))
                    while dia < 0 or dia > 31:
                        dia = int(input(F"Ingrese un dia válido (entre 1 y 30): "))
                elif mes == 2:
                    dia = int(input("Ingrese el dia:"))
                    while dia < 0 or dia > 28:
                        dia = int(input(F"Ingrese un dia válido (entre 1 y  28): "))
                else:
                    dia = int(input("Ingrese el dia:"))
                    while dia < 0 or dia > 31:
                        dia = int(input("Ingrese un dia válido (entre 1 y 31): "))
    else:
        mes = int(input("Ingrese el mes (formato númerico): "))
        while 0 > mes or mes > 12:
            if mes == 4 or mes == 6 or mes == 9 or mes == 11 :
                dia = int(input("Ingrese el dia:"))
                while dia < 0 or dia > 31:
                    dia = int(input(F"Ingrese un dia válido (entre 1 y 30): "))
            elif mes == 2:                    
                dia = int(input("Ingrese el dia:"))
                while dia < 0 or dia > 28:
                    dia = int(input(F"Ingrese un dia válido (entre 1 y  28): "))
            else:
                dia = int(input("Ingrese el dia:"))
                while dia < 0 or dia > 31:
                    dia = int(input("Ingrese un dia válido (entre 1 y 31): "))
    fecha = dia + "/" + mes + "/" + año
    return fecha


# valido que el ingreso de los datos del camion, peso y tara sean núnmero flotante
def check_float(mensaje: str)-> float:
    while True:
        try:
            option = float((input(mensaje)))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")

# valido que el ingreso de las opciones del menu sean numericos
def check_int()-> int:
    while True:
        try:
            option = int(input("Seleccione una opción del menu: "))
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
    else:
        registros_activados = False
    archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo
    return registros_activados

def check_producto_valido () -> int:
    archivo_logico = open("PRODUCTOS.dat", "r+b")
    longitud_archivo = os.path.getsize("PRODUCTOS.dat")
    registro = main_TP3.Productos()   
    archivo_logico.seek(io.SEEK_SET)
    producto_ingresado = input("Ingrese el producto que contiene el camion:")
    while archivo_logico.tell() < longitud_archivo:
        registro = pickle.load(archivo_logico)
        if producto_ingresado == registro.nomprod:
            return registro.codprod
    print(f"{WARNING}El producto ingresado no se encuentra entre los activos. Pruebe de nuevo{NORMAL}")
    archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo
    check_producto_valido()