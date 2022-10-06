import user_menu_TP3
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""
class Operaciones:
    def _init_(self):
        self.patente = ""
        self.codprod = 0
        self.estado = ""
        self.fecha = ""
        self.pesobruto = 0
        self.tara = 0

class Productos:
    def _init_(self):
        self.codprod = 0
        self.nomprod = ""
        self.activo = False

class Rubros:
    def _init_(self):
        self.codrub = 0
        self.nomrub = ""

class RubrosxProducto:
    def _init_(self):
        self.codrubx = 0
        self.codprodx = ""
        self.vmin = 0.0
        self.vmax = 0.0

class Silos:
    def _init_(self):
        self.codsil = 0
        self.nomsil = ""
        self.codprods = 0
        self.stock = 0

if __name__ == "__main__":
    user_menu_TP3.menu_principal()