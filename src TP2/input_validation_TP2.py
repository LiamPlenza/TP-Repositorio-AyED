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
def check_producto() -> str:
    producto = input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper()
    while producto not in ["TRIGO", "SOJA", "MAIZ", "CEBADA", "ARROZ"]:
        print(f"{WARNING}Ingrese una opción valida{NORMAL}")
        producto = input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maíz)\nIngrese un producto: ").upper()
    return producto

#valido si la patente se encuentra dentro del array cupos, es decir, que haya pedido un cupo previamente
def check_cupo_valido(cupos: list, patente: str):
    indice = 0
    while indice < len(cupos):
        if cupos[indice] == patente:
            return True, indice
        else:
            indice += 1
    return False, 0
