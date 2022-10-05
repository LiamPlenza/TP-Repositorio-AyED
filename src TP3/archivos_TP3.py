import os, time, pickle, io, os.path
import input_validation_TP3, user_menu_TP3, main_TP3

# COLORES
WARNING = '\033[1;31m'
SUCCESS = '\033[1;32m'
NORMAL = '\033[0m'

def alta(menu):
    posicion = 0
    if menu == "productos":# open(primer parametro, segundo parametro) --> primer parametro: ruta del archivo, segundo parametro: modo de apertura
        registro = main_TP3.Productos()
        if os.path.exists("PRODUCTOS.dat"):
            archivo_logico = open("PRODUCTOS.dat", "r+b")
            longitud_archivo = os.path.getsize("PRODUCTOS.dat")

            archivo_logico.seek(longitud_archivo - 100) # para posicionarme al incio del último registro
            registro = pickle.load(archivo_logico) # ultimo registro ingresado
            codactual = registro.codprod + 1 # incremento el codigo

            nomprod_ingresado = input(f"Ingrese el nombre del producto cuyo codigo es {codactual}: ").capitalize().ljust(20)
            archivo_logico.seek(io.SEEK_SET) # me muevo al inicio del archivo
            while archivo_logico.tell() < longitud_archivo:
                registro = pickle.load(archivo_logico)# traigo el primer registro

                if registro.nomprod == nomprod_ingresado:
                    print(f"{WARNING}Ya existe este producto. A este producto le corresponde el código: {registro.codprod}{NORMAL}")
                    if not registro.activo:
                        print("Desea reactivar el producto? [0]-Si [1]-No")
                        reactivar = input_validation_TP3.check_int()
                        if reactivar == 0:
                            codactual = registro.codprod
                            nomprod_ingresado = registro.nomprod
                            posicion = longitud_archivo - (longitud_archivo - (registro.codprod-1)*100)# me posicion en el registro a modificar, cada registro pesa 100 por ende si tengo un archivo de 300 y quiero el segundo registro me tengo que para en el 100
                        else:
                            nomprod_ingresado = input(f"Ingrese el nombre del producto cuyo codigo es {codactual}: ").capitalize().ljust(20)
                            archivo_logico.seek(io.SEEK_SET)# me vuelvo a mover al inicio
                    else:    
                        nomprod_ingresado = input(f"Ingrese el nombre del producto cuyo codigo es {codactual}: ").capitalize().ljust(20)
                        archivo_logico.seek(io.SEEK_SET)# me vuelvo a mover al inicio
        else:
            archivo_logico = open("PRODUCTOS.dat", "w+b")            
            codactual = 1
            nomprod_ingresado = input("Ingrese el nombre del primer producto: ").capitalize().ljust(20)
        
        registro.codprod = codactual # guardo el codigo
        registro.nomprod = nomprod_ingresado
        registro.activo = True
        if posicion != 0:
            archivo_logico.seek(posicion)

    elif menu == "rubros":
        registro = main_TP3.Rubros()
        if os.path.exists("RUBROS.dat"):
            archivo_logico = open("RUBROS.dat", "r+b")
            longitud_archivo = os.path.getsize("RUBROS.dat")
            
            archivo_logico.seek(longitud_archivo - 85) # para posicionarme al incio del último registro
            registro = pickle.load(archivo_logico)
            codactual = registro.codrub + 1
            
            nomrub_ingresado = input(f"Ingrese el nombre del rubro cuyo código es {codactual}: ").capitalize().ljust(20)
            archivo_logico.seek(io.SEEK_SET) # me muevo al inicio del archivo
            while archivo_logico.tell() < longitud_archivo:
                registro = pickle.load(archivo_logico)

                if registro.nomrub == nomrub_ingresado:
                    print(f"{WARNING}Ya existe ese nombre de rubro. Le corresponde al código: {registro.codrub}{NORMAL}")
                    nomrub_ingresado = input(f"Ingrese el nombre del rubro cuyo código es {codactual}: ").capitalize().ljust(20)
                    archivo_logico.seek(io.SEEK_SET)    
        else:
            archivo_logico = open("RUBROS.dat", "w+b")
            
            codactual = 1
            nomrub_ingresado = input("Ingrese el nombre del primer rubro: ").capitalize().ljust(20)
            
        registro.codrub = codactual
        registro.nomrub = nomrub_ingresado

    elif menu == "rubros por productos":
        
        registro = main_TP3.RubrosxProducto()
        registro_r = main_TP3.Rubros()
        registro_p = main_TP3.Productos()
        if os.path.exist("PRODUCTOS.dat") and os.path.exists("RUBROS.dat"):

            if os.path.exist("RUBROS-X-PRODUCTO.dat"):
                archivo_logico = open("RUBROS-X-PRODUCTO.dat", "r+b")
                archivo_logico_r = open("RUBROS.dat", "r+b")
                archivo_logico_p= open("PRODUCTOS.dat", "r+b")
                longitud_archivo_rxp = os.path.getsize("RUBROS-X-PRODUCTO.dat")

                
                
                codrub_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro: "))
                registro_r = pickle.load(archivo_logico_r)
                while codrub_ingresado > registro_r.codrub or codrub_ingresado < 1:
                    codrub_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro (tiene que ser mayor a 0 y menor a ",registro_r.codrub,"): "))

                codprod_ingresado = input_validation_TP3.check_int(input("Ingrese el código del producto: "))
                
                registro_p = pickle.load(archivo_logico_p)
                while codrub_ingresado > registro_p.codprod or codprod_ingresado < 1:
                    codprod_ingresado = input_validation_TP3.check_int(input("Ingrese el código del producto (tiene que ser mayor a 0 y menor a ",registro_p.codprod,"): "))

                
                while archivo_logico.tell() < longitud_archivo_rxp:
                    registro = pickle.load(archivo_logico)

                    if registro.codrub == codrub_ingresado:
                        
                        if registro.codprod == codprod_ingresado:
                            print(f"{WARNING}Ya existe esa combinacion de rubro y producto{NORMAL}")
                            codrub_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro: "))
                            registro_r = pickle.load(archivo_logico_r)
                            while codrub_ingresado > registro_r.codrub or codrub_ingresado < 1:
                                codrub_ingresado = input_validation_TP3.check_int(input("Ingrese el código del rubro (tiene que ser mayor a 0 y menor a ",registro_r.codrub,"): "))
                            codprod_ingresado = input_validation_TP3.check_int(input("Ingrese el código del producto: "))
                            registro_p = pickle.load(archivo_logico_p)
                            while codrub_ingresado > registro_p.codprod or codprod_ingresado < 1:
                                codprod_ingresado = input_validation_TP3.check_int(input("Ingrese el código del producto (tiene que ser mayor a 0 y menor a ",registro_p.codprod,"): "))
                        archivo_logico.seek(io.SEEK_SET)

                registro.codprod = codprod_ingresado
                registro.codrub = codrub_ingresado
            else:
                archivo_logico = open("RUBROS-X-PRODUCTO.dat", "w+b")
                
                registro.codrub = input_validation_TP3.check_int(("Ingrese el codigo del rubro: "))
                registro.codprod = input_validation_TP3.checkint(input("Ingrese el codigo del producto: "))
            
            valor_maximo_ingresado = float(input(f"Ingrese el valor mámixo correspondiente al rubro ({registro.codrub}, {registro.codprod})\nRecuerde que debe ser un valor menor a 100"))
            while valor_maximo_ingresado > 100:
                valor_maximo_ingresado = float(input(f"{WARNING}El valor máximo no puede ser mayor a 100.{NORMAL}\nIngrese el valor mámixo correspondiente al rubro ({registro.codrub}, {registro.codprod})"))
            
            valor_minimo_ingresado = float(input(f"Ingrese el valor mínimo correspondiente al rubro ({registro.codrub}, {registro.codprod})\nRecuerde que debe ser un valor mayor a 0"))
            while valor_minimo_ingresado < 0:
                valor_maximo_ingresado = float(input(f"{WARNING}El valor mínimo no puede ser menor a 0.{NORMAL}\nIngrese el valor mínimo correspondiente al rubro ({registro.codrub}, {registro.codprod})"))
                
            registro.vmin = valor_minimo_ingresado
            registro.vmax = valor_maximo_ingresado        
            pickle.dump(registro, archivo_logico) # guardo un regristro 
            archivo_logico.flush() # aeguro que no quede pendiente ningún registro en el bus
            archivo_logico.close()# cierro el archivo
        else:
            print(f"{WARNING}Para ingresar un rubro x producto debe haber al menos 1 producto y un rubro ingresados{NORMAL}")

    elif menu == "silos":

        registro = main_TP3.Silos()
        registro_p = main_TP3.Productos()
        if os.path.exist("PRODUCTOS.dat"):
            if os.path.exist("SILOS.dat"):
                archivo_logico = open("SILOS.dat", "a+b")
                archivo_logico_p= open("PRODUCTOS.dat", "a+b")


            else:
                archivo_logico = open("SILOS.dat", "w+b")
                archivo_logico_p= open("PRODUCTOS.dat", "r+b")
                registro_p = pickle.load(archivo_logico_p)
                ult = registro_p.codprod
                registro.codsil = 1
                registro.nomsil = input("Ingrese el nombre del silo:")
                registro.codprods = input("Ingrese el codigo del producto:")
                while registro.codprods < 1 or registro.codprods > ult:
                    registro.codprods = input(f"{WARNING}El codigo del producto no se encuentra ingresado.{NORMAL}\nIngrese un codigo entre 1 y {ult}:")
                registro.stock = input("Ingrese el stock:")
                while registro.stock < 0:
                    registro.stock = input(f"{WARNING}El stock no puede ser negativo{NORMAL}\nIngrese el stock:")
        else:
            print(f"{WARNING}Para ingresar un silo debe haber al menos 1 producto ingresado{NORMAL}")
            
    pickle.dump(registro, archivo_logico) # guardo el regristro en el archivo 
    archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
    archivo_logico.close()# cierro el archivo
    print(f"{SUCCESS}El registro ha sido guardado con exito{NORMAL}")
                    
