import os, time, input_validation_TP2, user_menu_TP2
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'

def alta(productos):
    user_menu_TP2.clear_shell()
    
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
    option = input_validation_TP2.check_int()
    
    indice = 0
    while option != 0:
        if option == 1:
            #while indice < 3:
            #    if productos[indice] == 0:
            #        productos[indice] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Trigo, Soja, Maíz)\nIngrese un producto: "))
            #    indice += 1
            #    if productos[2] != 0:
            #        print("Se ha alcanzado la cantidad maxima de productos (3) ")
            for producto in productos:
                if producto == 0:#si encuentra un espacio vacio en producto lo agrego
                    productos[indice] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Trigo, Soja, Maíz)\nIngrese un producto: "))
                indice += 1
            if indice == 2:
                print("Se ha alcanzado la cantidad maxima de productos (3) ")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")    
            
        time.sleep(1.5)
        user_menu_TP2.clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
        option = input_validation_TP2.check_int()

def consulta(productos):
    user_menu_TP2.clear_shell()    
    if productos[0] == 0:#como el array se llena del 0 al 2 si el primero es 0 es porque esta vacía
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else:
        print("La actual lista de productos es:\n*-------------------------------*")
        for indice, producto in enumerate(productos):
            print("|{:^3}| {:25} |".format(indice+1, producto))
        print("| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")

def baja(productos):
    user_menu_TP2.clear_shell()

    if productos[0] == 0:
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else: 
        consulta(productos)# como la lista no está vacía, llamo a consulta para que la imprima
        print("\n0- Volver al menu anterior\nIngrese el option del producto que desea eliminar: ")
        option = input_validation_TP2.check_int()
        
        while option != 0:
            if option not in [x for x in range(1, len(productos)+1)]: # me fijo si la opcion seleccionada NO está en una lista [1...opcion] 
                print(f"{WARNING}Ingrese un titular existente{NORMAL}") 
                option = input_validation_TP2.check_int()
            else:
                if productos[option-1] == 0:
                    print(f"{WARNING}Ingrese una opción que no esté vacia{NORMAL}")
                    option = input_validation_TP2.check_int()
                else:
                    if option == 2:
                        productos[option] = ""
                    elif option == 0:
                        productos[option] = productos[option + 1]
                        productos[option + 1] = productos[option + 2]
                        productos[option + 2] = 0
                    else:
                        productos[option] = productos[option + 1]
                        productos[option + 1] = ""
                    print(f"{SUCCESS}El titular ha sido eliminado{NORMAL}")

                    time.sleep(1.5)
                    
def modificacion(productos):
    user_menu_TP2.clear_shell()
    i = 0
    if productos[0] == 0:
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else:# como el array de productos no está vacía la función consulta va a mostrar el array completo
        consulta(productos)
        option = input_validation_TP2.check_int()
    
        while option != 0:
            if option not in [x for x in range(1, len(productos)+1)]: # me fijo si la opcion seleccionada NO está en una lista [1...opcion] 
                print(f"{WARNING}Ingrese un titular existente{NORMAL}")
                option = input_validation_TP2.check_int() 
            else:
                if productos[option - 1] == 0:
                    print(f"{WARNING}No es posible modificar un elemento que está vacio{NORMAL}")
                else:
                    productos[option - 1] = input("Ingrese el nombre del titular en cuestión: ")
                    print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                    time.sleep(1.5)
                    consulta(productos)
                    option = input_validation_TP2.check_int()#muestro la lista actualizada de productos