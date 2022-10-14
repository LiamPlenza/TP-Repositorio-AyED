import main_TP3, io, pickle, os, input_validation_TP3

WARNING = '\033[1;31m'
NORMAL = '\033[0m'

def clear_shell():
    if os.name ==  "nt":
        return os.system("cls")
    else:
        return os.system("clear")

def menu_reportes():
    clear_shell()
    print("0 - Volver al menu anterior \nEl reporte actual es: ")
    
    codprod = [[],[],[],[],[]] # nombre del silo, codigo del producto, cantidad de camiones, cantidad de stock
    cant_cupos_otorgados = 0
    cant_camiones_recibidos = 0
    mayor_stock = 0
    nombre_silo_mayor_stock = ""
    patentes_rechazadas = []
    
    fecha_ingresada = input_validation_TP3.check_fecha("reportes").ljust(8)
        
    if os.path.exists("OPERACIONES.dat"):
        registro_silos = main_TP3.Silos()
        registro_operaciones = main_TP3.Operaciones()
        archivo_logico_silos = open("SILOS.dat", "rb") # no verifico la existencia del archivo silos porque si se ingresa un camion al menos un silo debe existir
        archivo_logico_operaciones = open("OPERACIONES.dat", "rb")
        longitud_silos = os.path.getsize("SILOS.dat")
        longitud_operaciones = os.path.getsize("OPERACIONES.dat")
        
        while archivo_logico_silos.tell() < longitud_silos:
            registro_silos = pickle.load(archivo_logico_silos)
            if registro_silos.stock > mayor_stock:
                nombre_silo_mayor_stock = registro_silos.nomsil
                mayor_stock = registro_silos.stock
                
            if registro_silos.codprod not in codprod[0]:
                codprod[0].append("")
                codprod[1].append(registro_silos.codprod)
                codprod[2].append(0)
                codprod[3].append(0 + registro_silos.stock)
                codprod[4].append(0)
        
        while archivo_logico_operaciones.tell() < longitud_operaciones:
            cant_cupos_otorgados += 1
            registro_operaciones = pickle.load(archivo_logico_operaciones)
            
            for x in codprod[1]:
                menor = 100000000000
                if registro_operaciones.codprod == x:
                    indice = codprod[1].index(x)
                    codprod[2][indice] += 1
                    codprod[4][indice] = registro_operaciones.pesobruto - registro_operaciones.tara
                    if registro_operaciones.pesobruto < menor:
                        codprod[0][indice] = registro_operaciones.patente.strip()
                    
            if registro_operaciones.estado == "A":
                cant_camiones_recibidos += 1
            elif registro_operaciones.estado == "R" and registro_operaciones.fecha == fecha_ingresada:
                patentes_rechazadas.append(registro_operaciones.patente)
                
        archivo_logico_operaciones.flush()
        archivo_logico_silos.flush()
        archivo_logico_silos.close()
        archivo_logico_operaciones.close()

    print(f"Cantidad de cupos otorgados: {cant_cupos_otorgados}")
    print(f"Cantidad de camiones recibidos: {cant_camiones_recibidos}")
    
    if os.path.exists("PRODUCTOS.dat"):
        registro_productos = main_TP3.Productos()
        archivo_logico_productos = open("PRODUCTOS.dat", "rb")
        longitud_productos = os.path.getsize("PRODUCTOS.dat")
        for prod in codprod[1]:
            while archivo_logico_productos.tell() < longitud_productos:
                registro_productos = pickle.load(archivo_logico_productos)
                if registro_productos.codprod == prod:
                    indice = codprod[1].index(prod)
                    print(f"la cantidad de camiomnes del producto {registro_productos.nomprod.strip()}, de codigo {registro_productos.codprod}, es: {codprod[2][indice]}")
                    if codprod[2][indice] == 0:
                        print("No se registraron camiones de este producto")
                    else: 
                        print(f"La pantente del camión que menos descargó de ese producto es: {codprod[0][indice]}")
                        print(f"El promedio del peso neto por camión de este producto es: {codprod[4][indice]/codprod[2][indice]}")
                    print(f"El peso neto del stock del mismo producto es: {codprod[3][indice]}")
                    print("----------------------------------------------")
            archivo_logico_productos.seek(io.SEEK_SET)
        archivo_logico_productos.flush()
        archivo_logico_productos.close()
    else:
        print("No se han ingresados productos aún")
        
    if mayor_stock == 0:
        print(f"No existen silos creados para los productos existentes o no existen productos")
    else:
        print(f"El nombre del silo con mayor stock es: {nombre_silo_mayor_stock.strip()}, con un stock de: {mayor_stock}")
    
    print(f"Listado de las patentes rechazadas el día {fecha_ingresada} es: {patentes_rechazadas}")
    
    option = input_validation_TP3.check_int()
    if option != 0:
        print(f"{WARNING}Seleccione una opcion válida del menú{NORMAL}")   
    
          
menu_reportes()