def consulta():
    user_menu_TP3.clear_shell()
    if os.path.exists("PRODUCTOS.dat"):
        if input_validation_TP3.check_producto():
            registro = main_TP3.Productos()
            archivo_logico = open("PRODUCTOS.dat", "rb")
            longitud_archivo = os.path.getsize("PRODUCTOS.dat")

            print("La actual lista de Productos es:")
            print("----------------------------------------\n| {} | {:20} | {} |\n*----------------------------------------*".format("Código", "Nombre", "Estado"))
            while archivo_logico.tell() < longitud_archivo:# recorro todo el archivo
                registro = pickle.load(archivo_logico)# traigo el primer registro
                print("   {:^3}   | {:20} | {}".format(registro.codprod, registro.nomprod, registro.activo))
                print("----------------------------------------")

            archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus
            archivo_logico.close()# cierro el archivo       
            print("|   0    | Volver al menu anterior       |\n*----------------------------------------*")
            input("Precione enter para continuar... ")
        else:
            print(f"{WARNING}Todos los registros se encuentran desactivados. Para activarlos dirigase al menu ALTA{NORMAL}")
            time.sleep(1.5)
    else:
        print(f"{WARNING}No se ha cargado ningun producto.{NORMAL}")
        time.sleep(1.5)
        
