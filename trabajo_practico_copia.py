from asyncio.windows_events import NULL
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

    #titulares = [str]
    #my_dict_funciones = {
    #    1: alta,
    #    2: baja,
    #    3: consultar,
    #    4: modificacion,
    #    0: volver_al_menu
    #}
    
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

def menu_recepcion():
    clear_shell()
    print("0 - Volver al menu anterior\n1 - Ingresar un nuevo camion")
    
    option = int(input("Seleccione una opción del menu: "))
    while option != 0:
        if option == 1:
            ingreso_de_datos()
        elif option == 74:
            print(" grrr Felicidades! Encontró un easter egg, vamos la lepra")
        else:
            print("Ingrese una opción valida del menu... Imbecil")
            time.sleep(2) 
        menu_recepcion()


pesoMayorSoja = 0
pesoMenorMaiz = 0

def ingreso_de_datos():
    tipoCamion = input ("Ingrese si el camion contiene Soja o Maíz").upper()
    tara = float(input ("Ingrese la tara del camión"))
    pesoBruto = float(input ("Ingrese el peso bruto del camión"))
    patCamion = input("Ingrese la patente: ").upper()
    pesoNeto = pesoBruto - tara
    print("El peso neto del camión ingresado es",pesoNeto)
    time.sleep(2)
    if tipoCamion == "SOJA":
        camionSoja= camionSoja + 1
        pesoNetoSoja = pesoNetoSoja + pesoNeto
        promPesoNetoS = pesoNetoSoja / camionSoja
        if pesoNetoSoja > pesoMayorSoja:
            pesoMayorSoja = pesoNetoSoja
            patMayorSoja = patCamion
    elif tipoCamion == "MAIZ":
        camionMaiz = camionMaiz + 1
        pesoNetoMaiz = pesoNetoSoja + pesoNeto
        promPesoNetoM = pesoNetoMaiz / camionMaiz
        if pesoNetoMaiz < pesoMenorMaiz:
            pesoMenorMaiz = pesoNetoMaiz
            patMenorMaiz = patCamion
    else: 
        print("Ingrese un Proucto valido")
        ingreso_de_datos()
    cantCamion= cantCamion + 1

def menu_reportes():
    print("0 - Volver al menu anterior\n1 - Msotrar el reporte actual")
    
    option = int(input("Seleccione una opción del menu: "))
    if option == 0:
        menu_principal()
    elif option == 1:
        mostrar_reporte()
    else:
        print("Ingrese una opcion válida")
        clear_shell()
        menu_reportes()
def mostrar_reporte():
    pass
# para determinar el sistema operativo y limpiar la consola
def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

#vamoslalepra
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
