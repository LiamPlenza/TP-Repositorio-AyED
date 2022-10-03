import os, time, input_validation_TP3, user_menu_TP3, main_TP3, pickle, io, os.path
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'


def alta(abm_list, menu):
    if menu == "productos":# open(primer parametro, segundo parametro) --> primer parametro: ruta del archivo, segundo parametro: modo de apertura
        registro = main_TP3.Productos()
        if os.path.exist("PRODUCTOS.dat"):
            archivo_logico = open("PRODUCTOS.dat", "r+b")
            longitud_archivo = os.path.getsize("PRODUCTOS.dat")
            
            while archivo_logico.tell() < longitud_archivo:
                registro = pickle.load(archivo_logico)

                codprod_ingresado = input("Ingrese el codigo del producto: "))
                while registro.codprod == codprod_ingresado:
                    print(f"{WARNING}Ya existe ese codigo de producto. Le corresponde al producto: {registro.nomprod}{NORMAL}")
                    codprod_ingresado = int(input("Ingrese el codigo del producto: "))
                registro.codprod = codprod_ingresado

                nomprod_ingresado = input(f"Ingrese el nombre del producto, codigo: {registro.codprod}")
                while registro.nomprod == nomprod_ingresado:
                    print(f"{WARNING}Ya existe ese nombre de producto. Le corresponde al producto con el código: {registro.codprod}{NORMAL}")
                    codprod_ingresado = input("Ingrese el nombre del producto: ")
                registro.nomprod = nomprod_ingresado    
        else:
            archivo_logico = open("PRODUCTOS.dat", "w+b")
            codprod_ingresado = input_validation_TP3.check_int(input("Ingrese el codigo del producto: "))
            
            registro.codprod = input_validation_TP3.check_int(("Ingrese el codigo del producto: "))
            registro.nomprod = input("Ingrese el nombre del producto: ")
        
        registro.nomprod = registro.nomprod.ljust(20) # ajusto todos los string a la misma longitud
    
    elif menu == "rubros":
        registro = main_TP3.Rubros()
        if os.path.exist("RUBROS.dat"):
            archivo_logico = open("RUBROS.dat", "r+b")
            longitud_archivo = os.path.getsize("RUBROS.dat")
            
            codrub_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro: "))
            nomrub_ingresado = input(f"Ingrese el nombre del rubro, codigo: {registro.codrub}")
            
            while archivo_logico.tell() < longitud_archivo:
                registro = pickle.load(archivo_logico)

                while registro.codrub == codrub_ingresado:
                    print(f"{WARNING}Ya existe ese codigo de rubro. Le corresponde al rubro: {registro.nomrub}{NORMAL}")
                    codrub_ingresado = int(input("Ingrese el codigo del producto: "))
                    archivo_logico.seek(io.SEEK_SET)

                while registro.nomrub == nomrub_ingresado:
                    print(f"{WARNING}Ya existe ese nombre de rubro. Le corresponde al código: {registro.codrub}{NORMAL}")
                    codprod_ingresado = input("Ingrese el nombre del producto: ")
                    archivo_logico.seek(io.SEEK_SET)
            
            registro.nomrub = nomrub_ingresado    
            registro.codrub = codrub_ingresado
        else:
            archivo_logico = open("RUBROS.dat", "w+b")
            
            registro.codprod = input_validation_TP3.check_int(("Ingrese el codigo del rubro: "))
            registro.nomrub = input("Ingrese el nombre del rubro: ")
        
        registro.nomrub = registro.nomrub.ljust(20) # ajusto todos los string a la misma longitud
            
    elif menu == "rubros por productos":
        registro = main_TP3.RubrosxProducto()
        if os.path.exist("RUBROX-X-PRODUCTOS.dat"):
            archivo_logico = open("RUBROX-X-PRODUCTOS.dat", "r+b")
            longitud_archivo = os.path.getsize("RUBROX-X-PRODUCTOS.dat")
            
            while archivo_logico.tell() < longitud_archivo:
                registro = pickle.load(archivo_logico)

                codrubx_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro: "))
                while registro.codrubx == codrubx_ingresado:
                    print(f"{WARNING}Ya existe ese codigo de rubro. Le corresponde al rubro: {registro.nomrubx}{NORMAL}")
                    codrubx_ingresado = int(input("Ingrese el codigo del producto: "))
                registro.codrubx = codrubx_ingresado

                nomrubx_ingresado = input(f"Ingrese el nombre del producto, codigo: {registro.nomrubx}")
                while registro.nomrubx == nomrubx_ingresado:
                    print(f"{WARNING}Ya existe ese nombre de rubro. Le corresponde al código: {registro.codrubx}{NORMAL}")
                    codprod_ingresado = input("Ingrese el nombre del producto: ")
                registro.nomrubx = nomrubx_ingresado    
        else:
            archivo_logico = open("RUBROX-X-PRODUCTOS.dat", "w+b")
            
            registro.codrubx = input_validation_TP3.check_int(("Ingrese el codigo del rubro: "))
            registro.nomrubx = input("Ingrese el nombre del rubro: ")
        
        valor_maximo_ingresado = float(input(f"Ingrese el valor mámixo correspondiente al rubro ({registro.codrubx}, {registro.codprodx})\nRecuerde que debe ser un valor menor a 100"))
        while valor_maximo_ingresado < 100:
            valor_maximo_ingresado = float(input(f"{WARNING}El valor máximo no puede ser mayor a 100.{NORMAL}\nIngrese el valor mámixo correspondiente al rubro ({registro.codrubx}, {registro.codprodx})"))
        
        valor_minimo_ingresado = float(input(f"Ingrese el valor mínimo correspondiente al rubro ({registro.codrubx}, {registro.codprodx})\nRecuerde que debe ser un valor mayor a 0"))
        while valor_minimo_ingresado < 0:
            valor_maximo_ingresado = float(input(f"{WARNING}El valor mínimo no puede ser menor a 0.{NORMAL}\nIngrese el valor mínimo correspondiente al rubro ({registro.codrubx}, {registro.codprodx})"))
            
        registro.vmin = valor_minimo_ingresado
        registro.vmax = valor_maximo_ingresado
        registro.nomprod = registro.nomprod.ljust(20) # ajusto todos los string a la misma longitud
        
    elif menu == "silos":
        if os.path.exist("SILOS.dat"):
            archivo_logico = open("SILOS.dat", "r+b")
        else:
            archivo_logico = open("SILOS.dat", "w+b")
        registro = main_TP3.Silos()

        registro.codsil = input("Ingrese el codigo del silo:")
        registro.nomsil = input("Ingrese el nombre del silo:")
        registro.codprods = input("Ingrese el codigo del producto:")
        registro.stock = input("Ingrese el stock:")
        
        
            
    #registro = pickle.load(archivo_logico) # traigo 
    pickle.dump(registro, archivo_logico) # guardo un regristro 
    archivo_logico.flush() # aeguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo
                
