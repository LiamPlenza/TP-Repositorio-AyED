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
    x=0
    while True:
        try:
            
            if x == 0:
                option = int(input())
                x += 1
            else:
                option = int((input("Seleccione una opción del menu: ")))
            return option
        except ValueError:
            print(f"{WARNING}Ingrese un valor numérico valido{NORMAL}")
            
#valido que el producto ingresado este entre las opciones dadas
def check_producto(menu) -> str:
    if menu == "productos":
        valid_options = ["TRIGO", "SOJA", "MAIZ", "CEBADA", "ARROZ"]
    elif menu == "rubros":
        valid_options = ["TRIGO", "SOJA", "MAIZ", "CEBADA", "ARROZ"] 
    elif menu == "silos":
        valid_options = ["TRIGO", "SOJA", "MAIZ", "CEBADA", "ARROZ"]       
    option_selected = input(f"Las optiones validas son: {valid_options}\nIngrese una opcion: ").upper()
    while option_selected not in valid_options:
        print(f"{WARNING}Ingrese una opción valida{NORMAL}")
        option_selected = input(f"Las optiones validas son: {valid_options}\nIngrese una opcion: ").upper()
    return option_selected

#valido si la patente se encuentra dentro del array cupos, es decir, que haya pedido un cupo previamente
def check_cupo_valido(matriz_camiones: list, patente: str) -> tuple:
    indice = 0
    while indice < len(matriz_camiones):
        if matriz_camiones[indice][0] == patente:
            return True, indice
        else:
            indice += 1
    return False, 0