import os, time, input_validation_TP2, user_menu_TP2
from xml.dom import IndexSizeErr
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'

def alta(productos):
    user_menu_TP2.clear_shell()
    if productos[2] != "":
        print(f"{WARNING}Se ha alcanzado la cantidad maxima de productos (3){NORMAL} ")
        time.sleep(1.5)
    else: 
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
        option = input_validation_TP2.check_int()
        while option != 0:
            indice = 0
            if option == 1:
                while indice < 3:
                    if productos[indice] == "":#si encuentra un espacio vacio en producto lo agrego
                        productos[indice] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())
                        if indice == 2: 
                            while productos[indice] == productos[0] or productos[indice] == productos [1]:
                                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                productos[indice] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())
                        elif indice == 1:
                            while productos[1] == productos[0]:
                                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                productos[indice] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())

                        indice = 10
                        print(f"{SUCCESS}El producto ha sido ingresado con éxito{NORMAL}")
                        time.sleep(0.7)
                    indice += 1  
                
                time.sleep(1.5)
                user_menu_TP2.clear_shell()
                
        
                print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
                option = input_validation_TP2.check_int()
                if option == 1 and productos[2] != "":
                    print(f"{WARNING}Se ha alcanzado la cantidad maxima de productos (3){NORMAL} ")
                    option = 0
                    time.sleep(1.5)
            else:
                print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
                option = input_validation_TP2.check_int()


def consulta(productos):
    user_menu_TP2.clear_shell()    
    if productos[0] == "":#como el array se llena del 0 al 2 si el primero es 0 es porque esta vacía
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else:
        indice = 0
        print("La actual lista de productos es:\n*-------------------------------*")
        while indice <3:
            if productos[indice] != "":
                print("|{:^3}| {:25} |".format(indice+1, productos[indice]))
            indice +=1
        print("| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")

def baja(productos):
    user_menu_TP2.clear_shell()
    if productos[0] == "":
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else: 
        consulta(productos)# como la lista no está vacía, llamo a consulta para que la imprima
        option = input_validation_TP2.check_int()
        
        while option != 0:
            while 0 > option or option > 4 or productos[option-1] == "": # me fijo si la opcion no esta en el rango o si la opcion esta vacia
                print(f"{WARNING}Ingrese un producto existente{NORMAL}") 
                option = input_validation_TP2.check_int()
            else:
                    option -= 1
                    if option == 2:
                        productos[option] = ""
                    elif option == 0:
                        productos[option] = productos[option + 1]
                        productos[option + 1] = productos[option + 2]
                        productos[option + 2] = ""
                    else:
                        productos[option] = productos[option + 1]
                        productos[option + 1] = ""
                    print(f"{SUCCESS}El producto ha sido eliminado{NORMAL}")
                    time.sleep(1.5)
                    if productos[0] == "":
                        print(f"{WARNING}No hay más productos ingresados. Volverá al menu anterior.{NORMAL}")
                        time.sleep(1.5)
                        option = 0
                    else: 
                        user_menu_TP2.clear_shell()
                        consulta(productos)# como la lista no está vacía, llamo a consulta para que la imprima
                        option = input_validation_TP2.check_int()
    
                    
def modificacion(productos):
    user_menu_TP2.clear_shell()
    i = 0
    if productos[0] == "":
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
                    productos[option - 1] = input_validation_TP2.check_producto(input("Ingrese el nombre del nuevo nombre del producto en cuestión. Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz\n").upper())
                    if option == 3: 
                            while productos[2] == productos[0] or productos[2] == productos [1]:
                                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                productos[option-1] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada ,Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())
                    elif option == 2:
                        while productos[1] == productos[0] or productos[1] == productos[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            productos[option-1] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())
                    elif option == 1:
                        while productos[0] == productos[1] or productos[0] == productos[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            productos[option-1] = input_validation_TP2.check_producto(input("(Las opciones valida de producto son: Cebada, Arroz, Trigo, Soja, Maiz)\nIngrese un producto: ").upper())

                    print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                    time.sleep(1.5)
                    consulta(productos)
                    option = input_validation_TP2.check_int()#muestro la lista actualizada de productos