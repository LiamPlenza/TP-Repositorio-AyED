import user_menu_TP2
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás Maximiliano García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""
if __name__ == "__main__":
    identificador = pesos = tara = [0]*8
    cupos = estado = [""]*8
    productos = [""] * 3

    user_menu_TP2.menu_principal(productos, cupos, identificador, pesos, estado, tara)