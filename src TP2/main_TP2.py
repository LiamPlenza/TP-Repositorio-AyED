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
    pesos = [0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3,[0]*3
    estado = [""]*8
    productos = [""] * 3
    matriz_camiones = [""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3,[""]*3
"""
DECLARATORIA DE MATRICES

pesos[0..7][0..3] of int
estado[0..7] of char (en python se declara como string pero lo utilizamos como char por lo dicho en la consigna)
productos[0..2] of string
matriz_camiones[0..7][0..3] of string

"""
user_menu_TP2.menu_principal(productos, matriz_camiones, pesos, estado)