def baja():
    user_menu_TP3.clear_shell()
    if input_validation_TP3.check_producto():
        consulta() # imprimo la lista actual de productos
        option = input_validation_TP3.check_int()
        
        registro = main_TP3.Productos()
        archivo_logico = open("PRODUCTOS.dat", "r+b")
        longitud_archivo = os.path.getsize("PRODUCTOS.dat")
        
        archivo_logico.seek(longitud_archivo - 100) # para posicionarme al inico del último registro
        registro = pickle.load(archivo_logico)
        ultimo_registro = registro.codprod
        
        if option != 0:
            while option not in [x for x in range(1, ultimo_registro+1)]: # me fijo si el código ingresado del producto a eliminar está entre 1 y el último codigo de producto
                print(f"{WARNING}La opción elegida no se encuentra entre las dadas{NORMAL}")
                option = input_validation_TP3.check_int()

            archivo_logico.seek(longitud_archivo - (longitud_archivo - (option-1)*100))# me posicion en el registro a modificar, cada registro pesa 100 por ende si tengo un archivo de 300 y quiero el segundo registro me tengo que para en el 100
            posicion = archivo_logico.tell()# guardo la posición del registro antes de avanzar
            registro = pickle.load(archivo_logico)# traigo el registro el archivo
            
            if not registro.activo:
                print(f"{WARNING}El registro seleccionado se encuentra desactivado{NORMAL}")
            else:
                registro.activo = False
                archivo_logico.seek(posicion) # me muevo a la posición del registro a modificar
                pickle.dump(registro, archivo_logico) # lo actualizo
                archivo_logico.flush() # me aseguro que no quede pendiente ningún registro en el bus

                print(f"{SUCCESS}El registro ha sido actualizado con exito{NORMAL}")
                
        archivo_logico.close()# cierro el archivo
    else:
        print(f"{WARNING}Todos los registros se encuentran desactivados. Para activarlos dirigase al menu ALTA{NORMAL}")
        time.sleep(1.5)

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