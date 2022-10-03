import user_menu_TP3
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""
class Productos:
    def __init__(self):
        self.codprod = 0
        self.nomprod = ""

class Rubros:
    def __init__(self):
        self.codrub = 0
        self.nomrub = ""

class RubrosxProducto:
    def __init__(self):
        self.codrubx = 0
        self.codprodx = ""
        self.vmin = 0.0
        self.vmax = 0.0

class Silos:
    def __init__(self):
        self.codsil = 0
        self.nomsil = ""
        self.codprods = 0
        self.stock = 0

if __name__ == "__main__":
    pesos = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    estado = [""]*8
    matriz_camiones = [""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3





"""
DECLARATORIA DE MATRICES

pesos[0..7][0..2] of int
estado[0..7] of char (en python se declara como string pero lo utilizamos como char por lo dicho en la consigna)
productos[0..2] of string
matriz_camiones[0..7][0..2] of string

"""
user_menu_TP3.menu_principal(matriz_camiones, pesos, estado, Productos, Rubros, RubrosxProducto, Silos)