# Listas

## Para que usamos las listas?

lista_de_kilos_por_pasajero = [
    33, 10, 15, 20,
    45, 55, 10, 8,
    99, 12, 20, 1
]

for equipaje in lista_de_kilos_por_pasajero:
    print(equipaje)

print("TOTAL: ", sum(lista_de_kilos_por_pasajero))

print("-" * 40)

# Anatomia de una lista
# - CORCHETES QUE LA ENCIERRAN
# - Elementos estan separados por comas
# POS     1º   2º   3º   4º
# INDICE  0    1    2    3
lista = ["a", "b", 33, "d"] 

# Imprimimos toda la lista
print(lista)
# Imprimimos el elemento 2
print(lista[2])

# Podemos modificar los elementos de una lista
lista[1] = "Patata"
print(lista)

# Puedo operar con los elementos de una lista
total = 10 + lista[2]
print(f"TOTAL: {total}")

# El tipo de lista es list
# El tipo de cada elemento depende del elemento
print("type(lista)   :", type(lista))
print("type(lista[2]):", type(lista[2]))
print("type(lista[3]):", type(lista[3]))

# la longitud de una lsita es entero

cantidad_elementos = len(lista)
print(cantidad_elementos, type(cantidad_elementos))
