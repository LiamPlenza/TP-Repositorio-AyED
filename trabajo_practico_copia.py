from calendar import c
import os
import string
c = 0
def menu_principal():
    return print("1 - Adminitraciones \n2 - Entrega de Cupos \n3 - Recepcion \n4 - Registrar Calidad \n5 - Registrar Peso Bruto \n6 - Registrar Descarga \n7 - Registrar Tara \n8 - Reportes \n0 - Salir del programa \n")

def menu_administraciones():
    clear_shell()
    print("1 - Titulares \n2 - Productos \n3 - Rubros \n4 - Rubros x Productos \n5 - Silos \n6 - Sucursales \n7 - Producto por Titular \n0 - Volver al menu principal")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if 1 == option :
            menu_opciones()
        elif option != 0 and option > 8:
            print("Esta Función está en desarrollo")
            #poner la funcion para el enter para continuar
            menu_administraciones()
        elif option == 0:
            menu_principal()
        else:
            print("La opcion elegida no se encuentra entre las dadas imbecil. Rompiste todo ")    

def menu_opciones():
    clear_shell()
    titulares = [str]
    print("1 - Alta \n2 - Baja \n3 - Consulta \n4 - Modificación \n0 - Volver al menu anterior ")
    my_dict_funciones = {
        1: alta,
        2: baja,
        3: consultar,
        4: modificacion,
        0: volver_al_menu
    }
    
#def alta(titulares):
#    titulares[c]= input("Ingrese el nombre del titular" )
#    c= c+1
#    #poner lo del enter para continuar
#    menu_opciones()

#def baja(titulares):
#        titularF = input("Ingrese el nombre del titular a eliminar")
#        co = 0
#        while co < c:
#            if titulares[c] == titularF:
#                pass
#            else:
#                co= co +1
        
#def consultar(titulares):
#    titularF = input("Ingrese el nombre del titular a consultar")
#    co = 0
#    while co < c:
#        if titulares[c] == titularF:
#            print("El titular se encuentra en el sistema")
#            menu_opciones()
#        else:
#            co= co + 1
#            if co==c:
#                print("El titular no se encuentra en el sistema")
#                menu_opciones()

#def modificacion(titulares):
#    pass

def volver_al_menu():
    menu_principal()

    option = int(input("Seleccione una opción del menu: "))

def menu_recepcion():
    camtot = 0
    camsojtot = 0
    cammaiztot = 0
    pnsojtot = 0
    pnmaiztot = 0    

    print("1 - Ingresar nuevo camión/n2 - Volver")
    my_dict_recepciones = {
        1: ingresar_camión,
        2: volver_al_menu()
    }

    option = int(input("Seleccione una opción del menu: "))

    while option != 2:
        my_dict_recepciones.get(option, lambda: print("Seleccion una opción afuera"))
        if option == 1:
            print("Ingrese los datos del camión:")
            camion[1](input("Ingrese la patente:"))
            camion[2](input("Ingrese la el producto que carga:"))
            camion[3](input("Ingrese el peso bruto del camión:"))
            camion[4](input("Ingrese la tara del camión:"))
        
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
wardo sos cagon

    print("Salio")
