import re
WARNING = '\033[1;31m'
NORMAL = '\033[0m'

# valido el formato de la patente, utilizando el modulo re -> [A-Z] corresponde a culquier letra y \d corresponde a cualquier dígito
def check_pat() -> str:
    patente = input("Ingrese la patente: ").upper()
    while not re.match(r"[A-Z][A-Z][A-Z]\d\d\d", patente) and not re.match(r"[A-Z][A-Z]\d\d\d[A-Z][A-Z]", patente):
        print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
        patente = input("Ingrese la patente: ").upper()
    return patente

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
            option = int((input("Seleccione una opción del menu: ")))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")
            
#valido que el producto ingresado este entre las opciones dadas
def check_producto(producto: str) -> str:
    while producto not in ["TRIGO", "SOJA", "MAIZ", "CEBADA", "ARROZ"]:
        print(f"{WARNING}Ingrese una opción valida{NORMAL}")
        producto = input("(Las opciones valida de producto son: Trigo, Soja, Maíz)\nIngrese un producto: ")
    
    return producto