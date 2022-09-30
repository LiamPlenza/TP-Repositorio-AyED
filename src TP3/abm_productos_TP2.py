
import time, input_validation_TP2, user_menu_TP2
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'

def alta(abm_list, menu):
    user_menu_TP2.clear_shell()
    if abm_list[2] != "":
        print(f"{WARNING}Se ha alcanzado la cantidad maxima(3){NORMAL} ")
        time.sleep(1.5)
    else: 
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
        option = input_validation_TP2.check_int()
        while option != 0:
            indice = 0
            if option == 1:
                while indice < 3:
                    if abm_list[indice] == "":#si encuentra un espacio vacio en producto lo agrego
                        abm_list[indice] = input_validation_TP2.check_producto(menu)
                        if indice == 2: 
                            while abm_list[indice] == abm_list[0] or abm_list[indice] == abm_list [1]:
                                print(f"{WARNING}Ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                abm_list[indice] = input_validation_TP2.check_producto()
                        elif indice == 1:
                            while abm_list[1] == abm_list[0]:
                                print(f"{WARNING}Ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                abm_list[indice] = input_validation_TP2.check_producto()
                        indice = 10
                        print(f"{SUCCESS}Se ha sido ingresado con éxito{NORMAL}")
                        time.sleep(0.7)
                    indice += 1  
                
                time.sleep(1.5)
                user_menu_TP2.clear_shell()
                
                print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
                option = input_validation_TP2.check_int()
                if option == 1 and abm_list[2] != "":
                    print(f"{WARNING}Se ha alcanzado la cantidad maxima de abm_list (3){NORMAL} ")
                    option = 0
                    time.sleep(1.5)
            else:
                print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
                option = input_validation_TP2.check_int()
                
def consulta(abm_list):
    user_menu_TP2.clear_shell()    
    if abm_list[0] == "":#como el array se llena del 0 al 2 si el primero es 0 es porque esta vacía
        print(f"{WARNING}No hay abm_list ingresados{NORMAL}")
        time.sleep(1.5)
    else:
        indice = 0
        print("La actual lista de abm_list es:\n*-------------------------------*")
        while indice <3:
            if abm_list[indice] != "":
                print("|{:^3}| {:25} |".format(indice+1, abm_list[indice]))
            indice +=1
        print("| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")
def baja(abm_list):
    user_menu_TP2.clear_shell()
    if abm_list[0] == "":
        print(f"{WARNING}No hay abm_list ingresados{NORMAL}")
        time.sleep(1.5)
    else: 
        consulta(abm_list)# como la lista no está vacía, llamo a consulta para que la imprima
        option = input_validation_TP2.check_int()
        
        while option != 0:
            while 0 > option or option > 4 or abm_list[option-1] == "": # me fijo si la opcion no esta en el rango o si la opcion esta vacia
                print(f"{WARNING}Ingrese un producto existente{NORMAL}") 
                option = input_validation_TP2.check_int()
            else:
                    option -= 1
                    if option == 2:
                        abm_list[option] = ""
                    elif option == 0:
                        abm_list[option] = abm_list[option + 1]
                        abm_list[option + 1] = abm_list[option + 2]
                        abm_list[option + 2] = ""
                    else:
                        abm_list[option] = abm_list[option + 1]
                        abm_list[option + 1] = ""
                    print(f"{SUCCESS}El producto ha sido eliminado{NORMAL}")
                    time.sleep(1.5)
                    if abm_list[0] == "":
                        print(f"{WARNING}No hay más abm_list ingresados. Volverá al menu anterior.{NORMAL}")
                        time.sleep(1.5)
                        option = 0
                    else: 
                        user_menu_TP2.clear_shell()
                        consulta(abm_list)# como la lista no está vacía, llamo a consulta para que la imprima
                        option = input_validation_TP2.check_int()


def modificacion(abm_list):
    user_menu_TP2.clear_shell()
    i = 0
    if abm_list[0] == "":
        print(f"{WARNING}No hay abm_list ingresados{NORMAL}")
        time.sleep(1.5)
    else:# como el array de abm_list no está vacía la función consulta va a mostrar el array completo
        consulta(abm_list)
        option = input_validation_TP2.check_int()
    
        while option != 0:
            if abm_list[option-1] == "":
                print(f"{WARNING}Ingrese un titular existente{NORMAL}")
                option = input_validation_TP2.check_int() 
            else:
                if abm_list[option - 1] == 0:
                    print(f"{WARNING}No es posible modificar un elemento que está vacio{NORMAL}")
                else:
                    abm_list[option - 1] = input_validation_TP2.check_producto()
                    if option == 3: 
                            while abm_list[2] == abm_list[0] or abm_list[2] == abm_list [1]:
                                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                abm_list[option-1] = input_validation_TP2.check_producto()
                    elif option == 2:
                        while abm_list[1] == abm_list[0] or abm_list[1] == abm_list[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            abm_list[option-1] = input_validation_TP2.check_producto()
                    elif option == 1:
                        while abm_list[0] == abm_list[1] or abm_list[0] == abm_list[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            abm_list[option-1] = input_validation_TP2.check_producto()
                    print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                    time.sleep(1.5)
                    consulta(abm_list)
                    option = input_validation_TP2.check_int()#muestro la lista actualizada de abm_list