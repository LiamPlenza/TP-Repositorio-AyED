import main_TP3, io, pickle, archivos_TP3, time, os

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
    
    codprod = [[],[],[],[]] # nombre del silo, codigo del producto, cantidad de camiones, cantidad de stock
    cant_cupos_otorgados = 0
    cant_camiones_recibidos = 0
    registro_silos = main_TP3.Silos()
    registro_operaciones = main_TP3.Operaciones()
    
    if os.path.exists("OPERACIONES.dat"):
        archivo_logico_silos = open("SILOS.dat", "rb")
        archivo_logico_operaciones = open("OPERACIONES.dat", "rb")
        longitud_silos = os.path.getsize("SILOS.dat")
        longitud_operaciones = os.path.getsize("OPERACIONES.dat")
        
        while archivo_logico_silos.tell() < longitud_silos:
            registro_silos = pickle.load(archivo_logico_silos)
            if registro_silos.codprod not in codprod[0]:
                codprod[0].append(registro_silos.nomsil.strip())
                codprod[1].append(registro_silos.codprod)
                codprod[2].append(0)
                codprod[3].append(0 + registro_silos.stock)
        
        while archivo_logico_operaciones.tell() < longitud_operaciones:
            cant_cupos_otorgados += 1
            registro_operaciones = pickle.load(archivo_logico_operaciones)
            
            for x in codprod[1]:
                if registro_operaciones.codprod == x:
                    indice = codprod[1].index(x)
                    codprod[2][indice] += 1
                    
            if registro_operaciones.estado == "A":
                cant_camiones_recibidos += 1

    print(f"Cupos otorgados: {cant_cupos_otorgados}")
    print(f"Cantidad de productos con silos: {len(codprod[0])}, {codprod}")
    

#archivo_logico = open("SILOS.dat", "rb")
#long = os.path.getsize("SILOS.dat")
#registro = main_TP3.Silos()
#while archivo_logico.tell() < long:
#    registro = pickle.load(archivo_logico)
#    print(f"{registro.codsil}, {registro.nomsil}, {registro.codprod}, {registro.stock}")
          
menu_reportes()
