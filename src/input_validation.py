WARNING = '\033[1;31m'
NORMAL = '\033[0m'

def check_pat() -> str:
    patente = input("Ingrese la patente: ").upper()
    if len(patente) == 6:
        for contador, caracter in enumerate(patente):
            if contador < 3:
                if caracter.isdigit():
                    print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                    check_pat()
            elif "A" <= caracter <= "Z":
                print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                check_pat()
            break
    elif len(patente) == 7:
        for contador, caracter in enumerate(patente):
            if contador < 2 or 4 < contador < 7: #AA123AA
                if caracter.isdigit():
                    print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                    check_pat()
            elif "A" <= caracter <= "Z":
                print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
                check_pat()
            break
    else:
        print(f"{WARNING}Ingrese un formato de patente valido (aa111aa o aaa111) {NORMAL}")
        check_pat()
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