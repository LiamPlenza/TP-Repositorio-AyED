import os, time, user_menu
"""
Trabajo Práctico N1 - Algoritmos y Estructura de Datos - Ingeniería en Sistemas - UTN
Integrantes:
    Nicolás Maximiliano García - Comisión 107
    Lucio Mondelli - Comisión 107
    Liam Nahuel Plenza - Comisión 104
    Tomas Joel Wardoloff - Comisión 108
"""

if __name__ == "__main__":
    # inicialización de las variables a mostrar
    titulares = []
    maiz = user_menu.ObjetoMaiz()
    soja = user_menu.ObjetoSoja()
    user_menu.menu_principal(maiz,soja, titulares)