def consulta(abm_list):
    user_menu_TP3.clear_shell()
    if os.path.exist("PRODUCTOS.dat"):
        archivo_logico = open("PRODUCTOS.dat", "r+b")
    else:
        archivo_logico = open("PRODUCTOS.dat", "w+b")
    
    registro = main_TP3.Productos()
    registro = archivo_logico.load()
    longitud_archivo = os.path.getsize("PRODUCTOS.dat")

    if registro.nomprod == "":
        print(f"{WARNING}No se ha cargado ningun producto.{NORMAL}")
        time.sleep(1.5)
    else:
        print("La actual lista de Productos es:\n*-------------------------------*")
        while archivo_logico.tell() < longitud_archivo:
            registro = archivo_logico.load()
            print("|{:^3}| {:25} |".format(registro.codprod, registro.nomprod))
        print("| 0 | Volver al menu anterior   |\n*-------------------------------*")
        input("Precione enter para continuar... ")
    archivo_logico.flush() # aeguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo       
                
def baja():
    user_menu_TP3.clear_shell()
    user_menu_TP3.clear_shell()
    if os.path.exist("PRODUCTOS.dat"):
        archivo_logico = open("PRODUCTOS.dat", "r+b")
    else:
        archivo_logico = open("PRODUCTOS.dat", "w+b")
    
    registro = main_TP3.Productos()
    registro = archivo_logico.load()
    longitud_archivo = os.path.getsize("PRODUCTOS.dat")

    
    
    
    
    if abm_list[0] == "":
        print(f"{WARNING}No hay abm_list ingresados{NORMAL}")
        time.sleep(1.5)
    else: 
        consulta()# como la lista no está vacía, llamo a consulta para que la imprima
        option = input_validation_TP3.check_int()
        
        while option != 0:
            while 0 > option or option > 4 or abm_list[option-1] == "": # me fijo si la opcion no esta en el rango o si la opcion esta vacia
                print(f"{WARNING}Ingrese un producto existente{NORMAL}") 
                option = input_validation_TP3.check_int()
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
                        user_menu_TP3.clear_shell()
                        consulta(abm_list)# como la lista no está vacía, llamo a consulta para que la imprima
                        option = input_validation_TP3.check_int()


def modificacion():
    user_menu_TP3.clear_shell()
    i = 0
    if abm_list[0] == "":
        print(f"{WARNING}No hay abm_list ingresados{NORMAL}")
        time.sleep(1.5)
    else:# como el array de abm_list no está vacía la función consulta va a mostrar el array completo
        consulta()
        option = input_validation_TP3.check_int()
    
        while option != 0:
            if abm_list[option-1] == "":
                print(f"{WARNING}Ingrese un titular existente{NORMAL}")
                option = input_validation_TP3.check_int() 
            else:
                if abm_list[option - 1] == 0:
                    print(f"{WARNING}No es posible modificar un elemento que está vacio{NORMAL}")
                else:
                    abm_list[option - 1] = input_validation_TP3.check_producto()
                    if option == 3: 
                            while abm_list[2] == abm_list[0] or abm_list[2] == abm_list [1]:
                                print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                                abm_list[option-1] = input_validation_TP3.check_producto()
                    elif option == 2:
                        while abm_list[1] == abm_list[0] or abm_list[1] == abm_list[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            abm_list[option-1] = input_validation_TP3.check_producto()
                    elif option == 1:
                        while abm_list[0] == abm_list[1] or abm_list[0] == abm_list[2]:
                            print(f"{WARNING}El producto ya ha sido ingresado. Elija otro de la lista {NORMAL}")
                            abm_list[option-1] = input_validation_TP3.check_producto()
                    print(f"{SUCCESS}El titular {option} ha sido actualizado{NORMAL}")
                    time.sleep(1.5)
                    consulta(abm_list)
                    option = input_validation_TP3.check_int()#muestro la lista actualizada de abm_list