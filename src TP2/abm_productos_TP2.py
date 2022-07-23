import os, time, input_validation_TP2, user_menu_TP2
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'

def alta(productos):
    user_menu_TP2.clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
    option = input_validation_TP2.check_int()
    while option != 0:
        indice = 0
        if option == 1:
            if "" in productos:
                while indice < len(productos):
                    if productos[indice] == "":#si encuentra un espacio vacio en producto lo agrego
                        producto_ingresado = input_validation_TP2.check_producto()
                        while producto_ingresado in productos:# si el producto ya fue ingresado hago que ingrese otro hasta que no se encuentre en la lista
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            producto_ingresado = input_validation_TP2.check_producto()
                        productos[indice] = producto_ingresado# guardo el producto
                        indice = 10 # hago que salga del ciclo
                        print(f"{SUCCESS}El producto ha sido ingresado con éxito{NORMAL}")
                    indice += 1  
            else:
                print(f"{WARNING}Se ha alcanzado la cantidad maxima de productos (3){NORMAL} ")
        else:
            print(f"{WARNING}La opcion elegida no se encuentra entre las dadas. Pruebe de nuevo{NORMAL}")
            option = input_validation_TP2.check_int()
        
        time.sleep(1.5)
        user_menu_TP2.clear_shell()
        print("0 - Volver al menu anterior\n1 - Ingresar un nuevo producto")
        option = input_validation_TP2.check_int()

def consulta(productos):
    user_menu_TP2.clear_shell()    
    if productos[0] == "":#como el array se llena del 0 al 2 si el primero es 0 es porque esta vacía
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        time.sleep(1.5)
    else:
        indice = 0
        print("La actual lista de productos es:\n*-------------------------------*")
        #for indice, producto in enumerate(productos):
        #    if productos[indice] != "":
        #        print("|{:^3}| {:25} |".format(indice+1, producto))
        while indice < len(productos):
            if productos[indice] != "":
                print("|{:^3}| {:25} |".format(indice+1, productos[indice]))
            indice +=1
        print("*-------------------------------*\n| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")

"""
    Ver como reacomodar la lista de una mejor manera
"""
def baja(productos):
    user_menu_TP2.clear_shell()
    if productos[0] == "":
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
    else: 
        consulta(productos)# como la lista no está vacía, llamo a consulta para que la imprima
        option = input_validation_TP2.check_int()
        
        while option != 0:
            while option not in [x for x in range(1, len(productos)+1)] or productos[option-1] == "":# me fijo si la opcion no esta en el rango o si la opcion esta vacia
                print(f"{WARNING}Ingrese un producto existente{NORMAL}") 
                option = input_validation_TP2.check_int()
        
            option -= 1 # resto uno a la posición ingresada, ya que internamente va de 0 a 2
            
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
                option = 0 # hago que salga del ciclo
            else: 
                user_menu_TP2.clear_shell()
                consulta(productos)# como la lista no está vacía, llamo a consulta para que la imprima
                option = input_validation_TP2.check_int()
                     
def modificacion(productos):
    user_menu_TP2.clear_shell()

    if productos[0] == "":
        print(f"{WARNING}No hay productos ingresados{NORMAL}")
        #time.sleep(1.5)
    else:# como el array de productos no está vacía la función consulta va a mostrar el array completo
        consulta(productos)
        option = input_validation_TP2.check_int()
    
        while option != 0:
            while option not in [x for x in range(1, len(productos)+1)] or productos[option-1] == "": # me fijo si la opcion seleccionada NO está en una lista [1...opcion], o es una opción vacía
                print(f"{WARNING}Ingrese un titular existente{NORMAL}")
                option = input_validation_TP2.check_int() 
                
            producto_ingresado = input_validation_TP2.check_producto()
            while producto_ingresado in productos:# si el producto ya fue ingresado hago que ingrese otro hasta que no se encuentre en la lista
                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                producto_ingresado = input_validation_TP2.check_producto()
            productos[option - 1] = producto_ingresado# guardo el producto
            print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                    
            time.sleep(1.5)
            consulta(productos)# muestro la lista actualizada de productos
            option = input_validation_TP2.check_int()