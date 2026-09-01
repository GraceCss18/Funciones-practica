# ============================================
# EJERCICIOS - Funciones en Python
# ============================================

# --------------------------------------------
# NIVEL BÁSICO
# --------------------------------------------

# Ejercicio 1: Crea una función llamada "saludar_usuario" que 
# reciba un nombre como parámetro, y muestre "Bienvenido, [nombre]"

def saludar_usuario(nombre):
    print(f"Buenas, eres bienvenido al sistema {nombre}")

saludar_usuario("Graciela")

print("--------------------------------------------")
print("--------------------------------------------")


# Ejercicio 2: Crea una función "es_mayor_edad" que reciba una edad 
# y devuelva (return) True si es mayor o igual a 18, o False si no

def esMayorDeEdad (edad):
    if edad >= 18:
        return True
    else:
        return False

print(f"Usted, {esMayorDeEdad} ")
