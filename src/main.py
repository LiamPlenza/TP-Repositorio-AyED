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
    
    class Maiz:
        camionesMaiz = 0
        pesoNetoMaiz = 0
        pesoMenorMaiz = 0
        promPesoNetoM = 0
        patMenorMaiz = ""

    titulares= []

    class Soja:
        camionesSoja = 0
        pesoNetoSoja = 0
        pesoMayorSoja = 0
        promPesoNetoS = 0
        patMenorSoja = ""

    user_menu.menu_principal(Maiz,Soja,titulares)