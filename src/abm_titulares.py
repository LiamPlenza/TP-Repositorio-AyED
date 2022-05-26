import os, time, input_validation,user_menu
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'


def alta(titulares):
    user_menu.clear_shell()
    
    print("0 - Volver al menu anterior \n1 - Ingresar un nuevo titular")
    option = input_validation.check_int()
    while option != 0:
        if option == 1:
                titulares.append(input("Ingrese el nombre del titular en cuestión: "))
                print(f"{SUCCESS}Se ingreso el nuevo titular correctamente{NORMAL}")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
        time.sleep(1.5)
        user_menu.clear_shell()
        print("0 - Volver al menu anterior \n1 - Ingresar un nuevo titular")            
        option = input_validation.check_int()

def consulta(titulares):
    user_menu.clear_shell()
    if titulares == []:
        print(f"{WARNING}No hay titulares ingresados{NORMAL}")
        time.sleep(1.5)
    else:
        print("La actual lista de titulares es:\n*-------------------------------*")
        for indice, titular in enumerate(titulares):
            print("|{:^3}| {:25} |".format(indice+1, titular))
        print("| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")
    #os.system("pause")

def baja(titulares):
    user_menu.clear_shell()

    if titulares == []:
        consulta(titulares)
    else:
        consulta(titulares)
        option = input_validation.check_int()

        while option != 0:
            if option not in [x for x in range(1, len(titulares)+1)]: # me fijo si la opcion seleccionada NO está en una lista [1...opcion] 
                print(f"{WARNING}Ingrese un titular existente{NORMAL}") 
                option = input_validation.check_int()
            else:
                titulares.pop(option-1)
                print(f"{SUCCESS}El titular ha sido eliminado{NORMAL}")
                time.sleep(1)
                if titulares == []:
                    consulta(titulares)
                    option = 0
                else:
                    consulta(titulares)
                    option = input_validation.check_int()


def modificacion(titulares):
    user_menu.clear_shell()
    i = 0
    if titulares == []:
        consulta(titulares)
    else:
        consulta(titulares)
        option = input_validation.check_int()
    
        while option != 0:
            if option not in [x for x in range(1, len(titulares)+1)]: # me fijo si la opcion seleccionada NO está en una lista [1...opcion] 
                print(f"{WARNING}Ingrese un titular existente{NORMAL}")
                option = input_validation.check_int() 
            else:
                titulares[option - 1] = input("Ingrese el nombre del titular en custión: ")
                print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                time.sleep(1)
                consulta(titulares)
                option = input_validation.check_int()
