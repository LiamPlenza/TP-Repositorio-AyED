import os, time
def menu_principal():
    clear_shell()
    return print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1 :
            menu_opciones()
        elif 1 < option < 8:
            print("Esta Función está en desarrollo...")
            time.sleep(2)
            menu_administraciones()
        else:
            print("La opcion elegida no se encuentra entre las dadas imbecil. Rompiste todo ")  
            time.sleep(2)
            menu_administraciones()  

def menu_opciones():
    clear_shell()
    print("0 - Volver al menu anterior \n1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if 1 <= option <= 4:
            print("Esta Función está en desarrollo...")
        else:
            print("La opcion elegida no se encuentra entre las dadas imbecil. Rompiste todo ")  
        time.sleep(2)
        menu_opciones()

def menu_recepcion():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            print("ingreso de datos")
        else:
            print("Ingrese una opción valida del menu... Imbecil")
            time.sleep(2) 
        menu_recepcion()
        
def menu_reportes():
    pass

# para determinar el sistema operativo y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

if __name__ == "__main__":
    menu_principal()
    option = int(input("Seleccione una opción del menu: "))
    
    #diccionario con las opciones y las funciones correspondientes
    my_dict = {
        1: menu_administraciones,
        3: menu_recepcion,
        8: menu_reportes
    }

    while option != 0:
        #busca la llave correspondiente a la opcion, si existe llama a la funcion sino ejecuta lambda -> reemplaza los if
        my_dict.get(option, lambda: print("Esta funcionalidad está en construcción"))()

        #if option == 1:
        #    menu_administraciones()
        #elif option == 3:
        #    menu_recepcion()
        #elif option == 8:
        #    menu_reportes
        #else:
        # 3
        # 3   print("Esta funcionalidad está en construcción \n")
        
        menu_principal()
        option = int(input("Seleccione una opción del menu: "))
    print("Salio")
