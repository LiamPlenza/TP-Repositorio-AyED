import os
def menu_principal():
    return print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            menu_terciario()    
nicococo
def menu_terciario():
    clear_shell()
    print("1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación \n0 - Volver al menu anterior ")
    option = int(input("Seleccione una opción del menu: "))

def menu_recepcion():
    pass

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
        2: menu_recepcion
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
        #    print("Esta funcionalidad está en construcción \n")
        
        menu_principal()
        option = int(input("Seleccione una opción del menu: "))

    print("Salio")
