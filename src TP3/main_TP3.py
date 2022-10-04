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
        self.activo = False

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
    user_menu_TP3.menu_principal()