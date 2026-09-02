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

def esMayorDeEdad(edad):
    if edad >= 18:
        return True
    else: 
        return False

print(esMayorDeEdad(20))
print(esMayorDeEdad(15))
print(esMayorDeEdad(90))
print(esMayorDeEdad(14))
print("--------------------------------------------")
print("--------------------------------------------")

# Ejercicio 3: Crea una función "calcular_precio_con_iva" que 
# reciba un precio y devuelva ese precio con el 19% de IVA agregado

def calcularPrecioIva (precio):
    iva = precio * 0.19
    precioFinal = precio + iva
    return precioFinal

print(f"Su precio final es: {calcularPrecioIva(30)}")
print("--------------------------------------------")
print("--------------------------------------------")


# --------------------------------------------
# NIVEL INTERMEDIO
# --------------------------------------------

# Ejercicio 4: Crea una función "contar_vocales" que reciba una 
# palabra y devuelva cuántas vocales tiene

def contadorVocal(palabra):
    #los contadores debo indiciarles desde donde inciar
    palabra = palabra.lower()
    contador = 0
    for letra in palabra:
        if letra in "aeiou":
            contador = contador + 1       
    return contador   

print(contadorVocal("hola"))
print(contadorVocal("Graciela"))
print(contadorVocal("antroPOmorfIco"))
print("--------------------------------------------")
print("--------------------------------------------")






