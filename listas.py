# Ejercicio 5: Crea una función "buscar_en_lista" que reciba una 
# lista y un valor a buscar, y devuelva True si el valor está en 
# la lista, o False si no
def buscarLista (lista, valor):
    if valor in lista:
        return True
    else:
        return False

frutas = ["manzana", "pera", "mango", "fresas", "uva"]
print(buscarLista(frutas, "fresas"))
print(buscarLista(frutas, "banano"))
print(buscarLista(frutas, "pera"))
print("----------------------------------------------")
print("----------------------------------------------")

# Ejercicio 6: Crea una función "promedio" que reciba una lista de 
# números y devuelva el promedio (usa sum() y len())

def promedio(numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    resultado = suma / cantidad
    return resultado

print(promedio([2, 4, 6]))
print(promedio([3, 5, 10]))
print(promedio([6, 7, 8]))
print("----------------------------------------------")
print("----------------------------------------------")

#Ejercicio 7: Crea una función "filtrar_mayores" que reciba una 
# lista de números y devuelva una nueva lista solo con los 
# números mayores a 50
def filtroMayores(numeros):
    resultado = []
    for numero in numeros:
        if numero > 50:
            resultado.append(numero)
    return resultado

print(filtroMayores([30, 20, 15, 50, 70, 65, 36]))
print(filtroMayores([3, 40, 25, 60, 80, 33, 12]))
print(filtroMayores([6, 7, 8, 9, 10, 30, 90]))
print("----------------------------------------------")
print("----------------------------------------------")


# Ejercicio 8 (con valor por defecto): Crea una función 
# "generar_descuento" que reciba un precio y un porcentaje de 
# descuento (por defecto 10%), y devuelva el precio ya descontado
def generarDescuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precioFinal = precio - descuento
    return precioFinal

print(generarDescuento(100, 250))
print(generarDescuento(40, 12))
print(generarDescuento(200, 150))
